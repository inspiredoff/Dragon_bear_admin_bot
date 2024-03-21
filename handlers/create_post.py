import io

import PIL.Image

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, PhotoSize
import requests

from keyboards.kb_MainMenu import *
from keyboards.kb_sending_post import *
from states.states import *
from texts.text_SendPost import *
from texts.text_MainMenu import *

from config import *

route = Router()


# Переход из главного меню к созданию поста
@route.message(F.text == send_post)
async def but_create_post(message: Message, state: FSMContext):
    await message.answer(create, reply_markup=MainMenuKeyboards.back_main_menu())
    await state.set_state(post.create_post)


# Ввод текста поста


@route.message(post.create_post, F.text)
async def create_post(message: Message, state: FSMContext):
    await message.answer(
        sending_post,
        reply_markup=PostKeyboard.view_ikb_post(send_tg, send_vk, send_ins),
    )
    await state.set_state(post.sending_post)
    await state.update_data(posts=message.text)


@route.message(post.create_post, F.photo[-1].as_("largest_photo"))
async def create_post_photo(
    message: Message, state: FSMContext, largest_photo: PhotoSize
):
    await message.answer(
        sending_post,
        reply_markup=PostKeyboard.view_ikb_post(send_tg, send_vk, send_ins),
    )
    Photo_bin = io.BytesIO()
    await message.bot.download(largest_photo.file_id, Photo_bin)
    await state.set_state(post.sending_post_photo)
    await state.update_data(caption=message.caption)
    await state.update_data(photo=largest_photo)
    await state.update_data(photo_bin=Photo_bin)


# отправка текстового сообщения в тг
@route.callback_query(post.sending_post, F.data == "send_post_tg")
async def send_post_tg(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await callback.bot.send_message(chat_id, user_data["posts"])
    user_data["state_tg"] = ok
    await callback.answer(
        reply_markup=PostKeyboard.view_ikb_post(
            user_data["state_tg"], user_data["state_vk"], user_data["state_ins"]
        )
    )


# отправка фотографии в тг
@route.callback_query(post.sending_post_photo, F.data == "send_post_tg")
async def send_photo_tg(
    callback: CallbackQuery,
    state: FSMContext,
):
    user_data = await state.get_data()
    await callback.bot.send_photo(
        chat_id, user_data["photo"].file_id, caption=user_data["caption"]
    )
    user_data["state_tg"] = ok
    await callback.answer(
        reply_markup=PostKeyboard.view_ikb_post(
            user_data["state_tg"], user_data["state_vk"], user_data["state_ins"]
        )
    )


# отправка текстового сообщения в вк
@route.callback_query(post.sending_post, F.data == "send_post_vk")
async def send_post_vk(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_data = user_data["posts"]
    vk_session = vk_api.VkApi(token=vk_token)
    vk_session.token = {"access_token": vk_token, "expires_in": 0}
    vk = vk_session.get_api()
    vk.wall.post(owner_id=vk_club_id, message=user_data, from_group=1)
    user_data["state_vk"] = ok
    await callback.answer(
        reply_markup=PostKeyboard.view_ikb_post(
            user_data["state_tg"], user_data["state_vk"], user_data["state_ins"]
        )
    )


# отправка фотографии в вк
@route.callback_query(post.sending_post_photo, F.data == "send_post_vk")
async def send_post_vk(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    photo_bin = user_data["photo_bin"]
    print(photo_bin)
    f = io.BytesIO()
    image = PIL.Image.open(photo_bin)
    image.save(f, format="png")
    f.seek(0)
    print(type(f.getvalue()))
    capt = user_data["caption"]
    files = {
        "group_id ": (None, vk_club_id),
        "access_token": (None, vk_token),
        "v": (None, "5.199"),
    }
    metod = "photos.getWallUploadServer"
    url = f"https://api.vk.ru/method/{metod}?"
    response = requests.post(url=url, files=files, verify=False)
    data = response.json()
    # contents = open(r'C:\Users\Артем\Downloads\Telegram Desktop\photo_2024-02-13_23-03-32.jpg', 'rb')
    # print(contents)
    files = {
        "photo": ("image.png", f, "image/png"),
    }
    response = requests.post(
        url=data["response"]["upload_url"], files=files, verify=False
    )
    data = response.json()
    print(response.json())

    files = {
        "access_token": (None, vk_token),
        "photo": (None, data["photo"]),
        "server": (None, data["server"]),
        "hash": (None, data["hash"]),
        "v": (None, "5.199"),
    }
    metod = "photos.saveWallPhoto"
    response = requests.post(
        "https://api.vk.com/method/photos.saveWallPhoto", files=files, verify=False
    )
    data = response.json()
    print(response.json())
    owner_id = data["response"][0]["owner_id"]
    id = data["response"][0]["id"]
    files = {
        "owner_id": (None, vk_club_id),
        "from_group": (None, "1"),
        "access_token": (None, vk_token),
        "message": (None, capt),
        "attachments": (None, f"photo{owner_id}_{id}"),
        "v": (None, "5.199"),
    }
    response = requests.post(
        "https://api.vk.com/method/wall.post", files=files, verify=False
    )
    print(response.json())
    user_data["state_vk"] = ok
    await callback.answer(
        reply_markup=PostKeyboard.view_ikb_post(
            user_data["state_tg"], user_data["state_vk"], user_data["state_ins"]
        )
    )
