import time

async def run(bot, message, args):

    # ⭐ lấy user (tag hoặc bản thân)
    user = message.mentions[0] if message.mentions else message.from_user

    name = user.first_name
    uid = user.id
    username = user.username if user.username else "Không có"
    isbot = "🤖 Bot" if user.is_bot else "👤 Người dùng"

    # ⭐ link
    if username != "Không có":
        link = f"https://t.me/{username}"
    else:
        link = f"tg://user?id={uid}"

    text = f"""
╔═══ INFO USER ═══╗
👤 Tên: {name}
🆔 ID: {uid}
📛 Username: {username}
📌 Loại: {isbot}
🔗 Link: {link}
🕒 Time: {time.strftime('%H:%M:%S')}
╚═════════════════╝
"""

    try:
        photos = await bot.get_profile_photos(uid, limit=1)
        if photos.total_count > 0:
            await bot.send_photo(
                message.chat.id,
                photos.photos[0][-1].file_id,
                caption=text
            )
        else:
            await message.reply(text)
    except:
        await message.reply(text)
