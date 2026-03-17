import os
import asyncio
import importlib
from aiogram import Bot, Dispatcher, types

TOKEN = "8603942729:AAGE1RaT8oXoVhWCXhKhp5fbAdQVKHqOIL4"
PREFIX = ".."

bot = Bot(TOKEN)
dp = Dispatcher()

commands = {}

def load_cmds():
    path = "cmds"
    if not os.path.exists(path):
        os.mkdir(path)

    for file in os.listdir(path):
        if file.endswith(".py"):
            name = file[:-3]
            module = importlib.import_module(f"cmds.{name}")
            commands[name] = module

load_cmds()

@dp.message()
async def handle_msg(message: types.Message):
    text = message.text
    if not text:
        return

    if text.startswith(PREFIX):
        cmd = text[len(PREFIX):].split()[0]

        if cmd in commands:
            await commands[cmd].run(bot, message)

async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)

asyncio.run(main())
