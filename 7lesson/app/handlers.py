from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter

import app.keyboards as kb

router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [5525270361]


@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Вы админ.')


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать', reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.catalog)


@router.callback_query(F.data == 'adidas')
async def adidas(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали {callback.data}')
