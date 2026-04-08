# Sistema de Solicitacoes Urbanas

> Atividade de Extensao Profissional (AEP) — ESOFT 5° Semestre — Turma A

Sistema de gerenciamento de demandas urbanas desenvolvido em Python, que permite a cidadaos registrarem solicitacoes junto ao municipio e a atendentes/gestores acompanharem e resolverem essas demandas com controle de prioridade e SLA.

---

## Grupo

| Integrante                  | RA           |
|-----------------------------|--------------|
| Joao Paulo Traguetta Rufino |24000674-2    |
| Heitor Ferrari              |              |
| Maria Eduarda               |              |

---

## Funcionalidades

### Area do Cidadao
- Registrar nova solicitacao (anonima ou identificada)
- Escolher categoria, prioridade e localizacao
- Acompanhar status da solicitacao via protocolo
- Visualizar prazo alvo e historico de movimentacoes

### Area do Atendente / Gestor
- Listar todas as demandas com filtros por prioridade e categoria
- Atualizar status das solicitacoes com comentario obrigatorio
- Visualizar solicitacoes atrasadas
- Exigencia de justificativa para solicitacoes fora do prazo

---

## Categorias de Solicitacao

| Categoria         | Descricao                                        |
|-------------------|--------------------------------------------------|
| Iluminacao        | Problemas com iluminacao publica                 |
| Buraco nas ruas   | Buracos ou irregularidades no pavimento          |
| Poda              | Podagem de arvores irregulares                   |
| Saude             | Duvidas ou solicitacoes relacionadas a saude     |
| Limpeza           | Limpeza e zeladoria                              |
| Outro             | Demais solicitacoes                              |

---

## Prioridades e SLA

| Prioridade | SLA (dias) | Impacto Social        |
|------------|------------|-----------------------|
| Baixa      | 15 dias    | Impacto localizado    |
| Media      | 7 dias     | Impacto moderado      |
| Alta       | 3 dias     | Impacto relevante     |
| Critica    | 1 dia      | Impacto social alto   |

---

## Fluxo de Status

```
ABERTO → TRIAGEM → EM EXECUCAO → RESOLVIDO → ENCERRADO
```

Cada transicao exige:
- Comentario obrigatorio
- Justificativa de atraso (caso o prazo SLA tenha sido ultrapassado)

---

## Estrutura do Projeto

```
AEP/
├── main.py                        # Ponto de entrada da aplicacao
├── Enums/
│   ├── cargo.py                   # Enum de cargo do usuario
│   ├── prioridade.py              # Enum de prioridade com SLA
│   ├── status.py                  # Enum de status com regras de transicao
│   ├── tipoCategoria.py           # Categorias de demanda urbana
│   └── tipoIdentificacao.py       # Anonimo ou Identificado
├── Models/
│   ├── categoria.py               # Modelo de categoria
│   ├── historico.py               # Registro de movimentacoes
│   ├── solicitacao.py             # Modelo principal da solicitacao
│   └── usuario.py                 # Modelo de usuario (cidadao/atendente)
├── Services/
│   ├── fila_atendimento.py        # Logica de fila de atendimento
│   └── servico_solicitacoes.py    # Servicos de CRUD de solicitacoes
├── UI/
│   ├── menu_atendente.py          # Interface do atendente/gestor
│   ├── menu_cidadao.py            # Interface do cidadao
│   └── terminal_ui.py             # Componentes de UI no terminal
└── Utils/
    └── protocolo.py               # Geracao de protocolo unico
```

---

## Requisitos

- Python 3.10 ou superior
- Sem dependencias externas (biblioteca padrao apenas)

---

## Como Executar

1. Clone o repositorio:

```bash
git clone <url-do-repositorio>
cd AEP-5-Bimestre---1
```

2. Execute o sistema:

```bash
python AEP/main.py
```

3. Navegue pelos menus no terminal:
   - `1` — Area do Cidadao
   - `2` — Area do Atendente/Gestor
   - `0` — Sair

---

## Conceitos Aplicados

- **Orientacao a Objetos** — Models, Services e Enums bem separados
- **Enums com comportamento** — Prioridade calcula SLA e peso; Status valida transicoes
- **Validacao de regras de negocio** — Anonimato, campos obrigatorios, fluxo de status
- **SLA e controle de prazo** — Calculo automatico de prazo alvo por prioridade
- **Historico de movimentacoes** — Rastreabilidade completa de cada solicitacao
- **Separacao de responsabilidades** — UI, Service e Model isolados

---

## Instituicao

**Unicesumar Maringá**
Curso: Engenharia de Software — ESOFT
Semestre: 5° — Turma A
