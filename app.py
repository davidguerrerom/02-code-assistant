import os
import streamlit as st
import ollama
st.set_page_config(
    page_title="AI Code Assistant",
    page_icon="💻",
    layout="centered"
)
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
def build_prompt(action, language, user_input):

    instructions = {
        "Generar código": "Genera código claro, correcto y bien estructurado.",
        "Explicar código": "Explica el código paso a paso de forma sencilla.",
        "Revisar código": "Revisa el código, detecta errores y explica los problemas encontrados.",
        "Mejorar código": "Mejora el código manteniendo su funcionalidad y explica los cambios realizados."
    }

    prompt = f"""
Eres un asistente experto en programación.

ACCIÓN:
{action}

LENGUAJE:
{language}

INSTRUCCIÓN:
{instructions[action]}

CONTENIDO DEL USUARIO:
{user_input}
"""

    return prompt

st.title("AI Code Assistant")
st.write("Asistente de programación con Inteligencia Artificial")
if api_key:
    st.success("API key cargada correctamente.")
else:
    st.error("No se ha encontrado la API key.")
action = st.selectbox(
    "Selecciona una acción:",
    [
        "Generar código",
        "Explicar código",
        "Revisar código",
        "Mejorar código"
    ]
)
language = st.selectbox(
    "Selecciona un lenguaje:",
    [
        "Python",
        "Java",
        "Kotlin",
        "JavaScript",
        "HTML/CSS"
    ]
)
user_input = st.text_area(
    "Escribe aquí tu descripción o pega tu código:",
    height=250
)
if st.button("Ejecutar"):
    if not user_input.strip():
        st.warning("Escribe una descripción o pega un código antes de continuar.")
    else:
        prompt = build_prompt(action, language, user_input)

        with st.spinner("Procesando con IA..."):
            response = ollama.generate(
                model="llama3.2:3b",
                prompt=prompt
            )

        st.write(response.response)