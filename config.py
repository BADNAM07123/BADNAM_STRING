from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","24621592"))
API_HASH = getenv("API_HASH","f8316a8865477f009ab53b7126eb52c3")

BOT_TOKEN = getenv("BOT_TOKEN","7716837295:AAFieaeRlXsB2aZqdFEZfP5PyIJjNt8OY1c")
OWNER_ID = int(getenv("OWNER_ID","7931228880"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://DxLEGEND143:DxLEGEND143@dxlegend.oztipqk.mongodb.net/?retryWrites=true&w=majority&appName=DxLEGEND")
MUST_JOIN = getenv("MUST_JOIN","anya_music_sport_group")
