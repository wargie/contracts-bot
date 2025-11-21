import asyncio
import os
from pathlib import Path
import warnings

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.bot.handlers import router as handlers_router
from app.bot.registry_search import router as registry_router

# подавим предупреждение от docxcompose/pkg_resources
warnings.filterwarnings("ignore", category=UserWarning, module=r"docxcompose\.properties")

def load_env():
    # грузим .env из корня проекта (родитель app/)
    root_env = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path=root_env)

async def main():
    load_env()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN not set")

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Роутеры бота
    dp.include_router(handlers_router)
    dp.include_router(registry_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass