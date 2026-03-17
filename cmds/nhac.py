import aiohttp

API_KEY = "db2d0600admshc5c042c9e80276ep18d4dajsn87984be2b676"

async def run(bot, message, args):
    query = " ".join(args[1:])

    if not query:
        return await message.reply("❌ Dùng: ..nhac tên bài")

    msg = await message.reply("🔎 Đang tìm nhạc...")

    url = f"https://deezerdevs-deezer.p.rapidapi.com/search?q={query}"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as res:
            data = await res.json()

    if not data["data"]:
        return await msg.edit_text("❌ Không tìm thấy")

    song = data["data"][0]

    title = song["title"]
    artist = song["artist"]["name"]
    preview = song["preview"]
    thumb = song["album"]["cover_big"]

    text = f"🎧 {title}\n👤 {artist}\n\n▶️ Nghe thử:\n{preview}"

    await bot.send_photo(message.chat.id, thumb, caption=text)

    await msg.delete()
