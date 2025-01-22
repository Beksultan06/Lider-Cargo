from aiogram import types, Router
from aiogram.filters import Command
from app.telegram.management.commands.app.button import inline
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

router = Router()
User = get_user_model()

@router.message(Command("start"))
async def start(message: types.Message):
    chat_id = message.chat.id
    username = message.from_user.username
    full_name = message.from_user.full_name or "Неизвестно"

    if username is None:
        await message.answer(
            "У вас отсутствует username в Telegram. Пожалуйста, установите его в настройках и повторите попытку."
        )
        return
    try:
        user, created = await sync_to_async(User.objects.get_or_create)(
            username=username,
            defaults={
                "chat_id": chat_id,
                "full_name": full_name,
            },
        )
        if not created and user.chat_id != chat_id:
            user.chat_id = chat_id
            await sync_to_async(user.save)()
        if created:
            await message.answer(f"Привет, {full_name}! Вы успешно зарегистрированы. Ваш chat_id сохранен.", reply_markup=inline)
        else:
            await message.answer(f"Привет, {user.full_name}! Ваш chat_id обновлен.", reply_markup=inline)

    except Exception as e:
        await message.answer("Произошла ошибка при обработке данных. Попробуйте позже.")
        print(f"Ошибка: {e}")