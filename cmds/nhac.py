import yt_dlp
import os

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        await message.reply("🎧 Nhập tên bài hát\nVí dụ: ..nhac 100 năm")
        return

    msg = await message.reply("🔎 Đang tìm nhạc...")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'song.%(ext)s',
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            file = ydl.prepare_filename(info['entries'][0])
            title = info['entries'][0]['title']

        await bot.send_audio(
            chat_id=message.chat.id,
            audio=open(file, 'rb'),
            title=title
        )

        os.remove(file)
        await msg.delete()

    except Exception as e:
        await msg.edit(f"❌ Lỗi lấy nhạc\n{e}")
