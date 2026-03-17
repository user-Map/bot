async def run(bot, message, args):

    text = """
╔══════════════════╗
      👮 MANAGER
╚══════════════════╝

⚙️ BOT
┠➤ ..reload
┠➤ ..uptime

👥 GROUP
┠➤ ..kick (reply)
┠➤ ..ban (reply)
┠➤ ..mute 60 (reply)
┠➤ ..unmute
"""
    await message.reply(text)
