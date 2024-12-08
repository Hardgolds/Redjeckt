import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API_TOKEN = '7733659306:AAH9OpfZDXb6MB-coaNhIA8QUJZAOIYfOSQ'
CHANNEL_ID = 2458384810  # Закрытый канал, с которого бот будет репостить
TARGET_CHANNELS = ['@opendoorrrrrs', '@channel_2']  # Открытые каналы

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик для всех типов сообщений
@dp.message(lambda message: message.chat.id == CHANNEL_ID)  # Проверка на канал
async def repost_message(msg: types.Message):
    for target_channel in TARGET_CHANNELS:
        try:
            # Пересылаем сообщение в целевой канал
            await bot.forward_message(chat_id=target_channel, from_chat_id=msg.chat.id, message_id=msg.message_id)
            logging.info(f"Message forwarded to {target_channel}")
        except Exception as e:
            logging.error(f"Failed to forward message to {target_channel}: {e}")

async def main():
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
