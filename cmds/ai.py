import requests

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("❓ dùng: ..ai nội dung")

    text = " ".join(args[1:])

    try:
        res = requests.get(
            f"https://api.simsimi.vn/v2/simtalk",
            params={"text": text, "lc": "vn"}
        )

        data = res.json()
        msg = data.get("message", "bot ko trả lời")

        await message.reply(msg)

    except:
        await message.reply("⚠️ lỗi AI")
