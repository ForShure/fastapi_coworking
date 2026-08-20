import asyncio
import os
import logging
import grpc

from protos import coworking_pb2
from protos import coworking_pb2_grpc

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("TOKEN")
user_router = Router()

@user_router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Напиши ID рабочего места, которое хочешь забронировать.")\

@user_router.message()
async def handler_text(message: Message):
    if not message.text.isdigit():
        await message.answer("Введи ID рабочего места числом.")
        return

    workplace_id = int(message.text)

    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = coworking_pb2_grpc.CoworkingServiceStub(channel)

        request = coworking_pb2.BookRequest(
            workplace_id=workplace_id
        )

        response = await stub.BookWorkplace(request)

    if response.success:
        await message.answer(f"✅{response.message}")
    else:
        await message.answer(f"❌{response.message}")

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user_router)
    logging.info("🚀 Бот успешно запущен! Пути настроены.")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stop")
