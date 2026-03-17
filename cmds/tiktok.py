import requests
import os
from aiogram.types import FSInputFile

def get_real_url(url):
    return requests.get(url, allow_redirects=True, timeout=10).url


async def run(bot, message, args):

    if not args:
        await message.reply("""
╔══════════════════╗
   🎬 TIKTOK DOWNLOADER
╚══════════════════╝

⚡ Dùng:
..tiktok link
""")
        return

    url = args[0]

    panel = await message.reply(f"""
╔══════════════════════╗
   🎬 ĐANG PHÂN TÍCH LINK
╚══════════════════════╝

🔗 Link: {url}

⏳ Vui lòng chờ...
""")

    try:

        # mở link rút gọn
        if "vt.tiktok.com" in url or "vm.tiktok.com" in url:
            url = get_real_url(url)

        await panel.edit_text("""
╔══════════════════════╗
   🔎 ĐANG LẤY DỮ LIỆU
╚══════════════════════╝

📡 Kết nối server TikTok...
""")

        api = f"https://tikwm.com/api/?url={url}"
        data = requests.get(api, timeout=20).json()

        if not data.get("data"):
            await panel.edit_text("""
❌ Không lấy được video

📌 Có thể:
• Video private
• API lỗi
• Link sai
""")
            return

        video_url = data["data"]["play"]
        title = data["data"]["title"]
        author = data["data"]["author"]["nickname"]

        await panel.edit_text(f"""
╔══════════════════════╗
   ⬇️ ĐANG TẢI VIDEO HD
╚══════════════════════╝

🎬 Nội dung:
{title[:50]}...

👤 {author}
""")

        video = requests.get(video_url, timeout=60).content

        with open("tiktok.mp4", "wb") as f:
            f.write(video)

        file = FSInputFile("tiktok.mp4")

        await bot.send_video(
            chat_id=message.chat.id,
            video=file,
            caption=f"""
╔══════════════════════╗
      🎬 TIKTOK VIDEO
╚══════════════════════╝

📝 Nội dung:
{title}

👤 Tác giả: {author}

✨ USERMAP VIP
"""
        )

        os.remove("tiktok.mp4")
        await panel.delete()

    except Exception as e:
        await panel.edit_text(f"❌ Lỗi tải video:\n{e}")
