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
start_time = time.time()

# ===== LOAD COMMAND =====

def load_cmds():
    commands.clear()
    for root, dirs, files in os.walk("cmds"):
        for file in files:
            if file.endswith(".py"):
                module = importlib.import_module(
                    os.path.join(root,file).replace("/",".")[:-3]
                )
                commands[file[:-3]] = module

load_cmds()

# ===== DB RAM =====
db = {}

# ===== WELCOME =====
@dp.message(lambda m: m.new_chat_members)
async def welcome(message: types.Message):
    for u in message.new_chat_members:
        await message.reply(f"👋 Welcome {u.first_name}")

# ===== GOODBYE =====
@dp.message(lambda m: m.left_chat_member)
async def bye(message: types.Message):
    await message.reply("😢 Thành viên đã rời nhóm")

# ===== MESSAGE =====
@dp.message()
async def handle(message: types.Message):
    try:
        text = message.text
        uid = str(message.from_user.id)

        # ===== SPAM SMART =====
        now = time.time()
        spam.setdefault(uid, []).append(now)
        spam[uid] = [t for t in spam[uid] if now - t < 4]

        if len(spam[uid]) > 7:
            try:
                await bot.restrict_chat_member(
                    message.chat.id,
                    message.from_user.id,
                    permissions=types.ChatPermissions(
                        can_send_messages=False
                    ),
                    until_date=int(time.time()) + 90
                )
                await message.reply("🤬 Spam → mute 90s")
            except:
                pass
            return

        # ===== DB CHAT =====
        db[uid] = db.get(uid, 0) + 1

        # ===== COMMAND =====
        if text and text.startswith(PREFIX):
            args = text[len(PREFIX):].split()
            cmd = args[0]

            if cmd == "reload":
                load_cmds()
                return await message.reply("♻️ reload xong")

            if cmd == "uptime":
                up = int(time.time() - start_time)
                return await message.reply(f"⏱ uptime: {up}s")

            if cmd == "top":
                top = sorted(db.items(), key=lambda x: x[1], reverse=True)[:10]
                msg = "🏆 BXH CHAT\n\n"
                i = 1
                for u,c in top:
                    msg += f"{i}. {u} → {c}\n"
                    i += 1
                return await message.reply(msg)

            if cmd in commands:
                await commands[cmd].run(bot, message, args)

    except Exception as e:
        print("ERROR:", e)

# ===== START =====
async def main():
    print("🔥 ULTRA TELE BOT RUNNING")
    await dp.start_polling(bot)

asyncio.run(main())
