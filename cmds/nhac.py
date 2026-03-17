import aiohttp
from aiogram import types

async def run(bot, message: types.Message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..nhac <tên bài>")

    query = " ".join(args[1:])

    await message.reply("🔎 Đang tìm nhạc...")

    try:
        async with aiohttp.ClientSession() as session:

            # 🔥 search youtube
            async with session.get(
                f"https://api.vevioz.com/api/button/youtube?q={query}"
            ) as res:

                text = await res.text()

                # 👉 lấy video id
                import re
                find = re.search(r"watch\\?v=(.{11})", text)

                if not find:
                    return await message.reply("❌ Không tìm thấy nhạc")

                vid = find.group(1)

            # 🔥 lấy link mp3
            link = f"https://api.vevioz.com/api/button/mp3/{vid}"

            await message.reply(
                f"🎧 Nhạc của bạn đây:\n{link}"
            )

    except Exception as e:
        await message.reply(f"❌ Lỗi: {e}")
