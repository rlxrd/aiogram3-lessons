import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot(token='')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!')
    

@dp.message(F.text == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')
    await message.answer_photo(photo='url',
                               caption='описание')


@dp.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
