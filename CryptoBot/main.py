import logging
from pycoingecko import CoinGeckoAPI
import tugmalar as nav
from aiogram import Bot, Dispatcher, executor, types
from API_TOKEN import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)
cg = CoinGeckoAPI()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Salom 👋 Kriptovalyuta Botga Xush Kelibsiz {0.first_name}\n"
                           "KriptoValyutani Tanlang".format(message.from_user), reply_markup=nav.crupto_list)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'start':
        result = cg.get_price(id=message.text, vs_currencies='usd')
        await bot.send_message(message.from_user.id,
                               f"Kriptovalyuta {message.text}\n Hozirgi Holati> : {result[message.text]['usd']} $",
                               reply_markup=nav.crupto_list)


@dp.callback_query_handler(text_contains='cc_')
async def crupto(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    currency = str(callback_data[3:])
    result = cg.get_price(ids=currency, vs_currencies='usd')
    await bot.send_message(call.from_user.id, f"Kriptovalyuta {currency}\n Hozirgi Holati> {result[currency]['usd']} $",
                           reply_markup=nav.crupto_list)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
