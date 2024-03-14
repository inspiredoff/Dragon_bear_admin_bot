import os
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('tg_token')
STORAGE = MemoryStorage()
chat_id = os.getenv('chat_tg_id')

database_dsn = os.getenv('dsn')

vk_club_id = os.getenv('vk_club')
vk_token = os.getenv('vk_token')
vk_autoriz_params = f'access_token={vk_token}&v=5.199'