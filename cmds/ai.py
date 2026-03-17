import os
import requests
from telegram import Update
from telegram.ext import ContextTypes

API_KEY = os.getenv("OPENAI_KEY")

chat_memory = {}

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if not msg:
        return

    text = msg.text.replace("..ai", "").strip()

    if not text:
        await msg.reply_text("⚡ dùng: ..ai nội_dung")
        return

    if not API_KEY:
        await msg.reply_text("❌ Chưa set API KEY")
        return

    chat_id = msg.chat_id

    if chat_id not in chat_memory:
        chat_memory[chat_id] = []

    chat_memory[chat_id].append({
        "role": "user",
        "content": text
    })

    await context.bot.send_chat_action(chat_id, "typing")

    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": chat_memory[chat_id][-8:]
            },
            timeout=60
        )

        data = r.json()

        reply = data["choices"][0]["message"]["content"]

        chat_memory[chat_id].append({
            "role": "assistant",
            "content": reply
        })

        if msg.reply_to_message:
            await msg.reply_text(
                reply,
                reply_to_message_id=msg.reply_to_message.message_id
            )
        else:
            await msg.reply_text(reply)

    except Exception as e:
        await msg.reply_text("❌ AI lỗi: " + str(e))
