import requests

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("⚡ dùng: ..down link_tiktok")

    url = args[1]

    try:
        r = requests.get(
            "https://www.tikwm.com/api/",
            params={
                "url": url,
                "hd": 1
            }
        )

        data = r.json()

        video = data["data"]["play"]

        await bot.send_video(
            chat_id=message.chat.id,
            video=video,
            caption="📥 Video đã tải"
        )

    except:
        await message.reply("❌ tải video lỗi")
