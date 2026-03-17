import aiohttp

cache = {}

async def run(bot, message, args):
    query = " ".join(args[1:])

    if not query:
        return await message.reply("❌ Dùng: ..nhacyt tên bài")

    msg = await message.reply("🔎 Đang tìm...")

    url = f"https://api.vevioz.com/api/search?q={query}"

    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            data = await r.json()

    videos = data["items"][:5]

    text = "🎧 Chọn bài:\n\n"

    for i,v in enumerate(videos,1):
        text += f"{i}. {v['title']}\n"

    cache[message.from_user.id] = videos

    await msg.edit_text(text)


async def choose(bot, message):
    if message.from_user.id not in cache:
        return

    if not message.text.isdigit():
        return

    index = int(message.text)-1
    videos = cache[message.from_user.id]

    if index<0 or index>=len(videos):
        return

    video = videos[index]

    await bot.send_message(message.chat.id,"📥 Đang lấy nhạc...")

    mp3 = f"https://api.vevioz.com/api/button/mp3/{video['url']}"

    await bot.send_audio(
        message.chat.id,
        audio=mp3,
        title=video["title"]
    )
