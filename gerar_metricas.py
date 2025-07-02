import requests
from datetime import datetime, timedelta
from collections import defaultdict
import time
import matplotlib
matplotlib.use('Agg') # Set the backend to 'Agg' for non-interactive plotting
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Configurações (Preencha com suas informações) ---
# ATENÇÃO: Nunca exponha seu token em repositórios públicos!
# Para segurança, considere usar variáveis de ambiente ou um arquivo .env
token = "" # <-- COLOQUE SEU TOKEN AQUI
project_number = 1 
owner = "joaomrpimentel" 
repo = "watchman"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.mockingbird-preview+json", # Para acessar dados de projetos
}

def parse_date(date_str):
    """Parses an ISO 8601 date string to a datetime object."""
    if date_str:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return None

def get_issues(owner, repo):
    """Fetches all issues (including pull requests treated as issues) from a repository, handling pagination."""
    issues = []
    page = 1
    print(f"Fetching issues for {owner}/{repo}...")
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {"state": "all", "per_page": 100, "page": page}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        data = resp.json()
        if not data:
            break
        issues.extend(data)
        page += 1
        print(f"  Fetched page {page-1}, total issues: {len(issues)}")
    print(f"Finished fetching {len(issues)} issues.")
    return issues

def get_issue_timeline(owner, repo, issue_number):
    """Fetches the timeline events for a specific issue, handling pagination."""
    timeline = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/timeline"
        params = {"per_page": 100, "page": page}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        timeline.extend(data)
        page += 1
    return timeline

# --- Main Data Collection Logic ---
print("Starting data collection...")
issues = get_issues(owner, repo)

lead_times = defaultdict(list)
cycle_times = defaultdict(list)
throughput = defaultdict(lambda: defaultdict(int)) # user -> {YYYY-MM: count} (issues closed by assigned user)
bugs_reported = defaultdict(int)
bugs_lead_time = defaultdict(list)
issues_created_by_author = defaultdict(int) 
issues_closed_by_assignee = defaultdict(int)

# New data structures for Burndown/Burnup
issues_created_daily = defaultdict(int)
issues_closed_daily = defaultdict(int)
project_start_date = None
project_end_date = datetime.now() # Initialize with current date, will update if issues are newer

for i, issue in enumerate(issues):
    if "pull_request" in issue:
        # Skip Pull Requests if you only want to analyze issues
        continue
    
    issue_number = issue["number"]
    created_at = parse_date(issue["created_at"])
    closed_at = parse_date(issue["closed_at"])
    assignees = [a["login"] for a in issue.get("assignees", [])] or ["Unassigned"]
    author = issue["user"]["login"] # Get the author of the issue

    # Update project start date
    if created_at and (project_start_date is None or created_at < project_start_date):
        project_start_date = created_at

    # Increment issues created by this author and daily created count
    issues_created_by_author[author] += 1
    if created_at:
        issues_created_daily[created_at.date()] += 1

    if not closed_at:
        # Metrics are only calculated for closed issues
        continue

    labels = [label["name"].lower() for label in issue.get("labels", [])]
    is_bug = "bug" in labels

    # Fetch timeline for project board events
    timeline = get_issue_timeline(owner, repo, issue_number)

    em_progresso_date = None
    feito_date = None

    # Try to find "In Progress" and "Done" dates from project board movements
    for event in timeline:
        if event.get("event") == "moved_columns_in_project":
            # The 'project_card' object contains details about the card and its column
            project_card = event.get("project_card", {})
            column_name = project_card.get("column_name")
            event_date = parse_date(event.get("created_at"))
            
            # Assuming your column names are exactly "Em Progresso" and "Feito"
            if column_name == "Em Progresso":
                if em_progresso_date is None or event_date < em_progresso_date:
                    em_progresso_date = event_date
            elif column_name == "Feito":
                if feito_date is None or event_date > feito_date: # Take the last "Done" date
                    feito_date = event_date
    
    # Fallback: if "Feito" column movement not found, use issue closed_at date
    if not feito_date:
        feito_date = closed_at

    # Calculate Lead Time (creation to done/closed)
    lead_time_days = (feito_date - created_at).days if (feito_date and created_at) else None
    
    # Calculate Cycle Time (in progress to done/closed)
    cycle_time_days = (feito_date - em_progresso_date).days if (feito_date and em_progresso_date) else None

    for user in assignees:
        if lead_time_days is not None:
            lead_times[user].append(lead_time_days)
        if cycle_time_days is not None:
            cycle_times[user].append(cycle_time_days)
        
        ym = feito_date.strftime("%Y-%m") if feito_date else None
        if ym:
            throughput[user][ym] += 1
            issues_closed_by_assignee[user] += 1 # Increment issues closed by this assignee
            if closed_at:
                issues_closed_daily[closed_at.date()] += 1 # Increment daily closed count

        if is_bug:
            bugs_reported[user] += 1
            if lead_time_days is not None: # Use lead_time_days for bug lead time
                bugs_lead_time[user].append(lead_time_days)

    # Small pause to respect GitHub API rate limits
    if (i + 1) % 10 == 0: # Pause every 10 issues to be safe
        print(f"Processed {i+1}/{len(issues)} issues. Pausing for 0.5s...")
        time.sleep(0.5)

