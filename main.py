# main.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        canal = discord.utils.get(member.guild.text_channels, name="❰🔔❱▸alertas")
        if canal:
            await canal.send(f"🔊 {member.display_name} se ha unido a {after.channel.name}")

import os
from keep_alive import keep_alive

keep_alive()
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
