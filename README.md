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
