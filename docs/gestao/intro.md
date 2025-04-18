---
sidebar_position: 1
title: Introdução
---
## Plataforma de Gestão

Escolhemos o **[GitHub Projects](https://docs.github.com/pt/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)** como *centralizador das atividades*, servindo como fonte única de verdade para acompanhamento das tarefas dos times de Gestão e Desenvolvimento.

### Organização do GitHub Projects
O GitHub Projects será estruturado com os seguintes campos e configurações para garantir rastreabilidade e clareza nas tarefas:

#### Campos Padrão
- **Status**:  
  - `A fazer`: Item ainda não iniciado (backlog).  
  - `Em Progresso`: Item em desenvolvimento ou revisão.  
  - `Feito`: Item finalizado e validado.  
  - `Bloqueado`: Item com dependências externas ou impedimentos.  

- **Time**:  
  - `Gestão`: Responsável por priorização, planejamento e acompanhamento. 
  - `Desenvolvimento`: Responsável pela implementação técnica.  

- **Outros Campos**:  
  - `Sprint`: Vincula a tarefa a uma sprint específica (ex.: "Sprint 01/2024").  
  - `Data de início`/`Data fim`: Prazos para acompanhamento.  
  - `Sub-issues progress`: Mostra o progresso de tarefas filhas (ex.: 2/5 concluídos).  

#### Milestones  
Os **Milestones (Marcos)** são utilizados para agrupar Issues e PRs relacionados a entregas específicas, como versões do produto ou metas de sprint. Eles ajudam a:  
- **Visualizar progresso**: Acompanhar o percentual concluído (ex.: `50% dos Issues fechados`).  
- **Definir prazos**: Associar uma data de entrega.  
- **Priorizar esforço**: Focar em tarefas críticas para o marco.  

**Como usar**:  
1. Crie um Milestone no GitHub vinculado a um objetivo claro.  
2. Associe Issues/PRs ao Milestone durante o planejamento.  
3. Revise o progresso nas reuniões de **Daily** ou **Planning**.  

---

#### **Tipos de Issue**  
| Tipo       | Descrição                                                                 | Exemplo de Uso                          |  
|------------|---------------------------------------------------------------------------|-----------------------------------------|  
| **TASK**   | Tarefas operacionais ou de infraestrutura (não relacionadas a features). | "Configurar ambiente de testes".        |  
| **FEATURE**| Funcionalidades novas ou melhorias no produto.                           | "Adicionar login via Google".           |  
| **BUG**    | Correções de erros ou comportamentos inesperados.                        | "Botão 'Salvar' não persiste dados".    |  

**Regras**:  
- Todo Issue deve ter:  
  - Tipo (`TASK`/`FEATURE`/`BUG`), Time e Status definidos, bem como Datas de Inícios e Fim.
  - Associar Sprints e Milestones aos issues também é obrigatório.
  - Descrição clara com critérios de aceite (se aplicável).  
  
:::warning Issues do tipo `FEATURE` devem ser vinculados a um PR com revisão aprovada.  
:::

## Método de Entrega das Tarefas

As entregas serão feitas exclusivamente via **Pull Requests (PRs)**, com as seguintes regras:
1. **Branchs**: Nomeadas conforme o tipo (ex.: `feat/nome-da-feature`, `fix/nome-do-bug`).  
2. **Revisões**: PRs exigem aprovação de pelo menos um responsável antes do merge.  
3. **Vinculação**: PRs devem referenciar o Issue correspondente no GitHub.  
