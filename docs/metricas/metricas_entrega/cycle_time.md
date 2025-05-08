---
sidebar_position: 4
title: Cycle Time
---

## O que é?

O **Cycle Time** é uma métrica fundamental para análise de produtividade em engenharia de software, metodologias ágeis e DevOps. Ele mede o tempo decorrido **entre o início efetivo da execução de uma tarefa** (quando ela entra em desenvolvimento) até a sua **finalização** (quando é considerada entregue tecnicamente).

Diferente do **Lead Time**, que abrange todo o ciclo de vida da demanda (inclusive o tempo em que a tarefa está aguardando priorização ou revisão), o **Cycle Time** foca exclusivamente no período **produtivo**, isto é, o tempo em que a equipe esteve ativamente trabalhando naquela entrega.

> 📌 É uma métrica centrada na execução e, por isso, ajuda a entender a performance real do time de desenvolvimento.

---

## Como medir?

A medição do Cycle Time varia conforme o fluxo de trabalho e a ferramenta adotada, mas geralmente envolve a análise das transições de status da tarefa ao longo do seu ciclo.

### Ferramenta:

- **GitHub Projects**: rastreio de eventos como mudança para “In Progress” e encerramento de PR.

### Procedimento:

1. **Defina o ponto inicial**: normalmente, o momento em que a tarefa entra no status “Em Progresso” ou equivalente.
2. **Defina o ponto final**: a data em que a tarefa é marcada como “Concluída” (por exemplo, Done, Merged, ou Delivered).
3. **Registre os timestamps** dessas mudanças, utilizando APIs, exports CSV, integrações com BI, ou ferramentas internas.
4. **Cycle Time = Data de fim - Data de início do trabalho ativo**

---

## Visualização e Análise

A forma mais comum de visualização do Cycle Time é por meio de **gráficos de barras** (para comparar tarefas individuais), **histogramas** (para ver distribuição de tempos) ou **boxplots** (para entender a dispersão e outliers).

> 🔍 Uma análise estatística do Cycle Time permite encontrar **mediana**, **desvios padrões**, e tarefas fora da curva — pontos críticos para melhoria contínua.

---

## Como essa métrica ajuda?

- **Avaliação objetiva da eficiência da equipe** durante a execução.
- **Identificação de tarefas travadas ou com baixa fluidez**, sinalizando problemas de dependências, comunicação ou escopo.
- **Apoia decisões de refino de backlog**: tarefas com altos Cycle Times podem indicar quebras no slicing (tamanho excessivo, ambiguidade).
- **Redução de desperdícios** (muda-muda, espera, retrabalho) ao tornar visíveis os tempos improdutivos.
- **Aumento da previsibilidade de entregas**, com base no histórico de ciclos anteriores.

---

## Boas práticas

- ✅ Defina claramente os status do fluxo (“To Do”, “In Progress”, “Code Review”, “Done”) e mantenha consistência.
- ✅ Automatize a coleta de timestamps sempre que possível.
- ✅ Combine o Cycle Time com outras métricas, como **Throughput**, **Work In Progress (WIP)** e **Lead Time**, para análises mais robustas.
- ✅ Revise frequentemente tarefas com Cycle Time anormalmente alto em retrospectivas.

---