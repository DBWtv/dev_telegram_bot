from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from environs import Env

env = Env()
env.read_env()

bot = Bot(token=env('TOKEN'))
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup()

button_1 = InlineKeyboardButton(text='Najmi na knopku poluchish rezultat',
                                callback_data='button1_pressed')
button_2 = InlineKeyboardButton(text='Docs telegram',
                                callback_data='button2_pressed')


keyboard.add(button_1).add(button_2)


async def process_start_command(message):
    await message.answer(text='inline buttons with url parametr', reply_markup=keyboard)


async def process_buttons_press(callback: CallbackQuery):
    if callback['data'] == 'button1_pressed':
        if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
            await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 1',
                                             reply_markup=callback.message.reply_markup)
        await callback.answer()
    elif callback['data'] == 'button2_pressed':
        if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
            await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 2',
                                             reply_markup=callback.message.reply_markup)
        await callback.answer()

dp.register_message_handler(process_start_command, commands='start')
dp.register_callback_query_handler(process_buttons_press, text=[
                                   'button1_pressed', 'button2_pressed'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
