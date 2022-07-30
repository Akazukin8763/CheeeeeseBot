import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    CLIENT_ID = os.environ['CLIENT_ID']
    BOT_NICK = os.environ['BOT_NICK']
    BOT_PREFIX = os.environ['BOT_PREFIX']
    CHANNEL = os.environ['CHANNEL'].split(',')
