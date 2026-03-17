import asyncio
import yt_dlp

cache = {}

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        return await message.reply("🎧 Nhập tên bài: .scl <tên>")

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

    text = "🎵 <b>DANH SÁCH NHẠC</b>\n\n"

    for i, r in enumerate(results, 1):
        text += f"{i}. {r['title']}\n"

    text += "\n👉 Reply số để chọn"

    msg = await message.reply(text, parse_mode="HTML")

    cache[msg.message_id] = results

    # auto xoá list sau 60s
    async def auto_delete():
        await asyncio.sleep(60)
        try:
            await msg.delete()
        except:
            pass

    asyncio.create_task(auto_delete())


async def reply(bot, message):

    if not message.reply_to_message:
        return

    mid = message.reply_to_message.message_id

    if mid not in cache:
        return

    try:
        index = int(message.text) - 1
        song = cache[mid][index]
    except:
        return

    title = song["title"]
    thumb = song["thumbnail"]
    url = song["url"]

    caption = f"""
🎧 <b>{title}</b>

✨ Quality: HD
🚀 Powered by USERMAP
"""

    await bot.send_photo(
        message.chat.id,
        thumb,
        caption=caption,
        parse_mode="HTML"
    )

    await bot.send_audio(
        message.chat.id,
        url,
        title=title
    )
