from aiogram import types
from aiogram.filters import Command
import yt_dlp
import os

def setup(dp):

    @dp.message(Command("nhac"))
    async def nhac_handler(message: types.Message):

        text = message.text.replace("/nhac", "").strip()

        if not text:
            await message.reply(
                "🎧 Nhập tên bài hát\nVí dụ:\n/nhac Sơn Tùng MTP"
            )
            return

        await message.reply("🔎 Đang tìm nhạc...")

        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'song.%(ext)s',
            'quiet': True
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(
                    f"ytsearch1:{text}",
                    download=True
                )

                file = ydl.prepare_filename(info['entries'][0])

            await message.reply_audio(
                audio=types.FSInputFile(file),
                title=info['entries'][0]['title']
            )

            os.remove(file)

        except:
            await message.reply("❌ Không lấy được nhạc")
