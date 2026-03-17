import requests
from aiogram import types

API = "https://wttr.in/{}?format=j1"

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("🌦 Dùng: ..weather <thành phố>")

    city = " ".join(args[1:])

    try:
        r = requests.get(API.format(city))
        data = r.json()

        now = data["current_condition"][0]
        temp = now["temp_C"]
        feel = now["FeelsLikeC"]
        humidity = now["humidity"]
        wind = now["windspeedKmph"]
        desc = now["weatherDesc"][0]["value"]

        text = f"""
🌦 THỜI TIẾT {city.upper()}

🌡 Nhiệt độ: {temp}°C
🥵 Cảm giác như: {feel}°C
☁ Trạng thái: {desc}
💧 Độ ẩm: {humidity}%
🌬 Gió: {wind} km/h
"""

        await message.reply(text)

    except:
        await message.reply("❌ Không lấy được thời tiết")
