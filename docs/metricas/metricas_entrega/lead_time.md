---
sidebar_position: 3
title: Lead Time
---

## O que é?

O **Lead Time** é uma métrica fundamental utilizada em engenharia de software, DevOps e metodologias ágeis para mensurar o **tempo total decorrido entre a criação de uma solicitação** (ex: abertura de uma *issue*, *ticket* ou *história de usuário*) até sua **entrega efetiva** (como *deploy* em produção ou conclusão técnica formal).

Essa métrica abrange **todo o ciclo de vida da demanda**, incluindo:

- tempo em espera no backlog,
- tempo em desenvolvimento ativo,
- revisões de código,
- validações de qualidade (QA),
- testes de homologação,
- e etapas de aprovação.

> 📌 O Lead Time responde à pergunta: **“Quanto tempo levamos, do pedido até a entrega?”**

Diferentemente do *Cycle Time*, que mede apenas o tempo de trabalho ativo, o **Lead Time** oferece uma visão mais completa da jornada de entrega de valor ao cliente ou usuário final.

---

## Como medir?

### Ferramentas recomendadas:

- **GitHub Projects**: utilizar a data de criação e a data de fechamento da *issue* ou *pull request*.
- **Jira**: configurar o fluxo de trabalho para registrar transições de status; extrair relatórios como *Control Chart*.
- **Azure DevOps**: usar o *Work Item Analytics* ou dashboards personalizados para capturar o tempo entre "Criado" e "Concluído".
- **Linear, Trello, YouTrack, DevLake**: também oferecem integrações e relatórios que extraem essas informações.

### Procedimento:

1. **Defina o ponto de início** da medição: geralmente a data de criação da *issue*, ou o momento em que ela entra no backlog priorizado.
2. **Defina o ponto de término**: pode ser a data de fechamento da *issue*, *merge* da *pull request*, *deploy* em produção ou marcação como "Done".
3. **Calcule a diferença entre os dois pontos**.
4. **Automatize o processo** sempre que possível com queries, plugins ou dashboards conectados a ferramentas como Power BI, Grafana ou DevLake.

> 🔍 É recomendável manter uma definição consistente sobre o que significa “entrega” para o time — produção, homologação, aceite, etc.

---

## Visualização e Análise

- **Gráficos de dispersão** (Scatter Plot) com datas de início e duração.
- **Histogramas de Lead Time** para avaliar distribuição de entregas.
- **Control Charts** para monitorar variações e detectar anomalias.

Esses gráficos ajudam a identificar **outliers**, **padrões sazonais** e **tendências de melhoria ou regressão** ao longo do tempo.

---

## Como essa métrica ajuda?

O acompanhamento do Lead Time oferece uma série de benefícios estratégicos e operacionais:

- **Avaliação de eficiência operacional**: mostra quanto tempo o time leva, do pedido à entrega, para gerar valor.
- **Identificação de gargalos**: revela onde as demandas passam mais tempo — como QA, análise, ou em espera para review.
- **Previsibilidade**: permite realizar estimativas mais precisas com base em dados históricos de entrega.
- **Melhoria contínua**: serve como insumo em retrospectivas ágeis e reuniões de Kaizen para refinar o fluxo de trabalho.
- **Transparência e comunicação**: ajuda na comunicação de desempenho com stakeholders e clientes.

---

## Boas práticas

- ✅ Use **amostras suficientes** para evitar conclusões com base em poucos dados.
- ✅ **Padronize a definição de “pronto”** para que a métrica seja comparável entre projetos ou sprints.
- ✅ Combine com outras métricas como *Cycle Time*, *WIP* e *Throughput* para uma visão sistêmica.
- ✅ **Evite comparações isoladas entre equipes** — o Lead Time deve ser usado principalmente para medir evolução dentro de um mesmo contexto.

---