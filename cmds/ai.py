import requests

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("⚡ dùng: ..ai nội dung")

    text = " ".join(args[1:])

    try:
        r = requests.get(
            f"https://api.affiliateplus.xyz/api/chatbot",
            params={
                "message": text,
                "botname": "TeleBot",
                "ownername": "Khoi"
            }
        )

        data = r.json()
        await message.reply(data["message"])

    except:
        await message.reply("❌ AI lỗi rồi")
