async def run(bot, message, args):

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    await message.reply(f"🆔 ID: {user.id}")
