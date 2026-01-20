import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(os.getenv("ODEyMzYxODY1MjkxNjI4NTQ1.GJJMzd.L9KxpuSKD2bswBTYjwztEiR2ePJgz2_8HkroRw"))
