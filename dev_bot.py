from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from lexicon.lexicon import LEXICON_RU
from environs import Env

env = Env()
env.read_env()

bot = Bot(token=env('TOKEN'))
dp = Dispatcher(bot)


def create_inline_kb(row_width, *args, **kwargs) -> InlineKeyboardMarkup:
    inline_kb = InlineKeyboardMarkup(row_width=row_width)
    if args:
        [inline_kb.insert(InlineKeyboardButton(text=LEXICON_RU[button],
                                               callback_data=button)) for button in args]
    if kwargs:
        [inline_kb.insert(InlineKeyboardButton(text=text,
                                               callback_data=button)) for button, text in kwargs.items()]
    return inline_kb


async def process_start_command(message: Message):
    await message.answer(text='inline buttons with url parametr')


async def process_buttons_press(callback: CallbackQuery):
    if callback['data'] == 'button1_pressed' and callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 1',
                                         reply_markup=callback.message.reply_markup)
    elif callback['data'] == 'button2_pressed' and callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(text='Была нажата БОЛЬШАЯ КНОПКА 2',
                                         reply_markup=callback.message.reply_markup)
    else:
        await callback.answer(show_alert=True, text='This button alrady pushed')
    await callback.answer()

dp.register_message_handler(process_start_command, commands='start')
dp.register_callback_query_handler(process_buttons_press, text=[
                                   'button1_pressed', 'button2_pressed'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
