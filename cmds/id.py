async def run(bot, message, args):

    uid = message.from_user.id
    await message.reply(f"🆔 ID của bạn: {uid}")
