import aiohttp

cache = {}

async def run(bot, message, args):
    query = " ".join(args[1:])

    if not query:
        return await message.reply("❌ Dùng: ..nhac tên bài")

    msg = await message.reply("🔎 Đang tìm nhạc...")

    url = f"https://api.popcat.xyz/lyrics?song={query}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()

    if "title" not in data:
        return await msg.edit_text("❌ Không tìm thấy")

    title = data["title"]
    artist = data["artist"]
    thumb = data["image"]

    text = f"""
🎧 {title}
👤 {artist}

📥 Gửi số 1 để tải nhạc
"""

    cache[message.from_user.id] = query

    await bot.send_photo(message.chat.id, thumb, caption=text)

    await msg.delete()


async def choose(bot, message):
    if message.from_user.id not in cache:
        return

    if message.text != "1":
        return

    query = cache[message.from_user.id]

    await bot.send_message(
        message.chat.id,
        f"🎧 Đây là link tải MP3:\nhttps://api.vevioz.com/api/button/mp3/{query}"
    )
