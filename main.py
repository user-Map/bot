import yt_dlp
import os
import requests

def expand(url):
    try:
        r = requests.get(url, allow_redirects=True, timeout=10)
        return r.url
    except:
        return url


async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("⚡ dùng: ..tiktok link")

    url = args[1]
    url = expand(url)

    panel = await message.reply("""
╔══════════════╗
   🎬 Đang tải TikTok
   ⏳ vui lòng chờ...
╚══════════════╝
""")

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

        await bot.send_document(
            message.chat.id,
            document=open("video.mp4", "rb"),
            caption=f"🎬 {title}"
        )

        os.remove("video.mp4")
        await panel.delete()

    except Exception as e:

        await panel.edit_text(f"""
❌ Không tải được video

📎 {url}

⚠️ Có thể video bị private / hạn chế
""")
