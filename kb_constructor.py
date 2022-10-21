from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from que_class import first_que, second_que, third_que, fourth_que, fifth_que
from que_class import Question
from que_class import all_que
import random

hi_kb = InlineKeyboardMarkup()
hi_btn = InlineKeyboardButton("НАЧАТЬ ТЕСТ", callback_data='startTest')
hi_kb.add(hi_btn)

first_kb = InlineKeyboardMarkup(row_width=1)
first_btn1 = InlineKeyboardButton(f"{first_que.v2}", callback_data="wrong")
first_btn2 = InlineKeyboardButton(f"{first_que.right_v1}", callback_data="right")
first_btn3 = InlineKeyboardButton(f"{first_que.v3}", callback_data="wrong")
first_kb.add(first_btn1, first_btn2, first_btn3)

second_kb = InlineKeyboardMarkup(row_width=1)
second_btn1 = InlineKeyboardButton(f"{second_que.right_v1}", callback_data="right")
second_btn2 = InlineKeyboardButton(f"{second_que.v2}", callback_data="wrong")
second_btn3 = InlineKeyboardButton(f"{second_que.v3}", callback_data="wrong")
second_kb.add(second_btn1, second_btn2, second_btn3)

third_kb = InlineKeyboardMarkup(row_width=1)
third_btn1 = InlineKeyboardButton(f"{third_que.v2}", callback_data="wrong")
third_btn2 = InlineKeyboardButton(f"{third_que.v3}", callback_data="wrong")
third_btn3 = InlineKeyboardButton(f"{third_que.right_v1}", callback_data="right")
third_kb.add(third_btn1, third_btn2, third_btn3)

fourth_kb = InlineKeyboardMarkup(row_width=1)
fourth_btn1 = InlineKeyboardButton(f"{fourth_que.v2}", callback_data="wrong")
fourth_btn2 = InlineKeyboardButton(f"{fourth_que.right_v1}", callback_data="right")
fourth_btn3 = InlineKeyboardButton(f"{fourth_que.v3}", callback_data="right")
fourth_kb.add(fourth_btn1, fourth_btn2, fourth_btn3)

fifth_kb = InlineKeyboardMarkup(row_width=1)
fifth_btn1 = InlineKeyboardButton(f"{fifth_que.v2}", callback_data="wrong")
fifth_btn2 = InlineKeyboardButton(f"{fifth_que.v3}", callback_data="wrong")
fifth_btn3 = InlineKeyboardButton(f"{fifth_que.right_v1}", callback_data="right")
fifth_kb.add(fifth_btn1, fifth_btn2, fifth_btn3)



def generate_kb(count):
    que = all_que[count]
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(f"{que.v2}", callback_data="wrong")
    btn2 = InlineKeyboardButton(f"{que.v3}", callback_data="wrong")
    btn3 = InlineKeyboardButton(f"{que.right_v1}", callback_data="right")
    btn_list = [btn1, btn2, btn3]

    btn_fr = btn_list[random.randint(0, len(btn_list)-1)]
    btn_list.remove(btn_fr)
    btn_sc = btn_list[random.randint(0, len(btn_list)-1)]
    btn_list.remove(btn_sc)
    btn_thr = btn_list[0]

    markup.add(btn_fr, btn_sc, btn_thr)
    return markup
