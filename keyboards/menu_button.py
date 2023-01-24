from aiogram import Dispatcher, types

async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Начать игру'),
        types.BotCommand(command='/help', description='Справка по игре'),
        types.BotCommand(command='/test', description='Тестовая командо меню')
    ]
    await dp.bot.set_my_commands(main_menu_commands)