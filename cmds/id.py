async def run(bot, message, args):

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif message.mentions:
        user = message.mentions[0]
    else:
        user = message.from_user

    await message.reply(f"🆔 ID của {user.first_name} là:\n<code>{user.id}</code>", parse_mode="HTML")
