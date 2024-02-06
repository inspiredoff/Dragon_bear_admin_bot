import os
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('tg_token')
STORAGE = MemoryStorage()