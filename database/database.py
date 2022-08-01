import pymongo
from pymongo.server_api import ServerApi

from twitchio.ext import commands

from config import Config


class Database:

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        self.client = pymongo.MongoClient(
            "mongodb+srv://%s:%s@%s/%s" % (Config.DB_USERNAME, Config.DB_PASSWORD, Config.DB_HOST, Config.DB_OPTIONS),
            server_api=ServerApi('1')
        )

    def close(self):
        self.client.close()

    def __getattr__(self, name: str):
        return self.client[name]

    def __getitem__(self, name: str):
        return self.client[name]
