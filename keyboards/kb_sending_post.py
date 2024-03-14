from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import Optional
from texts.text_SendPost import *


class PostKeyboard:
    @staticmethod
    def view_ikb_post(text_tg, text_vk, text_ins):
        buttons = [
            [
                InlineKeyboardButton(text=text_tg, callback_data='send_post_tg'),
                InlineKeyboardButton(text=text_vk, callback_data='send_post_vk'),
                InlineKeyboardButton(text=text_ins, url='https://www.google.com')
            ]
        ]
        keyboards = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards
