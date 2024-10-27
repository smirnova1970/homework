"""The task "Vitamins for everyone!":
Complete the previously written code for the Telegram bot:
Create and complete keyboards:
Add the "Buy" button to the main (regular) menu keyboard.
Create an Inline menu of 4 buttons labeled "Product1", "Product2", "Product3", "Product4".
 Assign callback_data="product_buying" for all buttons
Create handlers and functions for them:
Message handler that reacts to the "Buy" text and wraps the get_buying_list(message) function.
The get_buying_list function should output the labels 'Name: Product<number> | Description: description <number>
| Price: <number * 100>' 4 times. After each label, display pictures of the products. At the end, display the
previously created Inline menu with the inscription "Select a product to purchase:".
A callback handler that responds to the text "product_buying" and wraps the send_confirm_message(call) function.
The send_confirm_message function sends the message "You have successfully purchased the product!"""


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

""" Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
 У всех кнопок назначьте callback_data="product_buying"  """
kb = InlineKeyboardMarkup(resize_keyboard=True)
button_ = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
button_2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
button_3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
button_4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
kb.insert(button_)
kb.insert(button_2)
kb.insert(button_3)
kb.insert(button_4)


kp = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kp.add(button)
kp.add(button2)

"""Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> |
Цена: <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное 
Inline меню с надписью "Выберите продукт для покупки:"."""
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('files/drawing1.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: Product1 | Описание: описание 1 | Цена: 200p')
    with open('files/drawing2.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: Product2 | Описание: описание 2 | Цена: 250p')
    with open('files/drawing3.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: Product3 | Описание: описание 3 | Цена: 300p')
    with open('files/drawing4.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: Product4 | Описание: описание 4 | Цена: 50p')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb)

"""Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call). 
Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!""""
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


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
