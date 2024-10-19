"""The task "Less text, more clicks":
It is necessary to supplement the code of the previous task so that questions about body parameters for calculating
calories are given at the touch of a button.
Change the message_handler for the set_age function. Now this handler will respond to the text 'Calculate',
 and not to 'Calories'.
Create a ReplyKeyboardMarkup keyboard and 2 Keyboard Buttons on it with the following text: 'Calculate'
and 'Information'. Make the keyboard adjust to the size of the device interface using the resize_keyboard parameter.
Use the previously created keyboard in the response to the start function using the reply_markup parameter.
As a result, when you use the /start command, you should be sent a keyboard with two buttons. When you click
on the button labeled 'Calculate', the set_age function is triggered, which starts the operation of the state
machine for age, growth and weight."""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button1, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Нажмите /START, чтобы начать общение.')


@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью!\n\nНажмите /Рассчитать, чтобы посчитать '
                         'необходимое вам суточное количество калорий', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я - бот, который знает секрет как похудеть!')


@dp.message_handler(text='Рассчитать')
async def set_gender(message):
    await message.answer('Введите свой пол (М/Ж):')
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    gender = data['gender']
    gender.lower()
    if gender=='м':
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    elif gender == 'ж':
        calories = 10 * weight + 6.25 * growth - 5 * age - 161
    else:
        await message.answer('Вы ввели ошибочные данные')
    await message.answer(f"Ваша норма калорий: {calories} ккал")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
