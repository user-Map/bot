import requests

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..tiktok <link>")

    link = args[1]

    try:
        msg = await message.reply("📥 Đang tải video TikTok...")

        api = f"https://nqduan.id.vn/api/tiktok?action=download&url={link}"
        res = requests.get(api, timeout=60).json()

        data = res["data"]

        video = data["play"]
        music = data["music"]
        title = data["title"]

        await bot.send_video(
            message.chat.id,
            video,
            caption=f"🎬 {title}"
        )

        await bot.send_audio(
            message.chat.id,
            music,
            caption="🎧 Nhạc từ video"
        )

        await msg.delete()

    except Exception as e:
        await message.reply(f"❌ Lỗi tải TikTok: {e}")
