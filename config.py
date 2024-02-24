from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", 22980504))
API_HASH = getenv("API_HASH", b85ecdd508ae39f4e64a08e9a4f9c48d)

BOT_TOKEN = getenv("BOT_TOKEN", "6686420045:AAH4xpOg3cfDtRK4TP7usMe7Mzl3rmej8dw")
LOG_ID = int(getenv("LOG_ID", ""))

MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://tonyxbot:tonyxbot@cluster0.bojrxzg.mongodb.net/?retryWrites=true&w=majority)
SUDO_USER = list(map(int, getenv("SUDO_USER", 5366891026).split()))
