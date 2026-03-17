import requests

async def run(bot, message, args):
    if len(args) < 2:
        return await message.reply("❌ Dùng: ..weather <thành phố>")

    city = " ".join(args[1:])

    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url, timeout=10).json()

        temp = data["current_condition"][0]["temp_C"]
        feel = data["current_condition"][0]["FeelsLikeC"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        hum = data["current_condition"][0]["humidity"]

        text = f"""
🌤 Thời tiết: {city}
🌡 Nhiệt độ: {temp}°C
🥵 Cảm giác: {feel}°C
💧 Độ ẩm: {hum}%
📌 Trạng thái: {desc}
"""

        await message.reply(text)

    except:
        await message.reply("❌ Không lấy được thời tiết")
