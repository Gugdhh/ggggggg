import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5846541835").split()))
OWNER_ID = int(getenv("OWNER_ID", "2028022016"))
MONGO_URL = getenv("MONGO_URL", "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0")
BOT_TOKEN = getenv("BOT_TOKEN", "5836746739:AAEuUGRiivAMlYkk4mZTxW-r8efouI2-gNk")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/b88cf163f17cddb3d08b3.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBbaGt-Rxx5DGdv-g3u2dTAQOP37Fl2ArpBiCOw8reTQ-1zCrTTtrRkEdW_Kt_i9lb4yLz70fCeEWQKOB0uhij2mJahNBIYsZdaf_iWjS7yjv2W60J3lGTx-nKKExqvqzyyzA4jLvj0kuCuxXB_9xiUJk-jXoyIjNMlJ2kedIKsI0u-5LgvZ8tKTnn6qmNrvRu8CADkFKmQ5dbcCoeW_voqKFKYEDPLdtHsQ5ETYT02FNxEnQdAuzXErSfdc1HUm_YH3yN9REkDMctWCuRNEddfCfILyLE5o24t8AW6gSZmu_rsaor8ui-tx9URFizlfqbyGlVm1Bbyq4LGoc170-7leOEpAAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
