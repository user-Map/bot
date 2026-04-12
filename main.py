import discord
from discord.ext import commands
import os
import time
import importlib
import json
import os

TOKEN = os.getenv("TOKEN")
PREFIX = ".."

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

commands_map = {}
start_time = time.time()


# tạo file json nếu chưa có
if not os.path.exists("group.json"):
    with open("group.json", "w") as f:
        f.write('{"warn":{},"antilink":false,"antibot":false}')

if not os.path.exists("admins.json"):
    with open("admins.json", "w") as f:
        f.write('{"owner":[],"admin":[]}')


# load commands
def load_commands():
    commands_map.clear()
    for file in os.listdir("cmds"):
        if file.endswith(".py"):
            name = file[:-3]
            module = importlib.import_module(f"cmds.{name}")
            importlib.reload(module)
            commands_map[name] = module

load_commands()


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.content:
        return

    # ANTI LINK
    try:
        with open("group.json") as f:
            g = json.load(f)

        if g.get("antilink"):
            if "http" in message.content or "t.me" in message.content:
                await message.delete()
                return
    except:
        pass

    # PREFIX
    if not message.content.startswith(PREFIX):
        return

    args = message.content[len(PREFIX):].split()
    cmd = args[0].lower()

    if cmd == "reload":
        load_commands()
        return await message.reply("♻️ Reload OK")

    if cmd == "uptime":
        up = int(time.time() - start_time)
        return await message.reply(f"⏱ Uptime: {up}s")

    if cmd in commands_map:
        try:
            await commands_map[cmd].run(bot, message, args)
        except Exception as e:
            await message.reply(f"❌ Error: {e}")

    await bot.process_commands(message)


# ANTI BOT JOIN (Discord version)
@bot.event
async def on_member_join(member):
    try:
        with open("group.json") as f:
            g = json.load(f)

        if g.get("antibot") and member.bot:
            await member.ban(reason="Anti bot system")
    except:
        pass


@bot.event
async def on_ready():
    print("🔥 DISCORD BOT RUNNING")


bot.run(TOKEN)
