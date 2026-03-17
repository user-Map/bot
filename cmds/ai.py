import requests
import os

API_KEY = os.getenv("GROQ_KEY")

memory = {}

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("⚡ dùng: ..ai nội_dung")

    if not API_KEY:
        return await message.reply("❌ Chưa set GROQ_KEY")

    text = " ".join(args[1:])
    chat_id = message.chat.id

    if chat_id not in memory:
        memory[chat_id] = []

    memory[chat_id].append({
        "role": "user",
        "content": text
    })

    try:
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": memory[chat_id][-10:]
            },
            timeout=60
        )

        data = r.json()

        # ⭐ CHECK ERROR
        if "error" in data:
            return await message.reply("❌ API lỗi: " + str(data["error"]["message"]))

        reply = data["choices"][0]["message"]["content"]

        memory[chat_id].append({
            "role": "assistant",
            "content": reply
        })

        await message.reply(reply)

    except Exception as e:
        await message.reply("❌ AI crash: " + str(e))
