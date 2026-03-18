import requests
import random

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..img <từ khoá>")

    query = " ".join(args[1:])

    msg = await message.reply("🖼 Đang tìm ảnh...")

    try:
        # ⭐ API 1
        url = f"https://btch.downloader.world/api/search/pinterest?query={query}"
        res = requests.get(url, timeout=30).json()

        imgs = res.get("result")

        # ⭐ nếu API 1 chết → dùng API 2
        if not imgs:
            url2 = f"https://nqduan.id.vn/api/pinterest?query={query}&limit=10"
            res2 = requests.get(url2, timeout=30).json()
            imgs = res2.get("data") or res2.get("result")

        if not imgs:
            return await msg.edit_text("❌ Không tìm thấy ảnh")

        await msg.delete()

        for img in random.sample(imgs, min(5, len(imgs))):
            await bot.send_photo(message.chat.id, img)

    except Exception as e:
        await message.reply(f"❌ Lỗi IMG: {e}")
