from aiogram import types
import requests

async def img_handler(message: types.Message):
    if not message.text.startswith("..img"):
        return
    
    q = message.text.replace("..img","").strip()
    if not q:
        return await message.reply("Nhập từ khoá ảnh")

    url = f"https://image.pollinations.ai/prompt/{q}"

    await message.answer_photo(photo=url)
