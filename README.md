# AI Code Assistant

Aplicación web desarrollada con Python y Streamlit que utiliza un modelo de inteligencia artificial local mediante Ollama para ayudar en tareas de programación.
## Funcionalidades

- Generar código.
- Explicar código.
- Revisar código.
- Mejorar código.
- Seleccionar distintos lenguajes de programación.
- Ejecutar el modelo de IA de forma local mediante Ollama.
## Tecnologías utilizadas

- Python
- Streamlit
- Ollama
- Llama 3.2
- Prompt Engineering
## Cómo funciona

1. El usuario selecciona una acción.
2. Selecciona el lenguaje de programación.
3. Introduce una descripción o pega código.
4. La aplicación construye un prompt estructurado.
5. El prompt se envía al modelo local Llama 3.2 mediante Ollama.
6. La respuesta se muestra en la interfaz de Streamlit.
## Ejecución

1. Crear y activar un entorno virtual.

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Tener Ollama instalado y descargar el modelo Llama 3.2:

```bash
ollama pull llama3.2:3b
```

4. Ejecutar la aplicación:

```bash
streamlit run app.py
```
## Limitaciones

- El modelo se ejecuta de forma local, por lo que el rendimiento depende del equipo.
- La calidad de las respuestas puede variar según la complejidad del código.
- No ejecuta ni valida automáticamente el código generado.
- Actualmente utiliza un único modelo local.
## Mejoras futuras

- Permitir elegir entre varios modelos de IA.
- Añadir soporte para más lenguajes de programación.
- Mostrar el código generado con resaltado de sintaxis.
- Añadir historial de consultas.
- Permitir comparar la respuesta de varios modelos.
- Añadir opción de usar una API externa además del modelo local.
## Arquitectura

El flujo principal de la aplicación es:

Usuario → Streamlit → Prompt estructurado → Ollama → Llama 3.2 → Respuesta

La interfaz recoge la acción seleccionada, el lenguaje y el contenido introducido por el usuario. A partir de estos datos se construye un prompt específico que se envía al modelo local mediante Ollama.