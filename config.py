from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", 29250051))
API_HASH = getenv("API_HASH", "5a8e5c861695595f38ec59b6e0a0f6cc")

BOT_TOKEN = getenv("BOT_TOKEN", "6686420045:AAH4xpOg3cfDtRK4TP7usMe7Mzl3rmej8dw")
LOG_ID = int(getenv("LOG_ID", ""))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://tonyxbot:tonyxbot@cluster0.bojrxzg.mongodb.net/?retryWrites=true&w=majority")
SUDO_USER = list(map(int, getenv("SUDO_USER", 5366891026).split()))
