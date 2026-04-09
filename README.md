# NLP Bot 🤖
Discord bot with artificial intelligence that answers questions and fetches technology news in real time.

## Features
- Answers questions on any topic using AI (LLaMA 3.3)
- Fetches and analyzes the latest technology news
- Per-user conversation memory
- Simple and intuitive commands

## Commands

| Command | Description |
|---|---|
| `!ask <question>` | Ask anything |
| `!news` | Latest technology news |
| `!reset` | Clear conversation history |
| `!help` | Show all commands |

## Technologies used
- Python
- discord.py
- Groq API (LLaMA 3.3)
- NewsAPI
- Railway (deploy)

## Local Installation

1. Clone the repository
```bash
   git clone https://github.com/LucaASchiavi/Bot-NPL.git
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file with the following variables
```
   DISCORD_TOKEN=your_token
   GROQ_API_KEY=your_key
   NEWS_API_KEY=your_key
```
4. Run the bot
```bash
   python bot.py
```

--------------------------------------------------------

# Bot NPL 🤖

Bot de Discord con inteligencia artificial que responde preguntas
y trae noticias de tecnología en tiempo real.

## Funcionalidades

- Responde preguntas sobre cualquier tema usando IA (LLaMA 3.3)
- Trae y analiza las últimas noticias de tecnología
- Memoria de conversación por usuario
- Comandos simples e intuitivos

## Comandos

| Comando | Descripción |
|---|---|
| `!ask <pregunta>` | Hacé cualquier pregunta |
| `!noticias` | Últimas noticias de tecnología |
| `!reset` | Borrá el historial de conversación |
| `!ayuda` | Mostrá todos los comandos |

## Tecnologías usadas

- Python
- discord.py
- Groq API (LLaMA 3.3)
- NewsAPI
- Railway (deploy)

## Instalación local

1. Clonar el repositorio
```bash
   git clone https://github.com/LucaASchiavi/Bot-NPL.git
```

2. Instalar dependencias
```bash
   pip install -r requirements.txt
```

3. Crear un archivo `.env` con las siguientes variables
```
   DISCORD_TOKEN=tu_token
   GROQ_API_KEY=tu_key
   NEWS_API_KEY=tu_key
```

4. Correr el bot
```bash
   python bot.py
```
