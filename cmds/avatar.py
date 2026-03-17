async def run(bot, message, args):

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    uid = user.id
    name = user.first_name

    link = f"tg://user?id={uid}"

    text = f"""
🖼 Avatar {name}

👉 Bấm link dưới để xem:
{link}
"""

    await message.reply(text)
