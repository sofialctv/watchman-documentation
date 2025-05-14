---
sidebar_position: 1
title: Design Structure Matrix
---
# DSM - Design Structure Matrix

## O que é DSM?

A *Design Structure Matrix* (DSM) é uma ferramenta visual usada para representar e analisar dependências entre elementos de um sistema, como funcionalidades, módulos ou componentes. Ela é particularmente útil para:

- Compreender o acoplamento entre partes do sistema.
- Identificar oportunidades de modularização ou refatoração.
- Planejar o desenvolvimento incremental de forma mais estratégica.

No contexto de engenharia de software, a DSM ajuda times a enxergar como funcionalidades se relacionam e dependem umas das outras, promovendo decisões mais informadas sobre ordem de implementação, testes e manutenção.


## DSM do Projeto

Nosso projeto está dividido em três grandes módulos:

- **Notas Fiscais (NF)**
- **Tipos de Gastos (TG)**
- **Categorização de Gastos (CG)**

Cada módulo é composto por funcionalidades, descritas na nossa [planilha de especificações](https://docs.google.com/spreadsheets/d/1CvDfyiDCnFFN6yI4YhSiVPG6a0834HQZN-pcWr80uk8/edit?usp=sharing), onde também indicamos o grau de prioridade usando a técnica MoSCoW e explicitando a matriz de dependências. Abaixo, apresentamos nossas funcionalidades e representamos as dependências funcionais entre essas features utilizando um grafo construído com Mermaid.


### Funcionalidades do Sistema

| ID    | Feature                                                                        | Prioridade |
| ----- | ------------------------------------------------------------------------------ | ---------- |
| NF-01 | Eu, como Usuário, quero fazer upload de uma nota fiscal                        | M          |
| NF-02 | Eu, como Usuário, quero preencher os dados de uma nota fiscal manualmente      | M          |
| NF-03 | Eu, como Usuário, quero validar o conteúdo da NF antes de salvar               | M          |
| NF-04 | Eu, como Usuário, quero visualizar todas as NFs cadastradas                    | M          |
| NF-05 | Eu, como Usuário, quero visualizar os detalhes de uma NF específica            | M          |
| NF-06 | Eu, como Usuário, quero baixar uma NF em formato PDF                           | S          |
| NF-07 | Eu, como Usuário, quero excluir uma NF específica                              | S          |
| NF-08 | Eu, como Usuário, quero excluir várias NFs de uma só vez                       | C          |
| NF-09 | Eu, como Usuário, quero visualizar o histórico de exclusão de NFs              | C          |
| TG-01 | Eu, como Usuário, quero cadastrar um novo tipo de gasto                        | M          |
| TG-02 | Eu, como Usuário, quero editar um tipo de gasto existente                      | M          |
| TG-03 | Eu, como Usuário, quero excluir um tipo de gasto do sistema                    | C          |
| TG-04 | Eu, como Usuário, quero listar todos os tipos de gasto cadastrados             | S          |
| TG-05 | Eu, como Usuário, quero ver detalhes de um tipo de gasto                       | C          |
| CG-01 | Eu, como Usuário, quero atribuir manualmente uma categoria a uma NF            | M          |
| CG-02 | Eu, como Usuário, quero visualizar todas as categorizações associadas à uma NF | M          |
| CG-03 | Eu, como Usuário, quero editar a categoria de uma NF                           | S          |
| CG-04 | Eu, como Usuário, quero ver o histórico de alterações da categorização         | C          |

### Grafo de dependência

```mermaid
flowchart LR

NF01 --> NF02
NF01 --> NF03
NF02 --> NF03
NF03 --> NF04
NF03 --> NF05
NF03 --> NF06
NF01 --> NF07
NF01 --> NF08
NF07 --> NF09
NF08 --> NF09

TG01 --> TG02
TG01 --> TG03
TG01 --> TG04
TG01 --> TG05

NF01 --> CG01
TG01 --> CG01
CG01 --> CG02
CG01 --> CG03
CG03 --> CG04
