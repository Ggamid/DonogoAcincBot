from re import T
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from config import botToken

from kb_constructor import generate_kb
from kb_constructor import hi_kb
import asyncio
from que_class import all_que
from wrk_db import check_num_of_que, update_que, add_name, add_phone_number, add_user

bot = Bot(botToken)
dp = Dispatcher(bot)

kb_list = [generate_kb(0), generate_kb(1), generate_kb(2), generate_kb(3), generate_kb(4), generate_kb(5),
           generate_kb(6), generate_kb(7), generate_kb(8), generate_kb(9), generate_kb(10), generate_kb(11),
           generate_kb(12), generate_kb(13), generate_kb(14), generate_kb(15), generate_kb(16), generate_kb(17),
           generate_kb(18)]

que_list = all_que


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):

    await message.answer(
        f'Мира тебе, {message.from_user.first_name}! Хочешь проверить свои знания истории Кавказа? Тогда жми 👉 "НАЧАТЬ ТЕСТ"',
        reply_markup=hi_kb)
    await message.delete()
    add_user(message.chat.id, False, 0)
    print(message.from_user.first_name, message.chat.id)


@dp.callback_query_handler(text="startTest")
async def test_start(callback: types.CallbackQuery):

    await callback.message.answer(f"{all_que[0].que}", reply_markup=kb_list[0])
    await callback.message.delete()
    update_que(callback.message.chat.id)



@dp.callback_query_handler()
async def test_checker(callback: types.CallbackQuery):


    count = check_num_of_que(callback.message.chat.id)
    if count <= 18:
        if callback.data == "right":

            await callback.message.answer("Верно! ✅")
            await asyncio.sleep(0)

            kb = kb_list[count]
            question = que_list[count]

            await callback.message.answer(f"{que_list[count - 1].answer}")
            await asyncio.sleep(0)

            await callback.message.answer(f"{question.que}", reply_markup=kb)
            update_que(callback.message.chat.id)
            # count_right += 1



        elif callback.data == "wrong":

            kb = kb_list[count]
            question = que_list[count]

            await callback.message.answer("Не верно ❌")
            await asyncio.sleep(0)
            await callback.message.answer(f"{que_list[count - 1].answer}")
            await asyncio.sleep(0)

            await callback.message.answer(f"{question.que}", reply_markup=kb)
            update_que(callback.message.chat.id)

            # count_wrong += 1



    elif count == 19:
        await callback.message.edit_text(que_list[-1].que)
        await callback.message.answer(f"Вы прошли тест! Количество верных ответов {0}, количество НЕверных {0}")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
