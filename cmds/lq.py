import requests

async def run(bot, message, args):
    try:
        msg = await message.reply("🎮 Đang lấy acc Liên Quân...")

        res = requests.get(
            "https://nqduan.id.vn/api/lq-acc?count=1",
            timeout=20
        ).json()

        acc = res["data"][0]

        user = acc.get("username", "N/A")
        pwd = acc.get("password", "N/A")
        skin = acc.get("skin", "N/A")
        rank = acc.get("rank", "N/A")

        text = f"""
🎮 ACC LIÊN QUÂN FREE

👤 User: {user}
🔑 Pass: {pwd}
🏆 Rank: {rank}
✨ Skin: {skin}
"""

        await msg.edit_text(text)

    except Exception as e:
        await message.reply(f"❌ API lỗi: {e}")
