import io
from typing import BinaryIO

import PIL.Image
from PIL import Image

import vk_api
from vk_api import VkUpload
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, PhotoSize
from aiogram.methods import GetFile
import aiohttp

import texts.text_SendPost
from keyboards.kb_MainMenu import *
from keyboards.kb_sending_post import *
from states.states import *
from texts.text_SendPost import *
from texts.text_MainMenu import *

from config import *

route = Router()


# Переход из главного меню к созданию поста
@route.message(MainMenu.menu, F.text == send_post)
async def but_create_post(message: Message, state: FSMContext):
    await message.answer(create, reply_markup=MainMenuKeyboards.back_main_menu())
    await state.set_state(post.create_post)


# Ввод текста поста

@route.message(post.create_post, F.text)
async def create_post(message: Message, state: FSMContext):
    await message.answer(sending_post, reply_markup=PostKeyboard.view_ikb_post())
    await state.set_state(post.sending_post)
    await state.update_data(posts=message.text)


@route.message(post.create_post, F.photo[-1].as_('largest_photo'))
async def create_post_photo(message: Message, state: FSMContext, largest_photo: PhotoSize):
    await message.answer(sending_post, reply_markup=PostKeyboard.view_ikb_post())
    Photo_bin = io.BytesIO()
    await message.bot.download(largest_photo.file_id, Photo_bin)
    await state.set_state(post.sending_post_photo)
    await state.update_data(caption=message.caption)
    await state.update_data(photo=largest_photo)
    await state.update_data(photo_bin = Photo_bin)



# отправка текстового сообщения в тг
@route.callback_query(post.sending_post, F.data == 'send_post_tg')
async def send_post_tg(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await callback.bot.send_message(chat_id, user_data['posts'])


# отправка фотографии в тг
@route.callback_query(post.sending_post_photo, F.data == 'send_post_tg')
async def send_photo_tg(callback: CallbackQuery, state: FSMContext,):
    user_data = await state.get_data()
    await callback.bot.send_photo(chat_id, user_data['photo'].file_id, user_data['caption'])


# отправка текстового сообщения в вк
@route.callback_query(post.sending_post, F.data == 'send_post_vk')
async def send_post_vk(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_data = user_data['posts']
    vk_session = vk_api.VkApi(token=vk_token)
    vk_session.token = {'access_token': vk_token, 'expires_in': 0}
    vk = vk_session.get_api()
    vk.wall.post(owner_id=vk_club_id, message=user_data, from_group=1)


#отправка фотографии в вк
@route.callback_query(post.sending_post_photo, F.data == 'send_post_vk')
async def send_post_vk(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    photo_bin = user_data['photo_bin']
    print(photo_bin)
    f = io.BytesIO()
    image = PIL.Image.open(photo_bin)
    image.save(f, format='png')
    f.seek(0)
    capt = user_data['caption']
    vk_session = vk_api.VkApi(token=vk_token)
    vk_session.token = {'access_token': vk_token, 'expires_in': 0}
    vk = vk_session.get_api()
    addr = vk.photos.getWallUploadServer(group_id = vk_club_id[1:])
    print(addr)
    upload = vk_api.VkUpload(vk_session)
    upload_images = upload.photo_messages(photos=f)[0]
    print(upload_images)
    owner_id = upload_images['owner_id']
    # photo_id = upload_images['sizes'][-1]['url']
    photo_id = upload_images['id']
    attachment = f'photo{owner_id}_{photo_id}'
    # post = upload.photo_wall(photos=attachment,
    #                            user_id=None,
    #                            group_id=vk_club_id[1:],
    #                            caption=capt
    #                            )
    post = vk.wall.post(owner_id = vk_club_id, message=capt,attachments = attachment)
    print(post)

    # async with aiohttp.ClientSession() as session:
    #     async with session.post(addr['upload_url'],data = f'photo={img}') as responce:
    #         resp = await responce
    #         print(resp)

    # vk.photos.saveWallPhoto(group_id = vk_club_id[1:], photo = )
# @route.message(Command('start'))
# @route.message(F.texts == back)
# async def view_main_menu(message: Message, state: FSMContext):
#     await state.set_state(MainMenu.menu)
#     await message.answer(mm, reply_markup=MainMenuKeyboards.view_main_menu())
#
#
# @route.message(F.texts == send_post)
# async def back_main_menu(message: Message, state: FSMContext):
#     await state.set_state(ToMainMenu.button)
#     await message.answer(post, reply_markup=MainMenuKeyboards.back_main_menu())
#
# @route.message(F.texts)
# async def back_main_menu(message: Message, state: FSMContext):
#     await state.set_state(ToMainMenu.button)
#     await message.answer(post, reply_markup=MainMenuKeyboards.back_main_menu())
#
#