print("Data collection complete. Generating reports and graphs...")

# --- Prepare Data for Plotting ---
users_data = []
for user in lead_times.keys():
    avg_lead = sum(lead_times[user]) / len(lead_times[user]) if lead_times[user] else 0
    avg_cycle = sum(cycle_times[user]) / len(cycle_times[user]) if cycle_times[user] else 0
    
    users_data.append({
        "User": user,
        "Avg_Lead_Time": avg_lead,
        "Avg_Cycle_Time": avg_cycle,
        "Bugs_Reported": bugs_reported[user],
        "Issues_Closed": issues_closed_by_assignee[user] # Add issues closed count
    })

# --- Save Text Report ---
filename = "metricas_issues.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write("Métricas por usuário (assigned):\n\n")
    for user_data in users_data:
        user = user_data["User"]
        f.write(f"Usuário: {user}\n")
        f.write(f"  - Lead Time médio (dias): {user_data['Avg_Lead_Time']:.2f}\n")
        f.write(f"  - Cycle Time médio (dias): {user_data['Avg_Cycle_Time']:.2f}\n")
        f.write(f"  - Bugs reportados: {user_data['Bugs_Reported']}\n")
        f.write(f"  - Issues Fechadas: {user_data['Issues_Closed']}\n") # New: Write issues closed
        
        if user in bugs_lead_time:
            avg_bug_lead = sum(bugs_lead_time[user]) / len(bugs_lead_time[user]) if bugs_lead_time[user] else 0
            f.write(f"  - Lead Time médio para bugs: {avg_bug_lead:.2f}\n")
        
        f.write(f"  - Throughput por mês:\n")
        for ym, count in sorted(throughput[user].items()):
            f.write(f"    {ym}: {count}\n")
        f.write("\n")

    # New: Write issues created by author
    f.write("Issues Criadas por Autor:\n\n")
    for author, count in sorted(issues_created_by_author.items()):
        f.write(f"  - {author}: {count}\n")
    f.write("\n")

print(f"Métricas salvas no arquivo {filename} com encoding utf8.")

# --- Generate and Save Graphs ---
output_dir = "metricas_graficos"
os.makedirs(output_dir, exist_ok=True) # Create directory if it doesn't exist

sns.set_theme(style="whitegrid")

# 1. Gráfico de Barras: Lead Time Médio e Cycle Time Médio por Usuário
if users_data:
    # Use a new figure and axes for each plot to prevent conflicts
    fig1, ax1 = plt.subplots(figsize=(12, 7))
    users = [d["User"] for d in users_data]
    avg_lead_times = [d["Avg_Lead_Time"] for d in users_data]
    avg_cycle_times = [d["Avg_Cycle_Time"] for d in users_data]

    x = range(len(users))
    width = 0.35

    rects1 = ax1.bar([i - width/2 for i in x], avg_lead_times, width, label='Lead Time Médio', color='skyblue')
    rects2 = ax1.bar([i + width/2 for i in x], avg_cycle_times, width, label='Cycle Time Médio', color='lightcoral')

    ax1.set_ylabel('Dias')
    ax1.set_title('Lead Time Médio e Cycle Time Médio por Usuário')
    ax1.set_xticks(x)
    ax1.set_xticklabels(users, rotation=45, ha="right")
    ax1.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "lead_cycle_time_por_usuario.png"))
    plt.close(fig1) # Close the figure to free memory
    print(f"Gráfico 'lead_cycle_time_por_usuario.png' salvo em '{output_dir}'")

# 2. Gráfico de Barras: Bugs Reportados por Usuário
if users_data:
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    users = [d["User"] for d in users_data]
    bugs_counts = [d["Bugs_Reported"] for d in users_data]

    sns.barplot(x=users, y=bugs_counts, palette="viridis", ax=ax2)
    ax2.set_xlabel('Usuário')
    ax2.set_ylabel('Número de Bugs Reportados')
    ax2.set_title('Bugs Reportados por Usuário')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "bugs_reportados_por_usuario.png"))
    plt.close(fig2) # Close the figure to free memory
    print(f"Gráfico 'bugs_reportados_por_usuario.png' salvo em '{output_dir}'")

