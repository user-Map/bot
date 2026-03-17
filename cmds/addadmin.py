import json
import os

FILE = "admins.json"

def load():
    if not os.path.exists(FILE):
        return {"owner": [], "admin": []}
    return json.load(open(FILE))

def save(data):
    json.dump(data, open(FILE, "w"))

async def run(bot, message, args):

    data = load()
    uid = message.from_user.id

    if uid not in data["owner"]:
        return await message.reply("❌ Chỉ OWNER mới thêm admin")

    if not message.reply_to_message:
        return await message.reply("⚠️ Reply người cần add")

    target = message.reply_to_message.from_user.id

    if target in data["admin"]:
        return await message.reply("⚠️ Đã là admin")

    data["admin"].append(target)
    save(data)

    await message.reply("✅ Đã thêm admin")
