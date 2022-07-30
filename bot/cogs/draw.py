import random

from twitchio.ext import commands


class Draw(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="早餐單")
    async def _breakfast(self, ctx: commands.Context):
        # 早餐單
        吐司 = ["草莓吐司", "巧克力吐司", "奶油吐司", "花生吐司", "奶酥厚片",
               "煎蛋吐司", "培根蛋吐司", "火腿蛋吐司", " StinkyGlitch 蛋吐司", "薯餅蛋吐司",
               "鮪魚蛋吐司", "燻雞蛋吐司", "豬肉蛋吐司", "卡拉雞蛋吐司"]

        厚片 = ["草莓厚片", "巧克力厚片", "奶油厚片", "花生厚片", "奶酥厚片"]

        蛋餅 = ["原味蛋餅", "蔬菜蛋餅",
               "玉米蛋餅", "培根蛋餅", "火腿蛋餅", " StinkyGlitch 蛋餅", "熱狗蛋餅", "薯餅蛋餅",
               "鮪魚蛋餅", "燻雞蛋餅", "豬肉蛋餅", "卡拉雞蛋餅"]

        漢堡 = ["豬肉蛋堡", "牛肉蛋堡", "燻雞蛋堡", "卡拉雞腿蛋堡"]

        鐵板麵 = ["鐵板麵", "鐵板麵加蛋"]

        小點 = ["荷包蛋", "德式香腸", "蘿蔔糕", "蔥抓餅", "蔥抓餅加蛋",
               "熱狗", "煎餃", "鍋貼", "雞塊", "脆薯", "薯餅"]

        飲料 = ["紅茶", "奶茶", "豆漿", "咖啡牛奶", "豆漿紅茶", "鮮奶茶", "柳橙汁", "牛奶", "巧克力牛奶"]

        # 隨機抽早餐
        breakfast = []

        # 主食為何
        if random.randint(1, 10) <= 2:  # 是否吃鐵板麵，機率為 20%
            breakfast.extend(random.choices(鐵板麵, k=1))
        else:  # 不以鐵板麵當主食
            main = [吐司, 厚片, 蛋餅, 漢堡]
            random.shuffle(main)

            # 不重複總類點 1 ~ 3 樣
            rnd = random.randint(1, 20)
            if rnd <= 15:  # 75% 點一樣
                choices = main[0:1]
            elif rnd <= 19:  # 20% 點兩樣
                choices = main[0:2]
            else:  # 5% 點三樣
                choices = main[0:3]

            # 各總類隨機選一種
            for choice in choices:
                random.shuffle(choice)
                breakfast.append(choice[0])

        # 小點是否搭配
        if random.randint(1, 10) <= 7:  # 是否加點小點，機率為 70%
            side = 小點
            random.shuffle(side)

            # 不重複小點點 1 ~ 3 樣
            rnd = random.randint(1, 20)
            if rnd <= 12:  # 60% 點一樣
                breakfast.extend(side[0:1])
            elif rnd <= 19:  # 35% 點兩樣
                breakfast.extend(side[0:2])
            else:  # 5% 點三樣
                breakfast.extend(side[0:3])

        # 一定配飲料
        breakfast.extend(random.choices(飲料, k=1))

        # 統整早餐單印出
        breakfast_list = "、".join(breakfast)

        if random.randint(1, 100) <= 99:
            await ctx.reply("【 StinkyGlitch 】" + breakfast_list)
        else:
            await ctx.reply("【 StinkyGlitch 】不吃")


def prepare(bot: commands.Bot):
    bot.add_cog(Draw(bot))
