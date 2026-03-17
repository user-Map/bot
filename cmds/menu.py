from aiogram import types

async def run(bot, message, args):

    text = """
╔══════════════════╗
   🔥 𝗨𝗦𝗘𝗥𝗠𝗔𝗣 𝗩𝗜𝗣 🔥
╚══════════════════╝

🤖 AI
┠➤ ..ai <câu hỏi>

🖼 ẢNH
┠➤ ..img <từ khoá>

🌦 THỜI TIẾT
┠➤ ..weather <thành phố>

🛠 TOOL
┠➤ ..id
┠➤ ..time
┠➤ ..ping
┠➤ ..uptime

👥 GROUP
┠➤ ..map
┠➤ ..tagall
┠➤ ..kick (reply)

⚙️ ADMIN
┠➤ ..reload

ㅤ
      ᵇᵒᵗ ᵇʸ 𝗻𝗴𝘂𝘆𝗲𝗻𝗸𝗵𝗼𝗶
"""

    await message.reply(text)
