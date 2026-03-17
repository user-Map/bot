import os

async def run(bot, message, args):

    text = "📜 MENU BOT TELE\n\n"

    total = 0

    for root, dirs, files in os.walk("cmds"):
        for file in files:
            if file.endswith(".py"):
                cmd = file[:-3]
                text += f"⚡ ..{cmd}\n"
                total += 1

    text += f"\n🔥 Tổng lệnh: {total}"

    await message.reply(text)
