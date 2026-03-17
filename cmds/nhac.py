import yt_dlp
import os
from aiogram.types import FSInputFile

async def run(bot, message, args):

    query = " ".join(args)

    if not query:
        await message.reply("""
🎧 <b>MUSIC PANEL</b>

❗ Vui lòng nhập tên bài hát

Ví dụ:
<code>..nhac 1000 năm</code>
""", parse_mode="HTML")
        return

    loading = await message.reply(f"""
╔══════════════════╗
   🎧 <b>ĐANG TÌM NHẠC</b>
╚══════════════════╝

🔎 Từ khoá: <b>{query}</b>
⏳ Vui lòng chờ...
""", parse_mode="HTML")

    ydl_opts = {
        'format': 'bestaudio[filesize<40M]/bestaudio',
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            entry = info['entries'][0]

            file = ydl.prepare_filename(entry)
            title = entry.get('title', 'Music')
            duration = entry.get('duration', 0)
            views = entry.get('view_count', 0)

        audio = FSInputFile(file)

        await bot.send_audio(
            chat_id=message.chat.id,
            audio=audio,
            title=title,
            caption=f"""
🎶 <b>{title}</b>

👁 Views: <b>{views}</b>
⏱ Duration: <b>{duration}s</b>

✨ Powered by USERMAP
""",
            parse_mode="HTML"
        )

        os.remove(file)
        await loading.delete()

    except Exception as e:
        await loading.edit_text(f"""
❌ <b>LỖI TẢI NHẠC</b>

<code>{e}</code>
""", parse_mode="HTML")
