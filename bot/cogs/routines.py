from twitchio.ext import commands, routines


class Routines(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.bot.db.refresh()
        self._database_backup.start()

    def cog_unload(self):
        self._database_backup.cancel()

    @routines.routine(hours=12, wait_first=True)
    async def _database_backup(self):
        self.bot.db.commit()
        self.bot.db.refresh()


def prepare(bot: commands.Bot):
    bot.add_cog(Routines(bot))
