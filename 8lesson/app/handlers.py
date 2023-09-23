from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb

router = Router()


class Registration(StatesGroup):
    login = State()
    password = State()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [5525270361]


@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Вы админ.')


@router.message(F.text == '/start')
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Registration.login)
    await message.answer('Введите логин', reply_markup=kb.main)


@router.message(Registration.login)
async def cmd_login(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await state.set_state(Registration.password)
    await message.answer('Введите пароль')


@router.message(Registration.password)
async def cmd_login(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    await message.answer(f'Введенные данные: {data["login"]} и {data["password"]}')
    await state.clear()


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.catalog)


@router.callback_query(F.data == 'adidas')
async def adidas(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали {callback.data}')
