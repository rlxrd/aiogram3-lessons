import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


# Polling, т.е бесконечный цикл проверки апдейтов
async def main():
    bot = Bot(token='6641089789:AAFV5I-IqkUQOFWTQtBDGI8qOyjLxd0jYuo')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


# Функция main() запускается только в случае если скрипт запущен с этого файла
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
