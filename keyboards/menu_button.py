from aiogram import Dispatcher, types


# Функция для настройки кнопки Menu бота
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Запуск бота'),
        types.BotCommand(command='/beginning', description='В начало книги'),
        types.BotCommand(command='/continue', description='Продолжить чтение'),
        types.BotCommand(command='/bookmarks', description='Мои закладки'),
        types.BotCommand(command='/help', description='Справка по работе бота')
    ]
    await dp.bot.set_my_commands(main_menu_commands)