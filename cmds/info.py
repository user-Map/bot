import time

async def run(bot, message, args):

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    name = user.first_name
    uid = user.id
    username = getattr(user, "username", "Không có")

    text = f"""
🔥 USER INFO 🔥
━━━━━━━━━━
👤 Name: {name}
🆔 ID: {uid}
📛 Username: {username}
🕒 Time: {time.strftime('%H:%M:%S')}
"""

    await message.reply(text)
