from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reset = KeyboardButton('reset')


create_inv =  KeyboardButton('create new invoice')

start_keyboard = ReplyKeyboardMarkup([
    [create_inv],
],resize_keyboard=True, input_field_placeholder='chose button')


who = KeyboardButton('A chi?')
obj = KeyboardButton('describe object')
add_obj = KeyboardButton('add_obj')
save_file = KeyboardButton('save file')

add_invoice_keyboard = ReplyKeyboardMarkup([
    [who, obj],
    [add_obj],
    [save_file, reset]
],resize_keyboard=True, input_field_placeholder='chose button')

