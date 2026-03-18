import requests

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..uidfb <link facebook>")

    link = args[1]

    try:
        msg = await message.reply("🔎 Đang lấy UID Facebook...")

        api = f"https://nqduan.id.vn/api/fb-uid?url={link}"
        res = requests.get(api, timeout=30).json()

        data = res.get("data")

        if not data:
            return await msg.edit_text("❌ Không lấy được UID")

        uid = data.get("uid")
        name = data.get("name")
        url = data.get("url")

        text = f"""
┏━━━━━━━━━━━━━━━━━━━┓
      🆔 UID FACEBOOK
┗━━━━━━━━━━━━━━━━━━━┛

👤 Tên : {name}
🆔 UID : {uid}
🔗 Link : {url}
"""

        await msg.edit_text(text)

    except Exception as e:
        await message.reply(f"❌ Lỗi UIDFB: {e}")
