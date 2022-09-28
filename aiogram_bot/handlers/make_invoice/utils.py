from aiogram import types
from aiogram.dispatcher import FSMContext


async def print_log(state: FSMContext):
    print('state data is: ', str(await state.get_data()))
    # await message.answer(str(await state.get_data()))


async def show_price_info(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data == {} or data == None:
        await message.answer("you didn't write any information, yet")
    if 'client' in data:
        await message.answer(data['client'])
    if "description" in data:
        await message.answer(data['description'])
    if "objs" in data:
        num = 1
        txt = ''
        for obj in data['objs']:
            txt = txt + '{} {} | {} \n'.format(str(num), obj['txt'], obj['price'])
            num += 1
        await message.answer(txt)


async def make_pdf(state: FSMContext):
    
    filename = 'file.pdf'
    from pdf_file.models import PDF

    f = PDF()
    f.add_page()
    data = await state.get_data()
    f.set_a(data['client'])
    f.set_oggetto(data['description'])

    f.print_price_list(data['objs'])
    f.s_footer()
    
    f.output(filename)

    file = types.InputFile(filename,filename)
    return file
