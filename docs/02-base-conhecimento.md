# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Papel no DevGuide |
| :--- | :--- | :--- |
| `perfil_estudante.json` | JSON | Nível atual, objetivo de carreira e teto de horas semanais disponíveis. |
| `trilhas_cursos.json` | JSON | Catálogo fechado de cursos (pré-requisitos, tecnologias e duração). |
| `historico_duvidas.csv` | CSV | Registro de dúvidas conceituais prévias já resolvidas pelo suporte/comunidade. |
| `progresso_estudos.csv` | CSV | Módulos e exercícios já concluídos ou em andamento pelo estudante. |

## Estratégia de Integração
- **Context Stuffing:** Dados sintetizados e concatenados diretamente no prompt de sistema via script Python em `src/app.py`.
- **Prevenção de Alucinação:** Restrição explícita de catálogo para evitar sugestão de ferramentas inexistentes na base.