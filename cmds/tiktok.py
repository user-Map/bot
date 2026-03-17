import requests
import os
from aiogram.types import FSInputFile

headers = {
    "user-agent": "Mozilla/5.0"
}

def get_real_url(url):
    r = requests.get(url, allow_redirects=True, headers=headers, timeout=10)
    return r.url


async def run(bot, message, args):

    if not args:
        await message.reply("⚡ dùng: ..tiktok link")
        return

    url = args[0]

    panel = await message.reply("""
╔══════════════════╗
   🎬 ĐANG XỬ LÝ
╚══════════════════╝
""")

    try:

        if "vt.tiktok.com" in url:
            url = get_real_url(url)

        api = f"https://www.tikwm.com/api/?url={url}"

        res = requests.get(api, headers=headers, timeout=30)

        data = res.json()

        if "data" not in data:
            await panel.edit_text("❌ API không trả dữ liệu")
            return

        video_url = data["data"]["play"]
        title = data["data"]["title"]
        author = data["data"]["author"]["nickname"]

        await panel.edit_text("⬇️ Đang tải video HD...")

        video = requests.get(video_url, headers=headers, timeout=60).content

        with open("tt.mp4", "wb") as f:
            f.write(video)

        file = FSInputFile("tt.mp4")

        await bot.send_video(
            chat_id=message.chat.id,
            video=file,
            caption=f"""
🎬 {title}

👤 {author}
"""
        )

        os.remove("tt.mp4")
        await panel.delete()

    except Exception as e:
        await panel.edit_text(f"❌ Lỗi: {e}")
