import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand, MenuButtonCommands

from app.bot.handlers import router as handlers_router
from app.bot.checkinn import router as checkinn_router


async def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN not set")

    # aiogram 3.7+: parse_mode указываем через DefaultBotProperties
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Кнопка «Меню бота» и список команд
    await bot.set_my_commands([
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="checkinn", description="Проверка по ИНН"),
        BotCommand(command="contract", description="Собрать договор"),
    ])
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())

    dp = Dispatcher()
    # порядок не критичен, но логично — сначала базовые сценарии, затем частные
    dp.include_router(handlers_router)
    dp.include_router(checkinn_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
