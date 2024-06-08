from aiogram import types
from aiogram.filters.command import Command
from dispatcher import dp

strings = {
    "help_text": ""
}

txt = {}

@dp.message(Command("help"))
async def help_handler(msg: types.Message):
    await msg.reply(strings["help_text"].format(**txt))
