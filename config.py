import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5846541835").split()))
OWNER_ID = int(getenv("OWNER_ID", "5868178288"))
MONGO_URL = getenv("MONGO_URL", "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0")
BOT_TOKEN = getenv("BOT_TOKEN", "5856143550:AAGdqv_ZwCcMC3r9Vf9m6da-XggJ9rY_rLA")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/b88cf163f17cddb3d08b3.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAAIb8lB23fK1AMql9h4LI0fIP1jKdkEPbIME0UobRSkoGL_xeZwWkaXhAl0_jX0wMLLxO-lmNivhZHrjqYlv3APyAHPr6nlSnbP_BEU4Ace8Y6C50kY3xlrMpyFY4PCrwn8IFtuuwkNxE1mGIicMI-o2mTN3eHtAsz1kDi_l23r-7RBIlOIhbKc2wwBL6imCLGgI4I7Ba_NaJmI2XlpIed2GgDxtmfS0zQK1eOKd2PtoT62Z9tK6emx5Aq3n9xM8h_fBQcLAnW4B0teP0oAQz0zpIwN25Oyz96uKqVLJXgMHsgCD5qTrT4H1gd8Hwsr317ZtL0_zXvTVrKU4-tid7-gAAAAFdxUtwAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
