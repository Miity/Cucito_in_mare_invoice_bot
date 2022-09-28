from aiogram import types
from loader import dp

from keyboards.default.keyboards import start_keyboard


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    print('bot started by new user')
    await message.answer('Press the button for start making new invoice', reply_markup=start_keyboard)
