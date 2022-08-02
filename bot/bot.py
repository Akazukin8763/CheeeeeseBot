import glob

from twitchio.ext import commands

from config import Config
from database import Database


class Bot(commands.Bot):

    __slots__ = ['db', ]

    def __init__(self):
        self.db = Database(self)

        super().__init__(token=Config.ACCESS_TOKEN,
                         client_id=Config.CLIENT_ID,
                         nick=Config.BOT_NICK,
                         prefix=Config.BOT_PREFIX,
                         initial_channels=Config.CHANNEL)

    def setup(self):
        print("Running setup ...")

        for cog in glob.glob("bot/cogs/**/*.py", recursive=True):
            self.load_module(
                cog.replace("\\", ".").replace("/", ".").removesuffix(".py")
            )

        print("Setup complete.")

    def run(self):
        self.setup()

        print("Running bot ...")
        super().run()

    async def close(self):
        # 關閉排程
        self.get_cog("Routines").cog_unload()
        # 關閉資料庫連結
        self.db.close()

        print("Shut down ...")
        await super().close()

    async def event_ready(self):
        print(f"Logged in as <{self.nick}>")
        print(f"User ID is <{self.user_id}>")

    async def event_message(self, message):
        if message.echo:
            return
        print(f'{message.timestamp}: {message.author.name} - {message.content}')
        await self.handle_commands(message)

    async def event_error(self, error: Exception, data: str = None):
        print(f"Error: {error}")

    async def event_command_error(self, context: commands.Context, error: Exception):
        print(f"Error: {error}")
