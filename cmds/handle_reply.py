async def handle_reply(bot, message):

    if not message.reply_to_message:
        return

    mid = message.reply_to_message.id

    from commands.scl import cache

    if mid not in cache:
        return

    try:
        index = int(message.text) - 1
        song = cache[mid][index]
    except:
        return await message.reply("❌ Sai số")

    await message.reply("⏬ Đang gửi nhạc...")

    await bot.send_audio(
        message.chat.id,
        song["webpage_url"],
        title=song["title"]
    )
