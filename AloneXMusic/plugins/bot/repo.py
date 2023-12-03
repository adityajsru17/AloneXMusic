from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """
ʙᴇᴛᴀ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ? 🗿 
...ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊᴅᴇ 10ᴍ ʙsss  ᴍᴀᴅᴀʀᴄʜᴏᴅ

ᴛᴇʀᴇ ʙᴀᴀᴘ sᴇ ʀᴇᴘᴏ ʟᴇʟᴇ ᴊᴀᴀᴋᴇ [ᴛᴇʀᴀ ʙᴀᴀᴘ ](https://t.me/HereShiva)
 

 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/70402820cd4afd8ea4c13.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
