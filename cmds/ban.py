async def run(bot, message, args):

    if message.chat.type == "private":
        return await message.reply("❌ chỉ dùng nhóm")

    if not message.reply_to_message:
        return await message.reply("⚡ reply người cần ban")

    try:
        uid = message.reply_to_message.from_user.id
        await bot.ban_chat_member(message.chat.id, uid)
        await message.reply("🚫 đã ban")
    except:
        await message.reply("❌ bot cần quyền admin")
