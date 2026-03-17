ADMIN_ID = [7126997268]  

async def run(bot, message, args):

    user_id = message.from_user.id

    if user_id not in ADMIN_ID:
        return await message.reply("❌ Mày Đéo phải admin nên Đéo mở được Manager ")

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
