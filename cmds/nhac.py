import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "BOT_TOKEN"

async def nhac(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.startswith(".nhac"):
        return

    keyword = text.replace(".nhac", "").strip()

    if not keyword:
        await update.message.reply_text("❌ Nhập tên bài")
        return

    msg = await update.message.reply_text("🔎 Đang tìm nhạc...")

    url = f"https://ytsearch.vercel.app/api?query={keyword}"
    data = requests.get(url).json()

    if not data["results"]:
        await msg.edit_text("❌ Không tìm thấy nhạc")
        return

    menu = "🎧 <b>KẾT QUẢ TÌM NHẠC</b>\n\n"

    for i, v in enumerate(data["results"][:5], start=1):
        title = v["title"]
        link = v["url"]
        duration = v["duration"]

        menu += f"""
{i}️⃣ <b>{title}</b>
⏱ {duration}
▶️ <a href="{link}">Nghe ngay</a>

"""

    await msg.edit_text(menu, parse_mode="HTML", disable_web_page_preview=True)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, nhac))

app.run_polling()
