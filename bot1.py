# Импортируем все необходимые библиотеки
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

# Импортируем дополнительный файл, в котором храним токен.
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(msg: types.Message):
     await bot.send_message(msg.from_user.id, msg.text+"просто текст")

if __name__ == '__main__':
    executor.start_polling(dp)
