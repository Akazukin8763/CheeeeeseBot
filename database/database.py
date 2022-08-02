from pymongo import MongoClient, UpdateOne
from pymongo.server_api import ServerApi

from twitchio.ext import commands

from config import Config


class Database:

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        self.client = MongoClient(
            "mongodb+srv://%s:%s@%s/%s" % (Config.DB_USERNAME, Config.DB_PASSWORD, Config.DB_HOST, Config.DB_OPTIONS),
            server_api=ServerApi('1')
        )

        self._channels = {}

    def close(self):
        self.client.close()

    def refresh(self) -> None:
        # 紀錄每個頻道的資料庫
        for db in self.client.list_database_names():
            if db == "admin" or db == "local":
                continue

            # 紀錄每個頻道資料庫中的每個資料表
            data = {}
            for coll in self.client[db].list_collection_names():
                # 將資料表的內容轉為 dict
                docs = {}
                for doc in self.client[db][coll].find({}, {"_id": 0}):
                    docs[doc["user"]] = {k: v for k, v in doc.items() if k != "user"}

                data[coll] = docs

            self._channels[db] = data

    def commit(self) -> None:
        # 寫入每個頻道的資料庫
        for db in self.client.list_database_names():
            if db == "admin" or db == "local":
                continue

            # 寫入每個頻道資料庫中的每個資料表
            for coll in self.client[db].list_collection_names():
                updates = []

                for user, data in self._channels[db][coll].items():
                    if data.get("update"):
                        updates.append(UpdateOne(filter={"user": user},
                                                 update={"$set": {k: v for k, v in data.items() if k != "update"}},
                                                 upsert=True))

                if len(updates) > 0:
                    self.client[db][coll].bulk_write(updates)

        # 將資料表重新讀出
        self.refresh()

    def get_doc(self, channel: str, doc_name: str):
        return self._channels[channel][doc_name]

    def set_doc(self, channel: str, doc_name: str, doc: dict):
        self._channels[channel][doc_name] = doc
