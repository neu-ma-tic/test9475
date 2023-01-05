import random
import re

from core import CogInit
from discord.ext import commands


class dice(CogInit):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if re.match(r"\d+[dD]\d+(\s.*)*", msg.content):
            result = []
            try:
                m = re.split("[dD\s]", msg.content, 2)
                if len(m) != 2:
                    times, side, content = m
                else:
                    times, side = m
                    content = ""
                times = int(times)
                side = int(side)
            except:
                await msg.channel.send("發生錯誤", delete_after=5)
            else:
                await msg.delete()
                for i in range(times):
                    result.append(random.randint(1, side))
                message = f"{msg.author.mention}\n"
                if content:
                    message += f"{content}"
                message += f"({times}D{side})：{sum(result)}{result}"
                await msg.channel.send(message, delete_after=10)


def setup(bot):
    bot.add_cog(dice(bot))
