import json

async def run(bot, message, args):

    with open("db.json") as f:
        db = json.load(f)

    top = sorted(db.items(), key=lambda x: x[1], reverse=True)[:10]

    msg = "🏆 BXH CHAT\n\n"

    i = 1
    for uid, count in top:
        msg += f"{i}. {uid} → {count}\n"
        i += 1

    await message.reply(msg)
