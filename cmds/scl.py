import aiohttp

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        return await message.reply("🎧 Nhập tên bài")

    url = f"https://api.siputzx.my.id/api/d/soundcloud?query={query}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()

    if not data.get("status"):
        return await message.reply("❌ Không tìm thấy")

    result = data["data"]

    await message.reply("⬇️ Đang gửi nhạc...")

    await bot.send_audio(
        message.chat.id,
        result["url"],
        title=result["title"]
    )
