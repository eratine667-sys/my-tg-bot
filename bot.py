import asyncio
import os  # Добавляем этот модуль для работы с переменными
from aiogram import Bot, Dispatcher, types

async def main():
    # Бот возьмет токен из поля "Значение", которое ты заполнил на хосте
    token = os.getenv('BOT_TOKEN') 
    
    if not token:
        print("Ошибка: Переменная BOT_TOKEN не найдена в настройках хостинга!")
        return

    bot = Bot(token=token)
    dp = Dispatcher()

    @dp.message(lambda m: m.text == "/start")
    async def start(m: types.Message):
        await m.answer("привет")

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
