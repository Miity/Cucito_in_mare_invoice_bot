
from cgitb import text
from email import message
from aiogram import types
from loader import dp
from keyboards.inline.keyboards import add_inline_invoice_keyboard

from aiogram.dispatcher import FSMContext
from states.create_pdf import Create_states


@dp.message_handler(text='create new invoice')
async def start(message: types.Message,  state: FSMContext):
    await Create_states.start.set()
    await message.answer('wait', reply_markup= types.ReplyKeyboardRemove())
    await message.answer("your keyboard", reply_markup=add_inline_invoice_keyboard)
    data = await state.get_data()
    print(data)




@dp.callback_query_handler(state=Create_states.start)
async def step_answer(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'name':
        await Create_states.level_1.set()
        await callback.message.answer('type client name', reply_markup=types.ReplyKeyboardRemove())
    elif callback.data == 'adress':
        await Create_states.level_2.set()
        await callback.message.answer('type client adress', reply_markup=types.ReplyKeyboardRemove())
    elif callback.data == 'description':
        await Create_states.level_3.set()
        await callback.message.answer('description', reply_markup=types.ReplyKeyboardRemove())
    elif callback.data == 'product':
        await Create_states.level_4.set()
        await callback.message.answer('type the name of product', reply_markup=types.ReplyKeyboardRemove())

    elif callback.data == 'show saved info':
        from .utils import show_price_info
        await show_price_info(callback.message, state)
        await Create_states.start.set()

    elif callback.data == 'save file':
        data = await state.get_data()
        try:
            await callback.message.answer('wait', reply_markup=types.ReplyKeyboardRemove())
            from .utils import make_pdf
            from loader import bot
            file = await make_pdf(state)
            await bot.send_document(callback.message.chat.id,document=file)
            await start(callback.message, state)
        except:
            if 'name' not in data or 'adress' not in data or 'description' not in data or 'products' not in data:
                await callback.message.answer('need more info', reply_markup=types.ReplyKeyboardRemove())
                await start(callback.message, state)

    elif callback.data == 'reset':
        await state.finish()
        await callback.message.answer("Let's start again", reply_markup=types.ReplyKeyboardRemove())
        from ..start import start_bot
        await start_bot(callback.message)




@dp.message_handler(state=Create_states.level_1)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(name = message.text)
    await Create_states.start.set()
    data = await state.get_data()
    print(data)

@dp.message_handler(state=Create_states.level_2)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(adress = message.text)
    await Create_states.start.set()
    data = await state.get_data()
    print(data)


@dp.message_handler(state=Create_states.level_3)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(description = message.text)
    await Create_states.start.set()
    data = await state.get_data()
    print(data)

@dp.message_handler(state=Create_states.level_4)
async def add_title_row(message: types.Message,  state: FSMContext):
    product = {'txt': message.text, 'price': None}

    data = await state.get_data()
    if 'products' in data:
        data['products'].append(product)
        await state.update_data(products = data['products'])
    else:
        await state.update_data(products = [product])

    await message.answer('write the price')
    await Create_states.level_5.set()

@dp.message_handler(state=Create_states.level_5)
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
    data['products'][-1]['price'] = price
    await state.update_data(products = data['products'])

    await Create_states.start.set()
    data = await state.get_data()
    print(data)