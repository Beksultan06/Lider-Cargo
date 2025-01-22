from aiogram import types, Router
from aiogram.filters import Command
from app.telegram.management.commands.app.button import inline

router = Router()

@router.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Приветя карго бот", reply_markup=inline)

