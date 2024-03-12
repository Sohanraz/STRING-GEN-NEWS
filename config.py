from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv.get("API_ID" ,"29219170"))
API_HASH = getenv.get("API_HASH", "12d6648ede66e1ef31d9c455317ee09d")

BOT_TOKEN = getenv.get("BOT_TOKEN", "6282594199:AAFXICV7X6uAOH2nELP3IruuU5o5TFylcBM")
MONGO_DB_URI = getenv.get("MONGO_DB_URI", "mongodb+srv://Sohanrazz:Sohanrazz@cluster0.wbcmn82.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv.get("OWNER_ID", "5897793065"))
SUPPORT_CHAT = getenv.get("SUPPORT_CHAT", "https://t.me/Developerr_Bots_Support")
