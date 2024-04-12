import logging
from os import getenv
from huepy import bad
from pyrogram import Client, filters
from pyrogram.enums import ParseMode, ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

API_ID = getenv("20780584")
API_HASH = getenv("9182371e5d69184a3a8f2feab777e9a3")
BOT_TOKEN = getenv("6636720264:AAG9rIUfo7dIi0qp5wOasXcproLHwNkQfSE")
CHANNEL_LOGS = getenv("CHANNEL_LOGS")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
    parse_mode=ParseMode.HTML,
)
