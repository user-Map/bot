import os
import importlib
import time
from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "8603942729:AAGE1RaT8oXoVhWCXhKhp5fbAdQVKHqOIL4"
PREFIX = ".."

bot = Bot(TOKEN)
dp = Dispatcher()

commands = {}
start_time = time.time()

# ===== LOAD COMMAND =====
def load_commands():
    commands.clear()
    for file in os.listdir("cmds"):
        if file.endswith(".py"):
            name = file[:-3]
            module = importlib.import_module(f"cmds.{name}")
            commands[name] = module

load_commands()

# ===== MESSAGE =====
@dp.message()
async def handle(message: types.Message):

    text = message.text
    if not text:
        return

    if not text.startswith(PREFIX):
        return

    args = text[len(PREFIX):].split()
    cmd = args[0]

    # reload
    if cmd == "reload":
        load_commands()
        return await message.reply("♻️ Reload OK")

    # uptime
    if cmd == "uptime":
        up = int(time.time() - start_time)
        return await message.reply(f"⏱ Uptime: {up}s")

    if cmd in commands:
        await commands[cmd].run(bot, message, args)

# ===== START =====
async def main():
    print("🔥 BOT ULTRA RUNNING")
    await dp.start_polling(bot)

asyncio.run(main())
