from aiogram import types
from aiogram.filters.command import Command
from dispatcher import dp

strings = {
    "start_text": "<b>{} Welcome to our bot</b>"
}

txt = {
    "name": "n/a"
}

@dp.message(Command("start"))
async def start_handler(msg: types.Message):
    txt["name"] = msg.from_user.first_name

    await msg.reply(strings["start_text"].fromat(**txt))
