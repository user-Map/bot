import json
import os

FILE = "admins.json"


def load():
    if not os.path.exists(FILE):
        return {"owner": [], "admin": []}
    with open(FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


async def run(bot, message, args):

    data = load()
    uid = message.from_user.id

    owners = data["owner"]
    admins = data["admin"]

    # ⭐ menu manager
    if len(args) == 1:
        if uid not in owners and uid not in admins:
            return await message.reply("❌ Bạn không có quyền")

        text = """
╔══════════════════╗
        👮 MANAGER
╚══════════════════╝

⚙️ ADMIN SYSTEM
┠➤ ..addadmin <id>
┠➤ ..deladmin <id>
┠➤ ..listadmin

⚙️ BOT
┠➤ ..reload
┠➤ ..uptime
"""
        return await message.reply(text)

    # ⭐ add admin (OWNER ONLY)
    if args[1] == "addadmin":
        if uid not in owners:
            return await message.reply("❌ Chỉ OWNER dùng")

        try:
            new = int(args[2])
        except:
            return await message.reply("❌ Nhập ID")

        if new in admins:
            return await message.reply("⚠️ Đã là admin")

        admins.append(new)
        save(data)
        return await message.reply("✅ Đã thêm admin")

    # ⭐ del admin
    if args[1] == "deladmin":
        if uid not in owners:
            return await message.reply("❌ Chỉ OWNER dùng")

        try:
            rem = int(args[2])
        except:
            return await message.reply("❌ Nhập ID")

        if rem not in admins:
            return await message.reply("⚠️ Không tồn tại")

        admins.remove(rem)
        save(data)
        return await message.reply("✅ Đã xoá admin")

    # ⭐ list admin
    if args[1] == "listadmin":

        text = "👑 OWNER:\n"
        for o in owners:
            text += f"• {o}\n"

        text += "\n👮 ADMIN:\n"
        for a in admins:
            text += f"• {a}\n"

        return await message.reply(text)
