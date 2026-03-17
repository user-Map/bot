import os
import json
import asyncio
import importlib
import time
from aiogram import Bot, Dispatcher, types

TOKEN = "8603942729:AAGE1RaT8oXoVhWCXhKhp5fbAdQVKHqOIL4"
PREFIX = ".."

bot = Bot(TOKEN)
dp = Dispatcher()

commands = {}
spam = {}

# ===== DATABASE =====

def load_db():
    try:
        with open("db.json") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open("db.json","w") as f:
        json.dump(data,f)

# ===== LOAD COMMAND =====

def load_cmds():
    for root, dirs, files in os.walk("cmds"):
        for file in files:
            if file.endswith(".py"):
                module = importlib.import_module(
                    os.path.join(root,file).replace("/",".")[:-3]
                )
                commands[file[:-3]] = module

load_cmds()

# ===== WELCOME =====

@dp.message(lambda m: m.new_chat_members)
async def welcome(message: types.Message):
    for user in message.new_chat_members:
        await message.reply(f"👋 chào mừng {user.first_name} vào nhóm")

# ===== MESSAGE =====

@dp.message()
async def handle(message: types.Message):
    try:
        text = message.text
        uid = str(message.from_user.id)

        # ===== SPAM =====
        now = time.time()
        if uid not in spam:
            spam[uid] = []

        spam[uid].append(now)
        spam[uid] = [t for t in spam[uid] if now - t < 5]

        if len(spam[uid]) > 6:
            try:
                await bot.restrict_chat_member(
                    message.chat.id,
                    message.from_user.id,
                    permissions=types.ChatPermissions(can_send_messages=False),
                    until_date=int(time.time()) + 60
                )
                await message.reply("🤬 spam nhiều quá → mute 60s")
            except:
                pass
            return

        # ===== DB CHAT =====
        db = load_db()
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

# ===== START =====

async def main():
    print("🔥 BOT TELE PRO RUNNING")
    await dp.start_polling(bot)

asyncio.run(main())
