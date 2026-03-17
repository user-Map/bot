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
    for root, dirs, files in os.walk("cmds"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                module_name = path.replace("/", ".").replace("\\", ".")[:-3]
                module = importlib.import_module(module_name)
                cmd_name = file[:-3]
                commands[cmd_name] = module

load_cmds()

@dp.message()
async def handle_msg(message: types.Message):
    text = message.text
    if not text:
        return

    if text.startswith(PREFIX):
        args = text[len(PREFIX):].split()
        cmd = args[0]

        if cmd in commands:
            try:
                await commands[cmd].run(bot, message, args)
            except:
                await message.reply("⚠️ lỗi lệnh")

async def main():
    print("🤖 TELE BOT FULL RUNNING")
    await dp.start_polling(bot)

asyncio.run(main())
