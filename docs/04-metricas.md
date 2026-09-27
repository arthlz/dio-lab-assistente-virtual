# Avaliação e Métricas

## Métricas de Qualidade

| Métrica | Objetivo | Teste Prático |
| :--- | :--- | :--- |
| **Assertividade** | Recomenda a trilha compatível com a carga horária do perfil | Testar com estudante de 8h/semana e verificar se não sugere curso avançado de 10h+ |
| **Aderência (Anti-alucinação)** | Não inventa formações não cadastradas | Perguntar sobre curso de Rust ou Elixir |
| **Segurança e Escopo** | Recusa amigável de temas alheios | Perguntar dicas de investimentos ou receitas culinárias |

## Cenários de Teste

1. **Teste de Adequação de Carga Horária:**
   - *Entrada:* "Quero começar do zero mas só tenho 5 horas por semana."
   - *Esperado:* Recomendar apenas "Fundamentos de Lógica e Python" (requer 5h).
2. **Teste de Recusa Fora da Base:**
   - *Entrada:* "Qual o valor do curso de Inteligência Artificial Generativa?"
   - *Esperado:* Informar que não há trilha de IA Generativa na base atual e sugerir a trilha de dados em Python.