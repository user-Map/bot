import json

FILE = "group.json"

async def run(bot, message, args):

    data = json.load(open("admins.json"))
    uid = message.from_user.id

    if uid not in data["owner"] and uid not in data["admin"]:
        return await message.reply("❌ Không có quyền")

    if not message.reply_to_message:
        return await message.reply("⚠️ Reply người cần warn")

    g = json.load(open(FILE))

    user = str(message.reply_to_message.from_user.id)

    g["warn"].setdefault(user, 0)
    g["warn"][user] += 1

    json.dump(g, open(FILE, "w"))

    if g["warn"][user] >= 3:
        await bot.ban_chat_member(message.chat.id, int(user))
        return await message.reply("🚫 3 warn → BAN")

    await message.reply(f"⚠️ Warn {g['warn'][user]}/3")
