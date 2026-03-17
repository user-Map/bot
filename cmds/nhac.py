import yt_dlp
from aiogram import types

async def run(bot, message: types.Message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..nhac <tên bài>")

    query = " ".join(args[1:])

    msg = await message.reply("🔎 Đang tìm nhạc...")

    try:
        ydl_opts = {
            "format": "bestaudio",
            "quiet": True,
            "noplaylist": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)

            video = info["entries"][0]

            title = video["title"]
            link = video["webpage_url"]

        await msg.edit_text(
            f"🎧 {title}\n{link}"
        )

    except Exception as e:
        await msg.edit_text(f"❌ Lỗi: {e}")
