# routers/share.py
from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

share_router = Router()

@share_router.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🎙️ Участник", callback_data="speaker"),
            InlineKeyboardButton(text="🎓 Сопровождающий", callback_data="companion")
        ]
    ])
    await message.answer(
        "Привет👋 На конференции ты присутствуешь как:",
        reply_markup=keyboard
    )


