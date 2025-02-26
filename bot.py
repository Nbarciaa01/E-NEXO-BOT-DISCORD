import discord
import random
import os
from discord.ext import commands

# Lista de mapas de Valorant
mapas = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture", "Lotus", "Pearl", "Abyss"]

# Configura el bot con los intents necesarios
intents = discord.Intents.default()
intents.message_content = True  # Habilita el intent para leer el contenido de los mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user.name}")

# Comando !play
@bot.command(name="play")
async def play(ctx, equipo1: str, equipo2: str):
    # Selecciona un mapa aleatorio
    mapa_elegido = random.choice(mapas)

    # Asigna los lados aleatoriamente sin importar el orden de los equipos
    lados = ["Atacante", "Defensor"]
    random.shuffle(lados)  # Mezcla los lados
    asignaciones = {equipo1: lados[0], equipo2: lados[1]}  # Asigna los lados aleatoriamente

    # Mensaje de respuesta
    mensaje = (
        f"**Partida generada:**\n"
        f"🔹 **Mapa:** {mapa_elegido}\n"
        f"🔹 **{equipo1}:** {asignaciones[equipo1]}\n"
        f"🔹 **{equipo2}:** {asignaciones[equipo2]}"
    )

    await ctx.send(mensaje)

# Inicia el bot
bot.run(os.getenv("DISCORD_TOKEN"))
