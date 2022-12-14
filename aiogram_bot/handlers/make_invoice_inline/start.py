from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_bot.loader import dp, bot
from aiogram_bot.keyboards.inline.keyboards import add_inline_invoice_keyboard
from aiogram_bot.states.create_pdf import Create_states


@dp.message_handler(text='create new invoice')
async def start(message: types.Message,  state: FSMContext):
    await Create_states.start.set()
    await message.answer('wait', reply_markup= types.ReplyKeyboardRemove())
    await message.answer("your keyboard", reply_markup=add_inline_invoice_keyboard)
    data = await state.get_data()
    print('Saved data: ' + str(data))



@dp.callback_query_handler(state=Create_states.start)
async def step_answer(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'name':
        await Create_states.level_1.set()
        await callback.message.answer('type client name', reply_markup=types.ReplyKeyboardRemove())
    elif callback.data == 'adress':
        await Create_states.level_2.set()
        await callback.message.answer('type client adress', reply_markup=types.ReplyKeyboardRemove())
    elif callback.data == 'oggetto':
        await Create_states.level_3.set()
        await callback.message.answer('Scrivi oggetto', reply_markup=types.ReplyKeyboardRemove())
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
            file = await make_pdf(data)
            await bot.send_document(callback.message.chat.id, document=file)
            await Create_states.start.set()
        except Exception as e:
            print('except: ', e)
            if 'name' not in data or 'adress' not in data or 'oggetto' not in data or 'products' not in data:
                await callback.message.answer('need more info', reply_markup=types.ReplyKeyboardRemove())
                await Create_states.start.set()

    elif callback.data == 'reset':
        await state.finish()
        await callback.message.answer("Let's start again", reply_markup=types.ReplyKeyboardRemove())
        await Create_states.start.set()




@dp.message_handler(state=Create_states.level_1)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(name = message.text)
    await Create_states.start.set()
    data = await state.get_data()
    print(data)
    await message.answer("Name saved", reply_markup=add_inline_invoice_keyboard)

@dp.message_handler(state=Create_states.level_2)
async def add_descript(message: types.Message,  state: FSMContext):
    await state.update_data(adress = message.text)
    await Create_states.start.set()
    data = await state.get_data()
    print(data)
    await message.answer("Adress saved", reply_markup=add_inline_invoice_keyboard)


@dp.message_handler(state=Create_states.level_3)
async def add_oggetto(message: types.Message,  state: FSMContext):
    await state.update_data(oggetto = message.text)
    await Create_states.start.set()
    data = await state.get_data()
    print(data)
    await message.answer("oggetto salvato", reply_markup=add_inline_invoice_keyboard)

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


# gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=Create_states.level_5)
async def process_age_invalid(message: types.Message):
    return await message.reply("Price gotta be a number.\n What price is it? (digits only)")

@dp.message_handler(state=Create_states.level_5)
async def add_price_row(message: types.Message,  state: FSMContext):
    price = int(message.text)
    data = await state.get_data()
    data['products'][-1]['price'] = price
    await state.update_data(products = data['products'])

    await Create_states.start.set()
    data = await state.get_data()
    print(data)
    await message.answer("Product and price saved", reply_markup=add_inline_invoice_keyboard)