import requests
from datetime import datetime
from collections import defaultdict
import time

token = ""
project_number = 1 
owner = "joaomrpimentel" 
repo = "watchman"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.mockingbird-preview+json",
}

def parse_date(date_str):
    if date_str:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return None

def get_issues(owner, repo):
    """Pega todas as issues paginando."""
    issues = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {"state": "all", "per_page": 100, "page": page}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        issues.extend(data)
        page += 1
    return issues

def get_issue_timeline(owner, repo, issue_number):
    """Pega o timeline de uma issue."""
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

issues = get_issues(owner, repo)

# Dicionários para armazenar dados por usuário assigned
lead_times = defaultdict(list)
cycle_times = defaultdict(list)
throughput = defaultdict(lambda: defaultdict(int))  # user -> {YYYY-MM: count}

for issue in issues:
    if "pull_request" in issue:
        # Opcional: pular PRs se quiser só issues
        continue
    
    issue_number = issue["number"]
    created_at = parse_date(issue["created_at"])
    closed_at = parse_date(issue["closed_at"])
    assignees = [a["login"] for a in issue.get("assignees", [])] or ["Unassigned"]

    if not closed_at:
        # Métricas só pra issues fechadas
        continue

    timeline = get_issue_timeline(owner, repo, issue_number)

    # Variáveis para armazenar eventos do projeto
    em_progresso_date = None
    feito_date = None

    # Procurar eventos de movimentação no timeline
    for event in timeline:
        # Eventos de "moved" geralmente aparecem no "event" ou em "event"=="moved_columns_in_project"
        # Vamos filtrar pelo texto do evento
        if event.get("event") == "moved_columns_in_project":
            # Exemplo de texto do evento no campo "project_card" ou "project_column_name"
            # Mas para garantir, vamos olhar no "project_card" ou "commit_id"
            # A API não dá muito padrão, mas podemos usar o campo "project_card" ou "project_column_name"
            # Vamos pegar a descrição "moved this from ... to ..."
            # Se disponível, verificar as colunas
            pass

        # Alternativamente, no "event" == "moved", ou no campo "commit_id", ou "project_card" tem coluna
        # Como não é super consistente, a forma mais garantida é analisar o campo "source" e "destination" do "project_card" se existir

        # Simplificando: vamos buscar texto nos campos "event" ou "commit_id" que diga "moved from" ou "moved to"

        # Porém a resposta do timeline é JSON com vários tipos diferentes de eventos. O texto que vc viu no web é do comentário do evento, mas a API pode ter dados estruturados.

        # Para simplificar aqui, vamos olhar o campo "event" e "commit_id" e "project_card"

        # Melhor abordagem: olhar no campo "event" == "moved_columns_in_project" e pegar as colunas do "project_card"

        if event.get("event") == "moved_columns_in_project":
            # Pega o nome da coluna depois da movimentação
            new_col = event.get("project_card", {}).get("column_name")
            event_date = parse_date(event.get("created_at"))
            if new_col == "Em Progresso":
                em_progresso_date = event_date
            elif new_col == "Feito":
                feito_date = event_date

    # Se não achou datas pela movimentação, tenta pelo fechado para feito
    if not feito_date:
        feito_date = closed_at

    # Calcula lead time (criação até fechamento)
    lead_time_days = (feito_date - created_at).days if (feito_date and created_at) else None
    # Calcula cycle time (em progresso até feito)
    cycle_time_days = (feito_date - em_progresso_date).days if (feito_date and em_progresso_date) else None

    for user in assignees:
        if lead_time_days is not None:
            lead_times[user].append(lead_time_days)
        if cycle_time_days is not None:
            cycle_times[user].append(cycle_time_days)
        ym = feito_date.strftime("%Y-%m") if feito_date else None
        if ym:
            throughput[user][ym] += 1

    # Pequena pausa para respeitar rate limit
    time.sleep(0.2)

# nome do arquivo
filename = "metricas_issues.txt"

# Resultados
with open(filename, "w", encoding="utf-8") as f:
    f.write("Métricas por usuário (assigned):\n\n")
    for user in lead_times.keys():
        avg_lead = sum(lead_times[user]) / len(lead_times[user]) if lead_times[user] else 0
        avg_cycle = sum(cycle_times[user]) / len(cycle_times[user]) if cycle_times[user] else 0
        f.write(f"Usuário: {user}\n")
        f.write(f"  - Lead Time médio (dias): {avg_lead:.2f}\n")
        f.write(f"  - Cycle Time médio (dias): {avg_cycle:.2f}\n")
        f.write(f"  - Throughput por mês:\n")
        for ym, count in sorted(throughput[user].items()):
            f.write(f"    {ym}: {count}\n")
        f.write("\n")

print(f"Métricas salvas no arquivo {filename} com encoding utf8.")
