import yt_dlp

async def run(bot, message, args):
    query = " ".join(args[1:])

    if not query:
        return await message.reply("❌ Dùng: ..nhac tên bài")

    msg = await message.reply("🔎 Đang tìm nhạc...")

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "format": "bestaudio"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)

        video = info["entries"][0]

        await bot.send_audio(
            message.chat.id,
            audio=video["url"],
            title=video["title"]
        )

        await msg.delete()

    except:
        await msg.edit_text("❌ Không lấy được nhạc (server bị YouTube chặn)")
