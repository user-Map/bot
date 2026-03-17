import json
import os

FILE = "admins.json"

async def run(bot, message, args):

    if not os.path.exists(FILE):
        return await message.reply("❌ Chưa có admin")

    data = json.load(open(FILE))

    text = "👑 OWNER:\n"
    for i in data["owner"]:
        text += f"• {i}\n"

    text += "\n⚙️ ADMIN:\n"
    for i in data["admin"]:
        text += f"• {i}\n"

    await message.reply(text)
