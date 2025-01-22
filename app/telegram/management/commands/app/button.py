from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from django.conf import settings


inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Написать менеджеру", url="https://www.youtube.com/")],
    [InlineKeyboardButton(text='Пройти регистрацию', web_app=WebAppInfo(url=f'{settings.SITE_BASE_URL}/register'))]
])