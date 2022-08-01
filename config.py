import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    CLIENT_ID = os.environ['CLIENT_ID']
    BOT_NICK = os.environ['BOT_NICK']
    BOT_PREFIX = os.environ['BOT_PREFIX'].split(',')
    CHANNEL = os.environ['CHANNEL'].split(',')

    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_OPTIONS = os.environ['DB_OPTIONS']
