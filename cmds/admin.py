async def run(bot, message, args):

    if message.chat.type == "private":
        return await message.reply("❌ dùng trong nhóm")

    text = """
👑 ADMIN MENU

⚡ ..kick (reply)
⚡ ..ban (reply)
⚡ ..reload
⚡ ..uptime
⚡ ..top
"""

    await message.reply(text)
