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
