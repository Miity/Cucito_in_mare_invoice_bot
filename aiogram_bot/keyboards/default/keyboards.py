from telnetlib import KERMIT
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reset = KeyboardButton('reset')


create_inv =  KeyboardButton('create new invoice')

start_keyboard = ReplyKeyboardMarkup([
    [create_inv],
],resize_keyboard=True, input_field_placeholder='chose button')


client_name = KeyboardButton('name')
adress = KeyboardButton('adress')
description = KeyboardButton('description')
product = KeyboardButton('product')
show_saved_info = KeyboardButton('show saved info')
save_file = KeyboardButton('save file')


add_invoice_keyboard = ReplyKeyboardMarkup([
    [client_name, adress, description],
    [product],
    [show_saved_info, save_file],
    [reset]
],resize_keyboard=True, input_field_placeholder='chose button')

