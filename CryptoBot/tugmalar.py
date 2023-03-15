from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

btnBitcoin = InlineKeyboardButton(text='Bitcoin',callback_data='cc_bitcoin')
btnLitecoin = InlineKeyboardButton(text='Litecoin',callback_data='cc_litecoin')
btnDogecoin = InlineKeyboardButton(text='Dogecoin',callback_data='cc_dogecoin')

crupto_list = InlineKeyboardMarkup(row_width=1)
crupto_list.insert(btnBitcoin)
crupto_list.insert(btnLitecoin)
crupto_list.insert(btnDogecoin)


