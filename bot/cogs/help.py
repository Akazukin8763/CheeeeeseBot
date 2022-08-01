from twitchio.ext import commands


class Help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="指令", aliases=["command", "commands", "help"])
    @commands.cooldown(rate=1, per=30, bucket=commands.Bucket.channel)
    async def _help(self, ctx: commands.Context):
        cmds = []
        for cmd in self.bot.commands.values():
            cmds.append(f"[ {' | '.join([cmd.name, *(cmd.aliases or [])])} ]")
        await ctx.reply("【 StinkyGlitch 】" + "、".join(cmds))


def prepare(bot: commands.Bot):
    bot.add_cog(Help(bot))
