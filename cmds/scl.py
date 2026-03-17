import aiohttp

cache = {}

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        return await message.reply("🎧 Nhập tên bài: ..scl <tên>")

    url = f"https://api.popcat.xyz/soundcloud?q={query}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()

    if not data:
        return await message.reply("❌ Không tìm thấy")

    cache[message.message_id] = data[:5]

    text = "🎵 DANH SÁCH NHẠC\n\n"

    for i, song in enumerate(data[:5], 1):
        text += f"{i}. {song['title']}\n"

    text += "\n👉 Reply số để chọn"

    await message.reply(text)


async def reply(bot, message):

    if not message.reply_to_message:
        return

    mid = message.reply_to_message.message_id

    if mid not in cache:
        return

    try:
        index = int(message.text) - 1
        song = cache[mid][index]
    except:
        return

    await message.reply("⬇️ Đang gửi nhạc...")

    await bot.send_audio(
        message.chat.id,
        song["url"],
        title=song["title"]
    )
