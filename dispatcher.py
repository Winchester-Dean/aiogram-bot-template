from config import TOKEN

from aiogram import Bot, Dispatcher
from filters import IsAdminFilter

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)