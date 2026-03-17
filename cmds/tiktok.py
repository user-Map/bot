import requests
import os
from aiogram.types import FSInputFile

async def run(bot, message, args):

    if not args:
        await message.reply("""
🎬 <b>TIKTOK DOWNLOADER</b>

❗ Gửi link video TikTok

Ví dụ:
<code>..tiktok https://vt.tiktok.com/xxxxx</code>
""", parse_mode="HTML")
        return

    url = args[0]

    loading = await message.reply("""
╔══════════════════╗
   🎬 <b>ĐANG TẢI VIDEO</b>
╚══════════════════╝

⏳ Vui lòng chờ...
""", parse_mode="HTML")

    try:
        api = f"https://www.tikwm.com/api/?url={url}"

        data = requests.get(api).json()

        video_url = data["data"]["play"]
        title = data["data"]["title"]

        video = requests.get(video_url).content

        with open("tiktok.mp4", "wb") as f:
            f.write(video)

        file = FSInputFile("tiktok.mp4")

        await bot.send_video(
            chat_id=message.chat.id,
            video=file,
            caption=f"""
🎬 <b>TIKTOK DOWNLOADED</b>

📝 {title}

✨ USERMAP VIP
""",
            parse_mode="HTML"
        )

        os.remove("tiktok.mp4")
        await loading.delete()

    except Exception as e:
        await loading.edit_text(f"""
❌ <b>LỖI TẢI VIDEO</b>

<code>{e}</code>
""", parse_mode="HTML")
