"""The task "He answered me!":
Change the start and all_messages functions so that instead of output to the console,
 lines are sent in telegram chat.
Launch your Telegram bot and check its performance.
Notes:
To respond to a message, run the answer method asynchronously.
When sending your code to GitHub, do not forget to remove the key to connect to your bot!"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler()
async def all_message(message):
    await message.reply('Введите команду /start, чтобы начать общение.')



@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
