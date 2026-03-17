import os
import yt_dlp
from aiogram.types import FSInputFile

async def run(bot, message, args):

    if not args:
        await message.reply("⚡ dùng: ..tiktok link")
        return

    url = args[0]

    panel = await message.reply("""
╔══════════════════╗
   🎬 ĐANG TẢI VIDEO
╚══════════════════╝
""")

    try:

        ydl_opts = {
            'outtmpl': 'video.mp4',
            'format': 'mp4',
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        title = info.get("title", "TikTok Video")

        file = FSInputFile("video.mp4")

        await bot.send_document(
            chat_id=message.chat.id,
            document=file,
            caption=f"""
🎬 {title}

⬇️ Tải bằng USERMAP PRO
"""
        )

        os.remove("video.mp4")
        await panel.delete()

    except Exception as e:
        await panel.edit_text(f"❌ Lỗi tải:\n{e}")
