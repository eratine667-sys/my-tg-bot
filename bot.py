import asyncio
from aiogram import Bot, Dispatcher, types

async def main():
    bot = Bot(token='ТВОЙ_ТОКЕН')
    dp = Dispatcher()

    @dp.message(lambda m: m.text == "/start")
    async def start(m: types.Message):
        await m.answer("привет")

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
