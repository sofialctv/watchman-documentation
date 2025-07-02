---
sidebar_position: 5
title: Throughput
---

## O que é?

O **Throughput** é uma métrica quantitativa que indica o **número de unidades de trabalho concluídas** em um determinado intervalo de tempo. Em contextos ágeis, essas unidades podem ser *issues*, *histórias de usuário*, *bugs resolvidos*, *pull requests entregues*, entre outros.

Ela mede a **cadência de entrega do time**, sendo crucial para entender a capacidade real de produção ao longo do tempo. Diferente de Lead Time ou Cycle Time, que focam em *duração*, o Throughput foca em *volume*.

> Throughput responde à pergunta: **"Quantas tarefas entregamos por semana, sprint ou mês?"**

---

## Como medir?

### Ferramenta:

- **GitHub Projects**: via filtros e exports por *labels* e *milestones*.

### Procedimento:

1. **Definir o intervalo de análise**: semanal, quinzenal (sprint), mensal etc.
2. **Filtrar tarefas finalizadas no período**, com base no status (“Done”, “Closed”, “Merged”) e data de conclusão.
3. **Contar o total de entregas** no intervalo.
4. **Opcional:** Classificar por tipo (bug, feature, refatoração) ou tamanho (story points) para análises segmentadas.

---

## Visualização e Análise

A métrica pode ser visualizada com:

- **Gráficos de barras** (entregas por período)
- **Gráficos de linha** (tendência ao longo do tempo)
- **Gráficos cumulativos** (visão acumulada de entregas)

> Flutuações abruptas podem indicar problemas com escopo, bloqueios, mudanças na equipe ou falhas de planejamento.

---

## Como essa métrica ajuda?

- **Capacidade de entrega**: revela quantas tarefas, em média, a equipe consegue concluir por sprint.
- **Planejamento baseado em dados**: ajuda a montar sprints mais realistas, evitando sobrecarga ou subutilização.
- **Identificação de instabilidade**: variações abruptas podem indicar problemas no fluxo de trabalho.
- **Base para previsão**: combinada com outras métricas como *Cycle Time*, permite projeções do tipo “quando teremos X tarefas prontas?”.
- **Suporte à melhoria contínua**: acompanhar o throughput ao longo de várias sprints ajuda a medir o impacto de ações como redefinição de WIP, melhoria de processos ou treinamento da equipe.

---

## Boas práticas

- Considere somente tarefas realmente concluídas (não em revisão, teste ou bloqueadas).
- Use intervalos de tempo consistentes para análise (ex: sempre considerar a sprint fechada).
- Combine com outras métricas (Cycle Time, Lead Time, WIP) para formar uma visão mais sistêmica do fluxo.
- Monitore a estabilidade do throughput — equipes maduras tendem a ter variações pequenas.