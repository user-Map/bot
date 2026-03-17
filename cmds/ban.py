import json

async def run(bot, message, args):

    data = json.load(open("admins.json"))
    uid = message.from_user.id

    if uid not in data["owner"] and uid not in data["admin"]:
        return await message.reply("❌ Không có quyền")

    if not message.reply_to_message:
        return await message.reply("⚠️ Reply người cần ban")

    user = message.reply_to_message.from_user.id

    await bot.ban_chat_member(message.chat.id, user)

    await message.reply("🚫 Đã ban")
