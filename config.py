import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24894984"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4956e23833905463efb588eb806f9804")

#Database 
DB_URI = os.environ.get("DB_URI", "")
