import asyncio
from aiogram import Bot, Dispatcher

from handlers import user_commands
from callbacks import payment

from dotenv import load_dotenv
import os

# Загрузка переменных из .env файла
load_dotenv()

bot_secret_key = os.getenv('BOT_SECRET_KEY')

async def main():
    bot = Bot(bot_secret_key)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        payment.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())