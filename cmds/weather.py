import requests

def icon(code):
    if code == 0:
        return "☀️ Trời quang"
    if code in [1,2,3]:
        return "⛅ Có mây"
    if code in [45,48]:
        return "🌫 Sương mù"
    if code in [51,53,55]:
        return "🌦 Mưa nhẹ"
    if code in [61,63,65]:
        return "🌧 Mưa"
    if code in [71,73,75]:
        return "❄️ Tuyết"
    if code in [95,96,99]:
        return "⛈ Giông"
    return "🌡 Không rõ"

async def run(bot, message, args):

    if len(args) < 2:
        return await message.reply("❌ Dùng: ..weather <thành phố>")

    city = " ".join(args[1:])

    try:
        msg = await message.reply("🌦 Đang lấy thời tiết VIP...")

        # ⭐ LẤY TOẠ ĐỘ
        geo = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}",
            timeout=15
        ).json()

        if "results" not in geo:
            return await msg.edit_text("❌ Không tìm thấy thành phố")

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        name = geo["results"][0]["name"]

        # ⭐ LẤY WEATHER
        weather = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max,temperature_2m_min&timezone=auto",
            timeout=15
        ).json()

        cur = weather["current_weather"]
        daily = weather["daily"]

        text = f"""
┏━━━━━━━━━━━━━━━━━━━┓
      🌦 𝗪𝗘𝗔𝗧𝗛𝗘𝗥 𝗩𝗜𝗣
┗━━━━━━━━━━━━━━━━━━━┛

📍 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻 : {name}

🌡 𝗧𝗲𝗺𝗽 𝗡𝗼𝘄 : {cur["temperature"]}°C
💨 𝗪𝗶𝗻𝗱     : {cur["windspeed"]} km/h
📊 𝗦𝘁𝗮𝘁𝘂𝘀  : {icon(cur["weathercode"])}

┏━━ 📅 𝗧𝗼𝗱𝗮𝘆 𝗙𝗼𝗿𝗲𝗰𝗮𝘀𝘁 ━━┓
🔺 𝗛𝗶𝗴𝗵 : {daily["temperature_2m_max"][0]}°C
🔻 𝗟𝗼𝘄  : {daily["temperature_2m_min"][0]}°C
┗━━━━━━━━━━━━━━━━━━━━┛
"""

        await msg.edit_text(text)

    except Exception as e:
        await message.reply(f"❌ Lỗi weather VIP: {e}")
