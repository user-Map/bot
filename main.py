import os
import time
import asyncio
import importlib

from aiogram import Bot, Dispatcher, types

# 🔐 lấy token từ Railway Variables
TOKEN = os.environ.get("BOT_TOKEN")

PREFIX = ".."

bot = Bot(TOKEN)
dp = Dispatcher()

commands = {}
start_time = time.time()


# 🔥 load toàn bộ lệnh trong thư mục cmds
def load_commands():
    commands.clear()
    for file in os.listdir("cmds"):
        if file.endswith(".py"):
            name = file[:-3]
            module = importlib.import_module(f"cmds.{name}")
            commands[name] = module


load_commands()


@dp.message()
async def handle(message: types.Message):

    if not message.text:
        return

    if not message.text.startswith(PREFIX):
        return

    args = message.text[len(PREFIX):].split()
    cmd = args[0].lower()

    # ⭐ reload bot
    if cmd == "reload":
        load_commands()
        return await message.reply("♻️ Reload OK")

    # ⭐ uptime
    if cmd == "uptime":
        up = int(time.time() - start_time)
        return await message.reply(f"⏱ Uptime: {up}s")

    # ⭐ gọi lệnh trong cmds
    if cmd in commands:
        try:
            await commands[cmd].run(bot, message, args)
        except Exception as e:
            await message.reply(f"❌ Error: {e}")


async def main():
    print("🔥 BOT USERMAP RUNNING")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
