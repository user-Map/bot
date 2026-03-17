import re
import os
import yt_dlp
from aiogram.types import FSInputFile


def get_tiktok_url(text):
    urls = re.findall(r'(https?://\S+)', text)
    for u in urls:
        if "tiktok" in u:
            return u
    return None


async def run(bot, message, args):

    url = get_tiktok_url(message.text)

    if not url:
        await message.reply("❌ Không tìm thấy link TikTok")
        return

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

⬇️ USERMAP DOWNLOADER
"""
        )

        os.remove("video.mp4")
        await panel.delete()

    except Exception as e:
        await panel.edit_text(f"❌ Lỗi tải:\n{e}")
