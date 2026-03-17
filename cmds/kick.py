async def run(bot, message, args):

    if message.chat.type == "private":
        return await message.reply("❌ chỉ dùng trong nhóm")

    if not message.reply_to_message:
        return await message.reply("⚡ reply người cần kick")

    try:
        user = message.reply_to_message.from_user.id

        await bot.kick_chat_member(message.chat.id, user)

        await message.reply("👢 đã kick")

    except:
        await message.reply("❌ bot cần quyền admin")
