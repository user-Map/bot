import yt_dlp
import asyncio

cache = {}

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        return await message.reply("🎵 Nhập tên bài hát")

    loop = asyncio.get_event_loop()

    def search():
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "format": "bestaudio"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                f"scsearch5:{query}",
                download=False
            )
            return info["entries"]

    results = await loop.run_in_executor(None, search)

    text = "🎧 DANH SÁCH SOUND CLOUD\n\n"

    for i, r in enumerate(results, 1):
        text += f"{i}. {r['title']}\n"

    text += "\n👉 Reply số để chọn"

    cache[message.id] = results

    await message.reply(text)
