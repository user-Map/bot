import requests
import random

async def run(bot, message, args):

    try:
        msg = await message.reply("💖 Đang tìm gái xinh...")

        api = "https://nqduan.id.vn/api/images?category=girl"
        res = requests.get(api, timeout=30).json()

        imgs = []

        # ⭐ bắt mọi dạng JSON
        if isinstance(res, dict):
            imgs = res.get("data") or res.get("result") or res.get("url")
        elif isinstance(res, list):
            imgs = res

        # ⭐ nếu chỉ là 1 link string
        if isinstance(imgs, str):
            imgs = [imgs]

        if not imgs:
            return await msg.edit_text("❌ API không trả ảnh")

        await msg.delete()

        # ⭐ gửi random 3 ảnh
        for img in random.sample(imgs, min(3, len(imgs))):
            await bot.send_photo(
                message.chat.id,
                img,
                caption="💖 Girl Random"
            )

    except Exception as e:
        await message.reply(f"❌ Lỗi GIRL: {e}")
