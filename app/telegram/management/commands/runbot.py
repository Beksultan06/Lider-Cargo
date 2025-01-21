import logging
import asyncio
from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher
from app.telegram.management.commands.app.bot import router
import django
import os

logging.basicConfig(level=logging.DEBUG)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

API_TOKEN = "7749815029:AAHu0CjSqNLLjq366h6CtTJYD78_tNOYlxw"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

class Command(BaseCommand):
    help = "Запускает Telegram-бота"

    def handle(self, *args, **kwargs):
        dp.include_router(router)

        async def main():
            try:
                logging.info("Запуск Telegram-бота...")
                await dp.start_polling(bot)
            except Exception as e:
                logging.error(f"Ошибка при запуске бота: {e}")
        asyncio.run(main())
