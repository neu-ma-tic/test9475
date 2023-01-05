import json
import os
import re

from core import CogInit
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from redis import ConnectionPool, Redis

guildID = [719132687897591808]
pool = ConnectionPool(
    host=os.environ["REDIS_HOST"],
    port=15499,
    password=os.environ["REDIS_PASSWD"],
    decode_responses=True,
)


def get_data(key):
    r = Redis(connection_pool=pool)
    data = json.loads(r.get(key))
    return data


def set_data(key, data=None):
    r = Redis(connection_pool=pool)
    if data:
        return r.set(key, json.dumps(data))
    else:
        return r.delete(key)


class redisDB(CogInit):
    @cog_ext.cog_subcommand(base="redis", guild_ids=guildID)
    async def getkeys(self, ctx):
        r = Redis(connection_pool=pool)
        keys = r.keys()
        for i, key in enumerate(keys):
            if re.match(r"\d{18}", key):
                keys[i] = (await self.bot.fetch_user(key)).name
        await ctx.send("\n".join(keys), hidden=True)

    @cog_ext.cog_subcommand(
        base="redis",
        guild_ids=guildID,
        options=[
            create_option("key", "key", 3, True),
            create_option("data", "data", 3, False),
        ],
    )
    async def setData(self, ctx, key, data=None):
        if set_data(key, data):
            await ctx.send("修改完成", hidden=True)


def setup(bot):
    bot.add_cog(redisDB(bot))
