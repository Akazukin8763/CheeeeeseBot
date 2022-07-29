import os
from dotenv import load_dotenv

from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.environ['ACCESS_TOKEN'],
                         client_id=os.environ['CLIENT_ID'],
                         # client_secret=os.environ['CLIENT_SECRET'],
                         nick=os.environ['BOT_NICK'],
                         prefix=os.environ['BOT_PREFIX'],
                         initial_channels=os.environ['CHANNEL'].split(','))

        self.initial_modules = [
            'commands.draw'
        ]

    async def event_ready(self):
        for module in self.initial_modules:
            self.load_module(module)

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


if __name__ == '__main__':
    # https://twitchtokengenerator.com/
    load_dotenv()

    # https://twitchio.dev/en/latest/exts/commands.html#twitchio.ext.commands.Bot
    bot = Bot()
    bot.run()

    # heroku ps:scale bot=1
