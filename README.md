# Pibble: Librería Multimodal de Audio, Gramatica e IA

## Integrantes

- Fausto Jafeth Vilches Mendieta
- Andy Gildo Vallejos Bascope
- Galilea Alissandre Hinojosa Cusicanqui

---

# Estado del proyecto

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tests](https://img.shields.io/badge/Tests-pytest-green)
![IA](https://img.shields.io/badge/AI-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

# Estructura del proyecto

├── 📁 src
│ ├── 🐍 init.py
│ ├── 🐍 audio.py
│ ├── 🐍 gramatica.py
│ └── 🐍 ia.py
├── 📁 tests
│ ├── 🐍 test_audio.py
│ ├── 🐍 test_gramatica.py
│ └── 🐍 test_ia.py
├── ⚙️ .env.example
├── ⚙️ .gitignore
├── 📝 README.md
├── 📝 README2.md
├── 🐍 app.py
├── ⚙️ pytest.ini
└── 📄 requirements.txt

---

# 🎯 Descripción general

Este proyecto es una **librería modular en Python** que integra procesamiento de:

- Audio (voz a texto y texto a voz)
- Texto (análisis lingüístico y validación)
- Inteligencia Artificial (Google Gemini multimodal)

---

# Módulo de Audio (`src/audio.py`)

## Funcionalidades

- Detección de micrófono
- Grabación en tiempo real
- Reconocimiento de voz (Speech-to-Text)
- Síntesis de voz (Text-to-Speech)
- Exportación a MP3

## Tecnologías

- `sounddevice`
- `speech_recognition`
- `pyttsx3`
- `pydub`

---

# Módulo de Gramática (`src/gramatica.py`)

## Funcionalidades

- Limpieza y normalización de texto
- Conteo de palabras, caracteres y oraciones
- Validación gramatical básica
- Detección de emails, URLs, teléfonos y fechas
- Tokenización de texto
- Métricas de legibilidad y riqueza léxica

## Capacidades

- Expresiones regulares avanzadas
- Análisis estructural de texto
- Validación dinámica de reglas

---

# Módulo de IA (`src/ia.py`)

## Funcionalidades

- Prompts de texto
- Análisis de imágenes
- Análisis de audio
- Archivos locales o URLs
- Respuestas con Google Gemini

## Características

- Multimodal (texto + imagen + audio)
- Detección automática de MIME type
- Manejo de errores robusto

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/andy-vallejos/pibble.git
cd pibble
```

## Crear entorno virtual

```
python -m venv .venv
```

### Activar

```
.venv\Scripts\activate
```

## Instalar dependencias

```
pip install -r requirements.txt
```

## Variables de entorno

Crear archivo .env:

```
GOOGLE_API_KEY=tu_api_key_aqui
```

### Obtener API key

<https://aistudio.google.com/app/api-keys>

# Testing

Este proyecto utiliza pytest.

## Ejecutar tests

```
pytest
```

Si hay problemas de entorno:

```
python -m pytest
```
