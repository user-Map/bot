import requests
import random

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("⚡ dùng: ..img từ_khoá")

    key = " ".join(args[1:])

    try:
        r = requests.get(
            "https://api.popcat.xyz/images/search",
            params={"q": key}
        )

        data = r.json()

        img = random.choice(data["images"])

        await bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption=f"🖼 ảnh: {key}"
        )

    except:
        await message.reply("❌ tìm ảnh lỗi")
