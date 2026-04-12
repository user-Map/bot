import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="..", intents=intents)

token = os.getenv("TOKEN")

if not token:
    print("TOKEN MISSING")
else:
    bot.run(token)
