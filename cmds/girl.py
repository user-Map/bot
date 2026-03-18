import requests

async def run(bot, message, args):

    try:
        msg = await message.reply("💖 Đang tìm gái xinh...")

        api = "https://nqduan.id.vn/api/images?category=girl"
        res = requests.get(api, timeout=30).json()

        # ⭐ bắt mọi dạng json
        img = None

        if isinstance(res, dict):
            img = res.get("url") or res.get("data") or res.get("result")
        elif isinstance(res, list):
            img = res[0]

        if not img:
            return await msg.edit_text("❌ API không trả ảnh")

        await msg.delete()

        await bot.send_photo(
            message.chat.id,
            img,
            caption="💖 Girl Random"
        )

    except Exception as e:
        await message.reply(f"❌ Lỗi GIRL: {e}")
