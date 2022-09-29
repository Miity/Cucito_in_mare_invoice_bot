from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.create_pdf import Create_states
from keyboards.default.keyboards import start_keyboard
from .steps import start


@dp.message_handler(state=Create_states.start)
async def step_answer(message: types.Message,  state: FSMContext):
    await state.update_data(state_mode_step=message.text)
    if message.text == 'name':
        await Create_states.level_1.set()
        await message.answer('type client name', reply_markup=types.ReplyKeyboardRemove())
    
    elif message.text == 'adress':
        await Create_states.level_2.set()
        await message.answer('type client adress', reply_markup=types.ReplyKeyboardRemove())

    elif message.text == 'description':
        await Create_states.level_3.set()
        await message.answer('description', reply_markup=types.ReplyKeyboardRemove())
        
    elif message.text == 'product':
        await Create_states.level_4.set()
        await message.answer('type the name of product', reply_markup=types.ReplyKeyboardRemove())

    elif message.text == 'show saved info':
        from .utils import show_price_info
        await show_price_info(message, state)
        await start(message, state)

    elif message.text == 'save file':
        data = await state.get_data()
        try:
            await message.answer('wait', reply_markup=types.ReplyKeyboardRemove())
            from . import make_pdf
            from loader import bot
            file = await make_pdf(state)
            await bot.send_document(message.chat.id,document=file)
            await start(message, state)
        except:
            if 'name' not in data or 'adress' not in data or 'description' not in data or 'products' not in data:
                await message.answer('need more info', reply_markup=types.ReplyKeyboardRemove())
                await start(message, state)

    
    elif message.text == 'reset':
        await state.finish()
        await message.answer("Let's start again", reply_markup=types.ReplyKeyboardRemove())
        from ..start import start_bot
        await start_bot(message)
