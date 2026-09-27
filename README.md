# 💻 DevGuide - Mentor de Estudos Inteligente

> Agente de IA Generativa que orienta a escolha de trilhas de aprendizagem e rotinas de estudo em tecnologia de forma simples e personalizada, usando os dados e objetivos reais do estudante como base prática.

## 💡 O Que é o DevGuide?

O DevGuide é um mentor virtual de tecnologia que **orienta e educa**, não sobrecarrega. Ele explica conteúdos programáticos, pré-requisitos e planeamento de rotinas de estudo com base no tempo semanal disponível e no histórico do estudante, combatendo a paralisia por excesso de informação.

**O que o DevGuide faz:**
- ✅ Explica requisitos e conteúdos das trilhas de tecnologia de forma simples
- ✅ Usa o perfil e a disponibilidade do estudante como base prática
- ✅ Responde a dúvidas sobre ferramentas e linguagens cadastradas no catálogo
- ✅ Analisa o progresso recente e recomenda o próximo passo de estudo

**O que o DevGuide NÃO faz:**
- ❌ Não inventa cursos, módulos ou certificados ausentes do catálogo
- ❌ Não sobrecarrega iniciantes com jargões técnicos sem explicação
- ❌ Não atua em temas alheios ao contexto de estudos e tecnologia

## 🏗️ Arquitetura

```mermaid
flowchart TD
    A[Utilizador] --> B[Streamlit]
    B --> C[Ollama - LLM Local]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Resposta Educativa]


## Estrutura do projeto

├── data/                          # Base de conhecimento
│   ├── perfil_estudante.json      # Perfil, objetivos e disponibilidade do aluno
│   ├── progresso_estudos.csv      # Módulos e exercícios já concluídos
│   ├── historico_duvidas.csv      # Interações e dúvidas técnicas anteriores
│   └── trilhas_cursos.json        # Catálogo oficial de cursos e pré-requisitos
│
├── docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md  # Caso de uso e persona
│   ├── 02-base-conhecimento.md    # Estratégia de dados
│   ├── 03-prompts.md              # System prompt e exemplos
│   ├── 04-metricas.md             # Avaliação de qualidade
│   └── 05-pitch.md                # Apresentação do projeto
│
└── src/
    └── app.py                     # Aplicação Streamlit    


## Como executar

```bash
    # Descarregar em: ollama.com
    ollama pull llama3
    ollama serve

```

```b
    pip install streamlit pandas requests
```

```bash
    streamlit run src/app.py
```

🎯 Exemplos de Uso
Pergunta: "Tenho 8 horas livres por semana e quero começar do zero. O que devo estudar?"

DevGuide: "Com base na sua disponibilidade de 8 horas semanais e foco inicial, a trilha recomendada é Fundamentos de Lógica e Python. Ela exige cerca de 5 horas por semana, permitindo que aprenda a sintaxe básica e resolva exercícios sem sobrecarga. Quer que eu apresente os tópicos da primeira semana ou prefere ver como configurar o VS Code?"

Pergunta: "Vocês têm um curso avançado de Rust para microsserviços?"

DevGuide: "No momento, a nossa base não conta com uma trilha específica de Rust. Na área de backend e infraestrutura, temos disponíveis Construção de APIs REST com FastAPI e Python e Arquitetura e Microsserviços em Nuvem. Gostaria de conhecer os pré-requisitos de alguma destas opções?"

Toda a documentação técnica, estratégias de prompt e casos de teste estão disponíveis na pasta docs/.