from aiogram import types
from aiogram.dispatcher import FSMContext


async def print_log(state: FSMContext):
    print('state data is: ', str(await state.get_data()))
    # await message.answer(str(await state.get_data()))


async def show_price_info(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data == '{}' or data == None:
        await message.answer("you didn't write any information, yet")
    if 'name' in data:
        await message.answer(data['name'])
    if 'adress' in data:
        await message.answer(data['adress'])
    if "description" in data:
        await message.answer(data['description'])
    if "products" in data:
        num = 1
        txt = ''
        for obj in data['products']:
            txt = txt + '{} {} | {} \n'.format(str(num), obj['txt'], obj['price'])
            num += 1
        await message.answer(txt)


async def make_pdf(data):
    
    from pdf_file.models import PDF

    f = PDF()
    f.add_page()
    f.set_filename(data['name'])
    f.set_client_name(data['name'])
    f.set_client_adress(data['adress'])
    f.set_oggetto(data['description'])
    f.print_price_list(data['products'])
    f.s_footer()
    f.output(f.filename)

    file = types.InputFile(f.filename,f.filename)
    return file
