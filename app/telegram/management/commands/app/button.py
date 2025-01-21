from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Написать менеджеру", callback_data="manager")],
    [InlineKeyboardButton(text='Пройти регистрацию', callback_data='register')]
])
