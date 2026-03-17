import os
import requests

API_KEY = os.getenv("OPENAI_KEY")

memory = {}

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("⚡ dùng: ..ai nội_dung")

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
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": memory[chat_id][-10:]
            },
            timeout=60
        )

        data = r.json()

        # ⭐ CHECK ERROR
        if "choices" not in data:
            return await message.reply(f"❌ OpenAI lỗi:\n{data}")

        reply = data["choices"][0]["message"]["content"]

        memory[chat_id].append({
            "role": "assistant",
            "content": reply
        })

        await message.reply(reply)

    except Exception as e:
        await message.reply("❌ AI crash: " + str(e))
