from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from texts.text_SendPost import *


class PostKeyboard:
    @staticmethod
    def view_ikb_post():
        buttons = [
            [
                InlineKeyboardButton(text=send_tg, callback_data='send_post_tg'),
                InlineKeyboardButton(text=send_vk, callback_data='send_post_vk'),
                InlineKeyboardButton(text=send_ins, url='https://www.google.com')
            ]
        ]
        keyboards = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards
