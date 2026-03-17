import asyncio
import random

ADMINS = [7126997268]   # 👉 sửa ID bạn

SCOLD_TEXT = "𝓗𝓸́𝓽 𝓬𝓪́𝓲 đ𝓮́𝓸 𝓳 𝓬𝓾̣𝓹𝓴 đ𝓾𝓸̂𝓲 𝓵𝓪̂̉𝓷 𝓬𝓱𝓸̂́𝓷 đ𝓪̣𝓹 =)) 𝓬𝓱𝓸 𝓽𝓾𝓷𝓰 𝓵𝓸̂̀𝓷 𝓽𝓸́𝓮 𝓵𝓾̛̉𝓪 𝓬𝓪̂̀𝓾 𝔁𝓲𝓷 𝓶𝓪̀ 𝓴𝓱𝓸́𝓬 𝓵𝓸́𝓬 𝓽𝓸̂́𝓬 𝓬𝓱𝓸 1 𝓬𝓾̛𝓸̛́𝓬 𝓫𝓪𝔂 𝓼𝓪𝓷𝓰 𝓬𝓪𝓶 𝓼𝓪𝓷𝓰 𝓬𝓪𝓶 𝓫𝓲̣ 𝓽 𝓽𝓻𝓲́𝓬𝓱 đ𝓲𝓮̣̂𝓷 𝓿𝓸̂ 𝓶𝓾 𝓵𝓸̂̀𝓷 𝓶𝓮̣ 𝓶 𝓬𝓸𝓷 𝓬𝓱𝓸́ đ𝓲𝓮̂𝓷 𝓵𝓮̂𝓷 đ𝓪̂𝔂 𝓻𝓮́𝓸 𝓫𝓸𝔁 𝓿𝓸̂ 𝓫𝓮𝓶 đ𝓾̣ 𝓶𝓪́ 𝓭𝓪̆𝓶 𝓫𝓪 𝓷𝓰𝓸̂𝓷 𝓵𝓸̉ 𝓵𝓮̂𝓷 𝓼𝓪̀𝓷 𝓽𝓱𝓪́𝓲 đ𝓸̣̂ 𝓫𝓲̣ 𝓭𝓲́ 𝓬𝓱𝓸 𝓫𝓪𝔂 𝓵𝓸̂̀𝓷 𝓬𝓪̂̀𝓾 𝔁𝓲𝓷 𝓵𝓲𝓮̂́𝓶 𝓬𝓱𝓪̂𝓷 𝓫𝓶 𝓽𝓾̛̀ 𝓶𝓪̣̆𝓽 𝓵𝓮̂𝓷 đ𝓪̂𝔂 𝓻𝓾̉𝓪 𝓬𝓱𝓪 𝓻𝓾̉𝓪 𝓶𝓮̣ 𝓶𝓪̀ 𝓷𝓰𝓱𝓲̃ 𝓵𝓪̀ 𝓱𝓪𝔂 𝓱𝓪̉ 𝓬𝓱𝓸́ 𝓬𝓾̛𝓷𝓰 đ𝓾̣ 𝓶𝓪́ 24 đ𝓾́𝓪 𝓬𝓱𝓪̆́𝓬 𝓫𝓪̆̀𝓰 𝓬𝓪́𝓲 𝓶𝓾 𝓵𝓸̂̀𝓷 𝓵𝓮̂𝓷 đ𝓪̂𝔂 𝓴𝓱𝓸𝓮 𝓽𝓻𝓲̀𝓷𝓱 𝓱𝔀 𝓶𝓪́ 𝓸̛𝓲 𝓷𝓰𝓱𝓮 𝓽𝓸̛̉𝓶 𝓷𝓱𝓪 𝓶𝓪́ 𝓽 𝓵𝓪̂́𝔂 𝓬𝓪̂𝔂 𝓻𝓾̛̣𝓪 𝓽 𝓫𝓾̛̣𝓪 𝓿𝓸̂ 𝓵𝓸̂̀𝓷 𝓽𝓾̣𝓲 𝓫𝓪̂𝔂 𝓪̂𝓶 𝓫𝓲𝓷𝓱 𝓫𝓾̛𝓸̛́𝓷𝓰 𝓫𝓲̉𝓷𝓱 𝓬𝓪̂̀𝓾 𝔁𝓲𝓷 𝓽𝓱𝓪 𝓶𝓪̣𝓷𝓰 🤪🤪🤗🤗🤗 đ𝓲̃ 𝓬𝓱𝓸́ 𝓬𝓪̂̀𝓾 𝔁𝓲𝓷 đ𝓲 𝓵𝓶 𝓬𝓱𝓸́ =)) 𝓬𝓱𝓸 𝓱𝔀 đ𝓬 𝓴𝓮̂ 𝓶𝓪́ 𝓸̛𝓲 𝓭𝓾̛̣𝓪 𝓱𝓸̛𝓲 đ𝓮́𝓸 𝓬𝓱𝓪̂́𝓹 𝓴𝓮̂𝓾 𝓫𝓸̂́ 𝓾𝓼𝓮𝓻𝓶𝓪𝓹 𝓱𝓸𝓽𝔀𝓪𝓻 đ𝓲 𝓫𝓸̂́ 𝓶𝓪̀𝔂 𝓽𝓱𝓪 𝓬𝓱𝓸=)) =)) 🤣😜🤪"   # ⭐ câu cố định

async def run(bot, message, args):

    if message.from_user.id not in ADMINS:
        return await message.reply("❌ Không có quyền")

    if message.chat.type == "private":
        return await message.reply("⚠️ Chỉ dùng trong group")

    if not message.reply_to_message:
        return await message.reply("⚠️ Reply 1 người để dùng lệnh")

    if len(args) < 2:
        return await message.reply("⚠️ Dùng: ..scold <số_tin>")

    try:
        total = int(args[1])
    except:
        return await message.reply("❌ Số không hợp lệ")

    if total > 100:
        return await message.reply("⚠️ Tối đa 100 tin")

    user = message.reply_to_message.from_user
    name = user.first_name
    uid = user.id

    await message.reply("🚀 Bắt đầu Chửi thằng ngu lồn ")

    for i in range(total):

        msg = f"<a href='tg://user?id={uid}'>{name}</a> {SCOLD_TEXT}"

        await bot.send_message(
            message.chat.id,
            msg,
            parse_mode="HTML"
        )

        await asyncio.sleep(random.uniform(0,5))   # ⭐ delay random 4-5s

    await message.reply(" 𝓑𝓸̂́ đ𝓪̃ 𝓽𝓱𝓪 𝓬𝓱𝓸 𝓬𝓸𝓷 𝓻𝓸̂̀𝓲 đ𝓸́ 𝓬𝓸𝓷 đ𝓲̉ 𝓬𝓱𝓸́ 𝓑𝓲𝓮̂́𝓽 𝓬𝓪̉𝓶 𝓸̛𝓷 𝓴𝓸 𝓿𝓪̣̂𝔂 đ𝓲̉ 𝓷𝓰𝓾=)) ")
