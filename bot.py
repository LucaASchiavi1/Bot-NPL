import discord
import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Configurar Groq
client_ai = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Configurar Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Diccionario que guarda el historial de cada usuario
historiales = {}

SYSTEM_PROMPT = """
Sos un asistente experto en noticias y tendencias de tecnología.
Respondés siempre en español, de forma clara y concisa (máximo 3 párrafos).
Cuando el usuario pida noticias, analizás y resumís la información que te dan.
Si te hacen preguntas generales de tecnología, respondés con tu conocimiento.
"""

def obtener_noticias(tema="technology", cantidad=5):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": tema,
        "language": "en",
        "pageSize": cantidad,
        "apiKey": os.getenv("NEWS_API_KEY")
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["status"] != "ok" or not data["articles"]:
        return None
    
    # Armar un texto con los titulares y descripciones
    resumen = ""
    for i, articulo in enumerate(data["articles"], 1):
        titulo = articulo.get("title", "Sin título")
        descripcion = articulo.get("description", "Sin descripción")
        resumen += f"{i}. {titulo}\n{descripcion}\n\n"
    
    return resumen
    

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user_id = message.author.id # ID único de cada usuario de Discord
    
    # Inicializar historial si es la primera vez que escribe este usuario
    if user_id not in historiales:
        historiales[user_id] = []
    
    if message.content.startswith("!ask"):
        pregunta = message.content[4:].strip()
        
        if not pregunta:
            await message.channel.send("Escribir algo despues de !ask.")
            
        historiales[user_id].append({
            "role": "user",
            "content": pregunta
        })
        
        respuesta = client_ai.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system","content": SYSTEM_PROMPT},
                *historiales[user_id] # Se despliega el historial
            ]
        ) 
        
        respuesta_texto = respuesta.choices[0].message.content
        
        # Agregar la respuesta del bot al historial
        historiales[user_id].append({
            "role": "assistant",
            "content": respuesta_texto
        })
        
        await message.channel.send(respuesta_texto)
        
    elif message.content.startswith("!noticias"):
        
        noticias = obtener_noticias()
        
        if not noticias:
            await message.channel.send("No pude obtener noticias en este momento.")
            return

        # Le pedimos al modelo que resuma y analice las noticias
        prompt = f"Estas son las últimas noticias de tecnología:\n\n{noticias}\nHacé un resumen breve de las más importantes y qué tendencias ves."
        
        respuesta = client_ai.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        await message.channel.send(respuesta.choices[0].message.content)
        
    # Comando: reset
    elif message.content.startswith("!reset"):
        historiales[user_id] = []
        await message.channel.send("Historial borrado.")
        
        
    # Comando: ayuda
    elif message.content.startswith("!ayuda"):
        await message.channel.send(
            "**Comandos disponibles:**\n"
            "`!ask <pregunta>` — Hacerme una pregunta\n"
            "`!noticias` — Traigo las últimas noticias de tech en tiempo real\n"
            "`!reset` — Borro el historial de la conversación\n"
            "`!ayuda` — Muestro este mensaje"
        )

client.run(os.getenv("DISCORD_TOKEN"))