# 3. Gráfico de Linha: Throughput por Mês por Usuário
if throughput:
    fig3, ax3 = plt.subplots(figsize=(15, 8))
    for user, monthly_data in throughput.items():
        sorted_months = sorted(monthly_data.keys())
        counts = [monthly_data[month] for month in sorted_months]
        ax3.plot(sorted_months, counts, marker='o', label=user)

    ax3.set_xlabel('Mês')
    ax3.set_ylabel('Número de Issues Fechadas')
    ax3.set_title('Throughput Mensal por Usuário')
    plt.xticks(rotation=45, ha="right")
    ax3.legend(title='Usuário')
    ax3.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "throughput_mensal_por_usuario.png"))
    plt.close(fig3) # Close the figure to free memory
    print(f"Gráfico 'throughput_mensal_por_usuario.png' salvo em '{output_dir}'")

# 4. Gráfico de Barras: Issues Criadas por Autor
if issues_created_by_author:
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    authors = list(issues_created_by_author.keys())
    counts = list(issues_created_by_author.values())

    sns.barplot(x=authors, y=counts, palette="magma", ax=ax4)
    ax4.set_xlabel('Autor')
    ax4.set_ylabel('Número de Issues Criadas')
    ax4.set_title('Issues Criadas por Autor')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "issues_criadas_por_autor.png"))
    plt.close(fig4)
    print(f"Gráfico 'issues_criadas_por_autor.png' salvo em '{output_dir}'")

# 5. Gráfico de Barras: Issues Fechadas por Atribuído (Assignee)
if issues_closed_by_assignee:
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    assignees = list(issues_closed_by_assignee.keys())
    counts = list(issues_closed_by_assignee.values())

    sns.barplot(x=assignees, y=counts, palette="cividis", ax=ax5)
    ax5.set_xlabel('Atribuído')
    ax5.set_ylabel('Número de Issues Fechadas')
    ax5.set_title('Issues Fechadas por Atribuído')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "issues_fechadas_por_atribuido.png"))
    plt.close(fig5)
    print(f"Gráfico 'issues_fechadas_por_atribuido.png' salvo em '{output_dir}'")

# NEW: 6. Gráfico de Burndown
if project_start_date and issues: # Ensure there's data to plot
    # Normalize project_end_date to just date for iteration
    current_end_date = project_end_date.date()
    
    # Generate all dates from project start to end
    all_dates = []
    current_date = project_start_date.date()
    while current_date <= current_end_date:
        all_dates.append(current_date)
        current_date += timedelta(days=1)

    # Calculate cumulative created and closed issues
    cumulative_created = []
    cumulative_closed = []
    total_issues_at_start = 0

    for date in all_dates:
        total_issues_at_start += issues_created_daily.get(date, 0)
        cumulative_created.append(total_issues_at_start)
        
        # Calculate cumulative closed for burnup
        if not cumulative_closed:
            cumulative_closed.append(issues_closed_daily.get(date, 0))
        else:
            cumulative_closed.append(cumulative_closed[-1] + issues_closed_daily.get(date, 0))

    # For Burndown, remaining work = total scope - cumulative closed
    remaining_work = [total_issues_at_start - closed for closed in cumulative_closed]
    
    # Ensure remaining_work does not go below zero if total_issues_at_start is not the final total
    # A more accurate burndown would consider the *current* total created issues up to that day.
    # Let's re-calculate remaining_work based on cumulative_created up to that day.
    
    # Recalculate remaining_work for a more accurate burndown
    remaining_work_accurate = []
    for i, date in enumerate(all_dates):
        current_total_scope = cumulative_created[i]
        current_closed_count = cumulative_closed[i]
        remaining_work_accurate.append(max(0, current_total_scope - current_closed_count))


    fig6, ax6 = plt.subplots(figsize=(15, 8))
    ax6.plot(all_dates, remaining_work_accurate, label='Trabalho Restante', color='red', marker='o', markersize=4)
    # Optional: Ideal Burndown Line (if you have a target end date and initial scope)
    # For a simple burndown, we just show remaining work against actual scope.

    ax6.set_xlabel('Data')
    ax6.set_ylabel('Número de Issues Restantes')
    ax6.set_title('Gráfico de Burndown')
    ax6.legend()
    ax6.grid(True)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "burndown_chart.png"))
    plt.close(fig6)
    print(f"Gráfico 'burndown_chart.png' salvo em '{output_dir}'")

# NEW: 7. Gráfico de Burnup
if project_start_date and issues:
    fig7, ax7 = plt.subplots(figsize=(15, 8))
    ax7.plot(all_dates, cumulative_created, label='Escopo Total (Issues Criadas)', color='blue', marker='o', markersize=4)
    ax7.plot(all_dates, cumulative_closed, label='Trabalho Concluído (Issues Fechadas)', color='green', marker='o', markersize=4)

    ax7.set_xlabel('Data')
    ax7.set_ylabel('Número de Issues')
    ax7.set_title('Gráfico de Burnup')
    ax7.legend()
    ax7.grid(True)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "burnup_chart.png"))
    plt.close(fig7)
    print(f"Gráfico 'burnup_chart.png' salvo em '{output_dir}'")

print(f"Todos os gráficos foram salvos na pasta '{output_dir}'.")
