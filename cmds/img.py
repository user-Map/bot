import requests
import random

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..img <từ khoá>")

    query = " ".join(args[1:])

    try:
        msg = await message.reply("🖼 Đang tìm ảnh ...")

        url = f"https://nqduan.id.vn/api/pinterest?query={query}&limit=10"
        res = requests.get(url, timeout=30).json()

        imgs = res.get("result")

        if not imgs:
            return await msg.edit_text("❌ Không tìm thấy ảnh")

        await msg.delete()

        for img in random.sample(imgs, min(5, len(imgs))):
            await bot.send_photo(
                message.chat.id,
                img,
                caption=f"🖼 {query}"
            )

    except Exception as e:
        await message.reply(f"❌ Lỗi IMG: {e}")
