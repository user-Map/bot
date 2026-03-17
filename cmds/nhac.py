import yt_dlp
import asyncio
import os

cache = {}

async def run(bot, message, args):

    query = " ".join(args[1:])

    if not query:
        return await message.reply("❌ Dùng: ..nhac tên bài")

    msg = await message.reply("🔎 Đang tìm nhạc...")

    loop = asyncio.get_event_loop()

    def search():
        with yt_dlp.YoutubeDL({
            "quiet": True,
            "skip_download": True
        }) as ydl:
            info = ydl.extract_info(
                f"ytsearch5:{query}",
                download=False
            )
            return info["entries"]

    results = await loop.run_in_executor(None, search)

    cache[message.message_id] = results

    text = "🎧 CHỌN NHẠC\n\n"

    for i, r in enumerate(results, 1):
        text += f"{i}. {r['title']}\n"

    text += "\n👉 Reply số để tải"

    await msg.edit_text(text)


async def reply(bot, message):

    if not message.reply_to_message:
        return

    mid = message.reply_to_message.message_id

    if mid not in cache:
        return

    try:
        index = int(message.text) - 1
        video = cache[mid][index]
    except:
        return

    url = video["webpage_url"]

    msg = await message.reply("⬇️ Đang tải mp3...")

    def download():
        with yt_dlp.YoutubeDL({
            "format": "bestaudio",
            "outtmpl": "song.%(ext)s",
            "quiet": True
        }) as ydl:
            ydl.download([url])

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, download)

    file = None
    for f in os.listdir():
        if f.startswith("song."):
            file = f

    await msg.edit_text("📤 Đang gửi...")

    await bot.send_audio(
        message.chat.id,
        open(file, "rb"),
        title=video["title"]
    )

    os.remove(file)
