"""The task "Even more choice":
It is necessary to supplement the code of the previous task so that when you click on the "Calculate" button,
an Inline keyboard is sent.
Create an InlineKeyboardMarkup keyboard with 2 InlineKeyboardButton buttons:
With the text 'Calculate calorie allowance' and callback_data='calories'
With the text 'Calculation Formulas' and callback_data='formulas'
Create a new main_menu(message) function that:
It will be wrapped in the message_handler decorator, triggered when passing the text 'Calculate'.
The function itself will send a previously created Inline menu and the text 'Select an option:'
Create a new get_formulas(call) function that:
It will be wrapped in the callback_query_handler decorator, which will respond to the text 'formulas'.
He will send a message with the Mifflin-San Geor formula.
Change the set_age function and the decorator for it:
Change the decorator to callback_query_handler, which will respond to the text 'calories'.
Now the function accepts a call instead of a message. Access to the message will be as follows - call.message.
As a result, the following algorithm will be obtained:
The /start command is entered
The usual menu is sent to this command: 'Calculate' and 'Information'.
In response to the 'Calculate' button, an Inline menu is sent: 'Calculate Calorie allowance' and 'Calculation Formulas'
A message with the formula is sent via the Inline button 'Calculation Formulas'.
Using the Inline button 'Calculate the calorie rate', the state machine starts working along the chain."""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kl = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
kl.add(button)
kl.add(button2)

kp = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kp.add(button)
kp.add(button2)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kl)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5'  
                              'Для женщин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) - 161')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!', reply_markup=kp)

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!')

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
                         'необходимое вам суточное количество калорий', reply_markup=kb, parse_mode='HTML')

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
