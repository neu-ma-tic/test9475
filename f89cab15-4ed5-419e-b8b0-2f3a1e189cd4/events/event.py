import random
import re

from discord.ext import commands

from core import CogInit, read_yaml


def choice_reply(item):
    reply = read_yaml("config")["event"][item]
    return random.choices(list(reply.keys()), weights=list(reply.values()))[0]


SAO = re.compile(
    "星[\~` ]*[爆暴報]|c8763|star(\s)*burst|(10|十)(\s)*(秒|sec)|((星光)|(西瓜)|(\N{WATERMELON})) *([流榴][槤蓮連]) *[擊雞機(\N{ROOSTER})]|[桐銅]([谷古鼓][和核])?[人仁]|kirito|當我.?.?第[二2].|艾恩葛朗特"
)


class Events(CogInit):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if not msg.author.bot:
            # mention
            if self.bot.user in msg.mentions:
                await msg.reply(choice_reply("mention"))

            # 星爆
            if SAO.search(msg.content.lower()):
                await msg.add_reaction("\N{THUMBS DOWN SIGN}")

            # emoji
            if re.search(
                r"([獵打揍殺屠砍幹尻肏淦弒]|hit|slay|attack|kill)[\s\n\W]*(龍|竜|多拉貢|dragon)", msg.content, re.I
            ) and not await self.bot.is_owner(msg.author):
                await msg.reply("<:092:819621685010366475>" * 3)
            if re.search(r"([＼／\\\|/l]\s?){3}|上香|:021:|:034:|:GIF009:", msg.content):
                await msg.reply(choice_reply("pray"))

            # 圖片
            if re.search(r"[rR啊阿ㄚ痾]{4,}", msg.content):
                await msg.reply(choice_reply("rrr"), delete_after=7)
            if "虫合" in msg.content or "蛤" in msg.content:
                await msg.channel.send(choice_reply("what"), delete_after=7)
            if re.search(r"[uhe]m{3,}|\N{THINKING FACE}", msg.content, re.I):
                await msg.channel.send(choice_reply("emm"), delete_after=10)
            if "並沒有" in msg.content or "不要瞎掰" in msg.content:
                await msg.channel.send(choice_reply("it's_not"), delete_after=7)
            if re.search(r"[^不]*好耶", msg.content):
                await msg.channel.send(choice_reply("yeah"), delete_after=7)
            if re.match(r"派[耶欸ㄟ]", msg.content):
                await msg.channel.send(choice_reply("pie"), delete_after=7)
            if re.match(r"[在再應因已以玩完道到字自]啦", msg.content):
                await msg.channel.send(choice_reply("again"), delete_after=7)
            if re.match(r"hello|哈[囉嘍]", msg.content, re.I):
                await msg.reply(choice_reply("hello"), delete_after=5)

    @commands.command()
    async def programming(self, ctx):
        await ctx.send(choice_reply("programming"), delete_after=7)
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        else:
            try:
                await ctx.message.delete()
            except:
                pass
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("缺少必要參數，請確認指令使用方法", delete_after=5)
            elif isinstance(error, commands.BadArgument):
                await ctx.send("參數類別轉換錯誤，請確認是否輸入正確", delete_after=5)
            else:
                await ctx.send(f"發生例外錯誤：{error}", delete_after=10)


def setup(bot):
    bot.add_cog(Events(bot))
