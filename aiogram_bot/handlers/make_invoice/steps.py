from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.create_pdf import Create_states

from keyboards.default.keyboards import start_keyboard, add_invoice_keyboard

from .utils import print_log



'''
1. start creating new invoice +
1.1 pass all name of input in buttons +
2. input for whom this invoice +
3. input object of invoice +
4. input name and price +
5. save invoice and send pdf file to user
'''

@dp.message_handler(text='create new invoice')
async def start(message: types.Message, state: FSMContext):
    await print_log(state)
    await message.answer(text='Chose something from keyboard',reply_markup=add_invoice_keyboard)
    await Create_states.start.set()


@dp.message_handler(state=Create_states.level_1)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(client = message.text)
    await start(message, state)


@dp.message_handler(state=Create_states.level_2)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(description = message.text)
    await start(message, state)


@dp.message_handler(state=Create_states.level_3)
async def add_title_row(message: types.Message,  state: FSMContext):
    obj = {'txt': message.text, 'price': None}

    data = await state.get_data()
    if 'objs' in data:
        data['objs'].append(obj)
        await state.update_data(objs = data['objs'])
    else:
        await state.update_data(objs = [obj])

    await message.answer('write the price')
    await Create_states.level_4.set()

@dp.message_handler(state=Create_states.level_4)
async def add_price_row(message: types.Message,  state: FSMContext):
    try:
        price = int(message.text)
    except:
        await message.answer('errore, write the number')
        await message.answer('write the price')
        await Create_states.level_4.set()
        from loader import bot
        await bot.get_updates()
    
    data = await state.get_data()
    data['objs'][-1]['price'] = price
    await state.update_data(objs = data['objs'])

    await start(message, state)
