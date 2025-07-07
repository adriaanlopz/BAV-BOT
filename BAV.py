# main.py
import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        canal = discord.utils.get(member.guild.text_channels, name="❰‼️❱▸alertas")
        if canal:
            await canal.send(f"🔊  **{member.display_name}** se ha conectado al canal de voz  **{after.channel.name}**.")

async def main():
    try:
        await bot.start(os.getenv("DISCORD_BOT_TOKEN"))
    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())
