import yt_dlp
import asyncio

cache = {}

async def run(bot, message, args):
    query = " ".join(args[1:])

    if not query:
        return await message.reply("❌ Dùng: ..nhacyt tên bài")

    msg = await message.reply("🔎 Đang tìm nhạc...")

    ydl_opts = {
        'quiet': True,
        'skip_download': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch5:{query}", download=False)

    videos = info["entries"]

    text = "🎧 Chọn bài:\n\n"

    for i, v in enumerate(videos, 1):
        text += f"{i}. {v['title']}\n"

    cache[message.from_user.id] = videos

    await msg.edit_text(text)


async def choose(bot, message):
    if message.from_user.id not in cache:
        return

    if not message.text.isdigit():
        return

    index = int(message.text) - 1
    videos = cache[message.from_user.id]

    if index < 0 or index >= len(videos):
        return

    video = videos[index]

    url = video["webpage_url"]

    await bot.send_message(message.chat.id, "📥 Đang tải mp3...")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'song.mp3',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    await bot.send_audio(
        message.chat.id,
        audio=open("song.mp3", "rb"),
        title=video["title"]
    )
