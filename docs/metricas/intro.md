---
sidebar_position: 2
title: Métricas Ágeis
---

As métricas ágeis são fundamentais para avaliar a performance da equipe, apoiar a tomada de decisão e impulsionar a melhoria contínua. Neste projeto, as métricas estão organizadas em três categorias principais: entrega, qualidade e satisfação.

## Objetivos da Medição Ágil

A adoção de métricas ágeis neste projeto visa:

1. Medir a eficiência na entrega de valor ao cliente
2. Monitorar a qualidade técnica das entregas
3. Avaliar o bem-estar e engajamento da equipe
4. Fornecer dados objetivos para retrospectivas e ajustes de processo
5. Aumentar a previsibilidade e reduzir riscos

## Categorias e Principais Métricas

### Métricas de Entrega

| Métrica                 | Definição | Coleta | Frequência |
|------------------------|-----------|--------|------------|
| **Lead Time**          | Tempo entre a criação e entrega de uma demanda | GitHub Projects, Jira, Azure DevOps | Por sprint |
| **Cycle Time**         | Tempo entre o início e a finalização da execução | GitHub Projects, Jira, Trello | Por sprint |
| **Throughput**         | Quantidade de entregas finalizadas em um período | GitHub Projects, DevLake | Por sprint |

### Métricas de Qualidade

| Métrica                 | Definição | Coleta | Frequência |
|------------------------|-----------|--------|------------|
| **Taxa de Defeitos**   | Número de bugs por entrega ou sprint | GitHub Issues, DevLake, SonarQube | Semanal ou por sprint |
| **Débito Técnico**     | Volume de código com problemas técnicos pendentes | SonarQube, DevLake | Mensal |
| **Tempo para correção de bugs** | Média de tempo entre a abertura e resolução de defeitos | GitHub Issues, Jira | Por sprint |

### Métricas de Satisfação

| Métrica                   | Definição | Coleta | Frequência |
|--------------------------|-----------|--------|------------|
| **Satisfação do Time**   | Grau de bem-estar e motivação da equipe | Formulários anônimos, FunRetro, TeamMood | Ao fim da sprint |
| **Feedback de Retrospectiva** | Pontos positivos e negativos levantados nas retrospectivas | Retrospectiva (manual) | A cada sprint |

## Ferramentas de Coleta de Dados

Duas opções principais estão sendo consideradas para coleta e visualização automática de métricas:

### GitHub Projects Graphs *(mais simples)*

- **Vantagens:** Já integrado ao repositório, fácil de configurar, visualizações automáticas (gráficos de issues, pull requests, etc).
- **Limitações:** Métricas limitadas, sem dashboards personalizados, pouca profundidade em métricas de qualidade.
- **Viável para:** Projetos menores, acompanhamento visual rápido, equipes já 100% no GitHub.

### DevLake *(mais completo)*

- **Vantagens:** Consolida dados de múltiplas fontes (GitHub, Jira, Jenkins, SonarQube), permite criação de dashboards personalizados com métricas de entrega, qualidade e produtividade.
- **Limitações:** Maior esforço de configuração, necessidade de infraestrutura para rodar.
- **Viável para:** Projetos com múltiplas ferramentas e necessidade de análise profunda e histórica.

## Aplicação no Projeto

As métricas serão utilizadas para:

- Monitorar a entrega contínua de valor
- Identificar gargalos no fluxo de trabalho
- Detectar falhas de qualidade de forma precoce
- Avaliar o engajamento e satisfação do time
- Apoiar decisões baseadas em dados nas retrospectivas