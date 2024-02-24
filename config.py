from os import getenv

# Retrieve API_ID environment variable
api_id = getenv("API_ID", 29250051)

# Check if API_ID is None or empty
if not api_id:
    print("ERROR: API_ID environment variable is not set.")
    exit(1)

# Convert API_ID to integer
try:
    API_ID = int(api_id)
except ValueError:
    print("ERROR: API_ID must be a valid integer.")
    exit(1)
API_HASH = getenv("API_HASH", "5a8e5c861695595f38ec59b6e0a0f6cc")

BOT_TOKEN = getenv("BOT_TOKEN", "6686420045:AAH4xpOg3cfDtRK4TP7usMe7Mzl3rmej8dw")
LOG_ID = int(getenv("LOG_ID", "-1001887112549"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://tonyxbot:tonyxbot@cluster0.bojrxzg.mongodb.net/?retryWrites=true&w=majority")
SUDO_USER = list(map(int, getenv("SUDO_USER", "5366891026").split()))
