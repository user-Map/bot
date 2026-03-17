import yt_dlp
import asyncio
import os

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        return await message.reply("🎧 Nhập tên bài hát")

    await message.reply("🔎 Đang tìm nhạc...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    loop = asyncio.get_event_loop()

    def download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            return info

    info = await loop.run_in_executor(None, download)

    file = None
    for f in os.listdir():
        if f.startswith("song."):
            file = f

    if not file:
        return await message.reply("❌ Lỗi tải nhạc")

    title = info['entries'][0]['title']

    await message.reply("⬇️ Đang gửi nhạc...")

    await bot.send_audio(
        message.chat.id,
        open(file, 'rb'),
        title=title
    )

    os.remove(file)
