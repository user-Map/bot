async def run(bot, message, args):

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif message.mentions:
        user = message.mentions[0]
    else:
        user = message.from_user

    try:
        photos = await bot.get_profile_photos(user.id, limit=1)

        if photos.total_count == 0:
            return await message.reply("❌ Người này không có avatar")

        await bot.send_photo(
            message.chat.id,
            photos.photos[0][-1].file_id,
            caption=f"🖼 Avatar của {user.first_name}"
        )

    except Exception as e:
        await message.reply(f"❌ Lỗi: {e}")
