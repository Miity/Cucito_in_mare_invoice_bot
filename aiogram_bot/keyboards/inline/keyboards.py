from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 



reset = InlineKeyboardButton(text = 'reset', callback_data='reset')


# create_inv =  InlineKeyboardButton('create new invoice')

# start_keyboard = InlineKeyboardMarkup(row_width=3,
#     inline_keyboard=[
#     [create_inv],
# ])


client_name = InlineKeyboardButton(text='name', callback_data='name')
adress = InlineKeyboardButton(text='adress', callback_data='adress')
description = InlineKeyboardButton(text='description', callback_data='description')
product = InlineKeyboardButton(text='product', callback_data='product')
show_saved_info = InlineKeyboardButton(text='show saved info', callback_data='show saved info')
save_file = InlineKeyboardButton(text='save file', callback_data='save file')


add_inline_invoice_keyboard = InlineKeyboardMarkup(row_width=3)
 
add_inline_invoice_keyboard.add(client_name,adress,description).add(product).add(show_saved_info,save_file).add(reset)

