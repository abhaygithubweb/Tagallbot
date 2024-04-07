import asyncio
import random
import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from Tagger import app


@app.on_message(filters.command("start"))
async def start(_, m: Message):

    await m.reply_photo("https://graph.org/file/2c7697ae0b7eaaca3478a.jpg", caption=f"""🥀 ʜᴇʏ {m.from_user.mention},\n\nᴛʜɪs ɪs {app.me.mention},\nᴀ ᴘᴏᴡᴇʀғᴜʟʟ ᴛᴀɢ ᴀʟʟ ʙᴏᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛᴏ sᴛᴀʀᴛ ɴᴇᴡ ᴄᴏɴᴠᴏ.""",
                         reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ", url=f"https://t.me/{app.me.username}?startgroup=new")],
        [InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="t.me/unxsupportchat"), InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url="t.me/unxassociation")]
    ]))