import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand, MenuButtonCommands

from app.bot.handlers import router


async def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN not set")

    # aiogram 3.7+: parse_mode через DefaultBotProperties
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Пункт «Меню бота» и команды
    await bot.set_my_commands([
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="checkinn", description="Проверка по ИНН"),
        BotCommand(command="contract", description="Собрать договор"),
    ])
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass