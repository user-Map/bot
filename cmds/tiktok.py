import re
import os
import requests
import yt_dlp
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

router = Router()


def get_url(text):
    urls = re.findall(r'(https?://\S+)', text)
    for u in urls:
        if "tiktok" in u:
            return u
    return None


def expand_url(url):
    try:
        r = requests.get(url, allow_redirects=True, timeout=10)
        return r.url
    except:
        return url


@router.message(F.text)
async def auto_tiktok(message: Message):

    url = get_url(message.text)
    if not url:
        return

    panel = await message.reply("""
╔══════════════════╗
   🎬 ĐANG TẢI TIKTOK
   ⏳ Vui lòng chờ...
╚══════════════════╝
""")

    url = expand_url(url)

    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'
        }
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        title = info.get("title", "TikTok Video")

        file = FSInputFile("video.mp4")

        await message.reply_document(
            document=file,
            caption=f"""
🎬 {title}

⬇️ USERMAP DOWNLOADER PRO
"""
        )

        os.remove("video.mp4")
        await panel.delete()

    except Exception as e:

        await panel.edit_text(f"""
❌ Không tải được video

📎 Link:
{url}

⚠️ Có thể video bị hạn chế / private
""")
