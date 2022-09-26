import logging
import os
import sys
import time
import spamwatch
import aiohttp

import telegram.ext as tg
from redis import StrictRedis
from Python_ARQ import ARQ
from pyrogram import Client, errors
from telethon.sessions import StringSession
from telethon import TelegramClient
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


    INFOPIC = int(getenv('INFOPIC', "true"))
    EVENT_LOGS = getenv('EVENT_LOGS', "-100")
    WEBHOOK = int(getenv('WEBHOOK', "False"))
    ARQ_API_URL = getenv("ARQ_API_URL", "https://thearq.tech/")
    ARQ_API_KEY = getenv("ARQ_API_KEY", "NHYSAP-ECJHZG-PTFOPN-IEDWSW-ARQ")
    URL = getenv('URL', "")  # Does not contain token
    PORT = int(getenv('PORT', 5000))
    CERT_PATH = getenv("CERT_PATH")
    API_ID = getenv('API_ID', "7801990")
    API_HASH = getenv('API_HASH', "a9a51f02cd8a57fe80175d76ba311c03")
    DB_URI = getenv('DATABASE_URL', "postgres://vtpiiizf:PFSDpTPBAiEu3XSx2LTAWALA4_Y08X4j@jelani.db.elephantsql.com/vtpiiizf")
    DONATION_LINK = getenv('DONATION_LINK', "https://t.me/Invincible_itAchi")
    LOAD = getenv("LOAD", "").split()
    NO_LOAD = getenv("NO_LOAD", "rss").split()
    DEL_CMDS = int(getenv('DEL_CMDS', "true"))
    STRICT_GBAN = int(getenv('STRICT_GBAN', "true"))
    WORKERS = int(getenv('WORKERS', "8"))
    BAN_STICKER = getenv('BAN_STICKER',
                                 'CAADAgADOwADPPEcAXkko5EB3YGYAg')
    ALLOW_EXCL = getenv('ALLOW_EXCL', "true")
    CASH_API_KEY = getenv('CASH_API_KEY', "6UUYHJ5W9ZTV6THE")
    TIME_API_KEY = getenv('TIME_API_KEY', "JPBVSSFPZ08J")
    AI_API_KEY = getenv('AI_API_KEY', "")
    WALL_API = getenv('WALL_API', "6950f559377140a4e1594c564cdca6a3")
    SUPPORT_CHAT = getenv('SUPPORT_CHAT', "https://t.me/Ft999_Support")
    SPAMWATCH_SUPPORT_CHAT = getenv('SPAMWATCH_SUPPORT_CHAT', "https://t.me/Ft999_Support")
    SPAMWATCH_API = getenv('SPAMWATCH_API', "rpZTGYSyXF5nuPUo8~ZxQVhD0fVsq~TtyuxOj3OyUeiqX69YSg5ozCCIDN5odPpF ")
    REPOSITORY = getenv("REPOSITORY", "https://github.com/SenapiGod/Itachi-Uchiha")
    IBM_WATSON_CRED_URL = getenv("IBM_WATSON_CRED_URL", "")
    IBM_WATSON_CRED_PASSWORD = getenv("IBM_WATSON_CRED_PASSWORD", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TEMP_DOWNLOAD_DIRECTORY", "./")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", "72437c4b-682b-4a87-987f-0da8c37bc85e")
    TELEGRAPH_SHORT_NAME = getenv("TELEGRAPH_SHORT_NAME", "Aftrr")
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
    BOT_NAME = getenv("BOT_NAME", "Itachi") # Name Of your Bot.4
    BOT_USERNAME = getenv("BOT_USERNAME", "Itachiuchihaxobot") # Bot Username
    OPENWEATHERMAP_ID = getenv("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
    LOG_GROUP_ID = getenv('LOG_GROUP_ID', "-1001766047758")
    BOT_ID = getenv("BOT_ID", "1792926815")
    ERROR_LOGS = getenv("ERROR_LOGS", "-1001766047758") # Error Logs (Channel Ya Group Choice Is Yours) (-100)
    STRICT_GMUTE = int(getenv('STRICT_GMUTE', "True"))
    MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb://mongo:UaqqZHSaCd7kXrNmfwiA@containers-us-west-23.railway.app:5574")
    DEBUG = int(getenv('IS_DEBUG', "False"))
    REDIS_URL = getenv("REDIS_URL", "redis://afttr:Afttr~97@redis-18785.c60.us-west-1-2.ec2.cloud.redislabs.com:18785") # REDIS URL (From:- Heraku & Redis)
    OWNER_NAME = getenv("OWNER_NAME", "Aftrr")
