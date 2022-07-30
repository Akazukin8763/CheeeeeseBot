import glob

from twitchio.ext import commands

from config import Config


class Bot(commands.Bot):

    def __init__(self):
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
