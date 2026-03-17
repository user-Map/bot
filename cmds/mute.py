import json
import time
from aiogram.types import ChatPermissions

async def run(bot, message, args):

    data = json.load(open("admins.json"))
    uid = message.from_user.id

    if uid not in data["owner"] and uid not in data["admin"]:
        return await message.reply("❌ Không có quyền")

    if not message.reply_to_message:
        return await message.reply("⚠️ Reply người cần mute")

    t = 60
    if len(args) >= 2:
        t = int(args[1])

    user = message.reply_to_message.from_user.id
    until = int(time.time()) + t

    await bot.restrict_chat_member(
        message.chat.id,
        user,
        permissions=ChatPermissions(can_send_messages=False),
        until_date=until
    )

    await message.reply(f"🔇 Mute {t}s")
