"""Task "Support Bot (Start)":
To the code from the preparatory video, write two asynchronous functions:
start(message) - prints a line in the console 'Hello! I'm a bot helping your health.' .
It starts only when the '/start' command is written in a chat with a 
bot. (use the appropriate decorator)
all_messages(message) - prints a line in the console
'Enter the /start command to start the conversation.'. 
Runs on any access not described earlier. (use the appropriate decorator)
Launch your Telegram bot and check its performance."""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
