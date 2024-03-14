from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from texts.text_MainMenu import *


class MainMenuKeyboards:
    @staticmethod
    def view_main_menu() -> ReplyKeyboardMarkup:
        kb = [
            [KeyboardButton(text=send_post), ],
            [KeyboardButton(text=quantity_of_goods)],
            [KeyboardButton(text=sale)],
            [KeyboardButton(text=admission)],
            [KeyboardButton(text=setting)]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

    @staticmethod
    def back_main_menu() -> ReplyKeyboardMarkup:
        kb = [
            [KeyboardButton(text=back)]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
