import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama-3"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_estudante.json', encoding='utf-8'))
progresso = pd.read_csv('./data/progresso_estudos.csv')
historico = pd.read_csv('./data/historico_duvidas.csv')
trilhas = json.load(open('./data/trilhas_cursos.json', encoding='utf-8'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
PERFIL DO ESTUDANTE:
- Nome: {perfil['nome']}, {perfil['idade']} anos
- Transição de carreira: {perfil['transicao_carreira']} (Profissão atual: {perfil['profissao_atual']})
- Nível: {perfil['nivel_atual']} | Horas disponíveis/semana: {perfil['horas_disponiveis_semana']}h
- Objetivo Principal: {perfil['objetivo_principal']}
- Preferência de Aprendizado: {perfil['preferencia_aprendizado']}

PROGRESSO DE ESTUDOS RECENTE:
{progresso.to_string(index=False)}

HISTÓRICO DE DÚVIDAS ANTERIORES:
{historico.to_string(index=False)}

CATÁLOGO DE TRILHAS DISPONÍVEIS:
{json.dumps(trilhas, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o DevGuide, um mentor virtual focado em orientar iniciantes em tecnologia.

OBJETIVO:
Ajudar o estudante a escolher trilhas e organizar rotinas de estudo com base no seu nível, disponibilidade e metas.

REGRAS:
- Use EXCLUSIVAMENTE as trilhas e informações presentes no catálogo fornecido;
- NUNCA invente formações, módulos ou certificados ausentes da base;
- Se perguntarem sobre assuntos fora da área de estudos/TI ou sobre tecnologias ausentes do catálogo, admita com clareza e ofereça uma alternativa cadastrada;
- Responda de forma sucinta e didática (máximo 3 parágrafos);
- Finalize sempre com uma pergunta ou sugestão de próximo passo prático.
"""

def perguntar(msg):
    prompt_completo = f"""
    {SYSTEM_PROMPT}

    CONTEXTO ATUAL:
    {contexto}

    Pergunta do estudante: {msg}
    """
    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt_completo, "stream": False})
        return r.json().get('response', 'Sem resposta do modelo.')
    except Exception as e:
        return f"Erro ao conectar com Ollama: {str(e)}"

# INTERFACE STREAMLIT
st.set_page_config(page_title="DevGuide - Mentor de Estudos", page_icon="💻")
st.title("💻 DevGuide: Mentor Virtual de Estudos em TI")

if pergunta := st.chat_input("Dúvida sobre trilhas, tecnologias ou rotina de estudos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Analisando seu perfil e catálogo..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)