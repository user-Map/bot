import os
import json
import asyncio
import importlib
from aiogram import Bot, Dispatcher, types

TOKEN = "8603942729:AAGE1RaT8oXoVhWCXhKhp5fbAdQVKHqOIL4"
PREFIX = ".."

bot = Bot(TOKEN)
dp = Dispatcher()

commands = {}

# ===== DATABASE =====

def load_db():
    try:
        with open("db.json") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open("db.json", "w") as f:
        json.dump(data, f)

# ===== LOAD COMMAND =====

def load_cmds():
    for root, dirs, files in os.walk("cmds"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                module_name = path.replace("/", ".").replace("\\", ".")[:-3]
                module = importlib.import_module(module_name)
                cmd = file[:-3]
                commands[cmd] = module

load_cmds()

# ===== EVENT MESSAGE =====

@dp.message()
async def handle_msg(message: types.Message):
    try:
        text = message.text

        # ===== ĐẾM TIN NHẮN =====
        db = load_db()
        uid = str(message.from_user.id)

        if uid not in db:
            db[uid] = 0

        db[uid] += 1
        save_db(db)

        # ===== COMMAND =====
        if text and text.startswith(PREFIX):
            args = text[len(PREFIX):].split()
            cmd = args[0]

            if cmd in commands:
                await commands[cmd].run(bot, message, args)

    except Exception as e:
        print("ERROR:", e)

# ===== START BOT =====

async def main():
    print("🤖 TELE BOT VIP RUNNING")
    await dp.start_polling(bot)

asyncio.run(main())
