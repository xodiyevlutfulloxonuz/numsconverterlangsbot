from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='english  🇺🇸', callback_data='en'),
         InlineKeyboardButton(text='rus  🇷🇺', callback_data='ru')],

    ]
)
