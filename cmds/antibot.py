import json

FILE = "group.json"

async def run(bot, message, args):

    data = json.load(open("admins.json"))
    uid = message.from_user.id

    if uid not in data["owner"] and uid not in data["admin"]:
        return await message.reply("❌ Không có quyền")

    g = json.load(open(FILE))

    if len(args) < 2:
        return await message.reply("⚠️ Dùng: ..antibot on/off")

    if args[1].lower() == "on":
        g["antibot"] = True
        text = "✅ AntiBot ON"

    elif args[1].lower() == "off":
        g["antibot"] = False
        text = "❌ AntiBot OFF"

    else:
        return await message.reply("⚠️ Dùng: ..antibot on/off")

    json.dump(g, open(FILE, "w"))
    await message.reply(text)
