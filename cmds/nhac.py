import aiohttp
from aiogram import types

async def run(bot, message: types.Message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..nhac <tên bài>")

    query = " ".join(args[1:])

    msg = await message.reply("🔎 Đang tìm nhạc...")

    try:
        async with aiohttp.ClientSession() as session:

            # 🔥 search nhạc
            async with session.get(
                f"https://api.popcat.xyz/youtube?q={query}"
            ) as res:
                data = await res.json()

            if not data or "url" not in data:
                return await msg.edit_text("❌ Không tìm thấy")

            video = data["url"]

            # 🔥 lấy mp3
            mp3 = f"https://api.popcat.xyz/ytmp3?url={video}"

            await msg.edit_text(
                f"🎧 Nhạc đây:\n{mp3}"
            )

    except Exception as e:
        await msg.edit_text(f"❌ Lỗi: {e}")
