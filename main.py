import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="..", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def load_commands():
    for file in os.listdir("./cmds"):
        if file.endswith(".py"):
            await bot.load_extension(f"cmds.{file[:-3]}")

@bot.event
async def setup_hook():
    await load_commands()

bot.run(TOKEN)
