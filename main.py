import os
import time
import asyncio
import importlib
import json

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

TOKEN = os.environ.get("BOT_TOKEN")
PREFIX = ".."

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

commands = {}
start_time = time.time()


# tạo json nếu chưa có
if not os.path.exists("group.json"):
    open("group.json", "w").write('{"warn":{},"antilink":false,"antibot":false}')

if not os.path.exists("admins.json"):
    open("admins.json", "w").write('{"owner":[],"admin":[]}')


# load cmds
def load_commands():
    commands.clear()
    for file in os.listdir("cmds"):
        if file.endswith(".py"):
            name = file[:-3]
            module = importlib.import_module(f"cmds.{name}")
            importlib.reload(module)
            commands[name] = module

load_commands()


@dp.message()
async def handle(message: types.Message):

    if not message.text:
        return

    # anti link
    try:
        g = json.load(open("group.json"))
        if g.get("antilink"):
            if "http" in message.text or "t.me" in message.text:
                await message.delete()
                return
    except:
        pass

    # phải có prefix
    if not message.text.startswith(PREFIX):
        return

    # tách lệnh chuẩn
    text = message.text[len(PREFIX):]
    parts = text.split()

    if not parts:
        return

    cmd = parts[0].lower()
    args = parts  # ⭐ QUAN TRỌNG → giữ nguyên để tiktok dùng args[1]

    # system
    if cmd == "reload":
        load_commands()
        return await message.reply("♻️ Reload OK")

    if cmd == "uptime":
        up = int(time.time() - start_time)
        return await message.reply(f"⏱ Uptime: {up}s")

    # chạy command
    if cmd in commands:
        try:
            await commands[cmd].run(bot, message, args)
        except Exception as e:
            await message.reply(f"❌ Error: {e}")
    else:
        await message.reply("❌ Lệnh không tồn tại")


@dp.chat_member()
async def anti_bot(event: types.ChatMemberUpdated):
    try:
        g = json.load(open("group.json"))
        if g.get("antibot"):
            if event.new_chat_member.user.is_bot:
                await bot.ban_chat_member(
                    event.chat.id,
                    event.new_chat_member.user.id
                )
    except:
        pass


async def main():
    print("🔥 USERMAP BOT RUNNING")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
