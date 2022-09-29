from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 



reset = InlineKeyboardButton(text = 'reset', callback_data='reset')


# create_inv =  InlineKeyboardButton('create new invoice')

# start_keyboard = InlineKeyboardMarkup(row_width=3,
#     inline_keyboard=[
#     [create_inv],
# ])


client_name = InlineKeyboardButton(text='Nome', callback_data='name')
adress = InlineKeyboardButton(text='indirizzo', callback_data='adress')
oggetto = InlineKeyboardButton(text='oggetto', callback_data='oggetto')
product = InlineKeyboardButton(text='servizio', callback_data='product')
show_saved_info = InlineKeyboardButton(text='mostra le informazioni memorizzate', callback_data='show saved info')
save_file = InlineKeyboardButton(text='salva', callback_data='save file')


add_inline_invoice_keyboard = InlineKeyboardMarkup(row_width=3)
 
add_inline_invoice_keyboard.add(client_name,adress,oggetto).add(product).add(show_saved_info,save_file).add(reset)

