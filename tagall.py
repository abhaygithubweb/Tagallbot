from pyrogram import filters
from Tagger import app
import asyncio
import random
from config import TXT

@app.on_message(filters.command("tagall"))
async def tag_all_members(app, message):
    async for member in app.get_chat_members(message.chat.id):
        mention = member.user.mention
        await message.reply_text(f"{mention}, {random.choice(TXT)}")
        await asyncio.sleep(0.10)