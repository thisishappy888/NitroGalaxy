from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import inline

router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Выбери, что хочешь купить.", reply_markup=inline.main)
