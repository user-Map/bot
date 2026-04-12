import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="..", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def setup_hook():
    for file in os.listdir("./cmds"):
        if file.endswith(".py"):
            await bot.load_extension(f"cmds.{file[:-3]}")

token = os.getenv("TOKEN")

if token:
    bot.run(token)
else:
    print("TOKEN MISSING")
