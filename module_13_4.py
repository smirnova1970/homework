"""State Group:
Import the State and StatesGroup classes from aiogram.dispatcher.filters.state.
Create a userState class inherited from StatesGroup.
Inside this class, describe 3 objects of the State class: age, growth, weight (age, height, weight).
This group (class) will be used in the message_handler call chain. Write the following functions to handle states:
The set_age(message) function:
Wrap it in a message_handler that responds to the 'Calories' text message.
This function should output a message to the Telegram bot 'Enter your age:'.
After that, you can enter the age in the userState.age attribute using the set method.
The set_growth(message, state) function:
Wrap it in a message_handler that reacts to the passed state of userState.age.
This function should update the data in the age state to message.text (a user-written message). Use the update_data method.
Next, it should output a message to the Telegram bot 'Enter your height:'.
After waiting for the growth to be entered in the userState attribute.growth using the set method.
The set_weight(message, state) function:
Wrap it in a message_handler that reacts to the passed userState state.growth.
This function should update the data in the growth state to message.text (a user-written message).
Use the update_data method.
Next, it should output a message to the Telegram bot 'Enter your weight:'.
After that, wait for the height to be entered into the userState.weight attribute using the set method.
The send_calories(message, state) function:
Wrap it in a message_handler that reacts to the passed state of userState.weight.
This function should update the data in the weight state to message.text (a user-written message).
 Use the update_data method.
Next, in the function, store all previously entered states in the data variable using state.get_data().
Use the simplified Mifflin - San Geor formula to calculate the calorie allowance
(for women or men, at your discretion). Take the data for the formula from the previously declared data variable
 using the keys age, growth and weight, respectively.
Send the result of the calculation according to the formula as a response to the user in the Telegram bot.
Finish the state machine using the finish() method.
!While writing these functions, keep in mind that they are asynchronous and all functions and methods
must be run with the await statement."""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    #gender = State()


@dp.message_handler(text='Calories')
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


"""a block for deriving the Mifflin-San Geor formula by gender"""
# @dp.message_handler(state=UserState.growth)
# async def set_weight(message,gender):
#     await gender.update_data(growth=int(message.text))
#     await message.gender('Введите свой пол (ж или м):')
#     await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    # gender = data['gender']
    # gender.lower()
    # if gender=='м':
    #     calories = 10 * weight + 6.25 * growth - 5 * age + 5
    # else:
    #     calories = 10 * weight + 6.25 * growth - 5 * age - 161
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша дневная норма калорий: {calories} ккал")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
