import json
import os

FILE = "admins.json"

def load():
    if not os.path.exists(FILE):
        return {"owner": [], "admin": []}
    return json.load(open(FILE))


async def run(bot, message, args):

    data = load()
    uid = message.from_user.id

    if uid not in data["owner"] and uid not in data["admin"]:
        return await message.reply("❌ Không có quyền mở Manager")

    text = """
╔══════════════════╗
        👮 MANAGER
╚══════════════════╝

⚙️ BOT
┠➤ ..reload
┠➤ ..uptime

👥 GROUP CONTROL
┠➤ ..kick (reply)
┠➤ ..ban (reply)
┠➤ ..mute <time> (reply)
┠➤ ..unmute (reply)

🛡 GROUP SYSTEM
┠➤ ..warn (reply)
┠➤ ..antilink on/off
┠➤ ..antibot on/off
"""
    await message.reply(text)
