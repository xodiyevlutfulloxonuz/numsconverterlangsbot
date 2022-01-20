from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline.inlinekeyboard import keyboards
from states.User import Lang
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Tilni tanlang.", reply_markup=keyboards)
    await Lang.lang.set()
    



   







