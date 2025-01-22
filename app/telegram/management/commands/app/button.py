from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Написать менеджеру", url="https://www.youtube.com/")],
    [InlineKeyboardButton(text='Пройти регистрацию', web_app=WebAppInfo(url='https://www.youtube.com/'))]
])