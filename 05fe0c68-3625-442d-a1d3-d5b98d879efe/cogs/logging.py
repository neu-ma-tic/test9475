import discord
from discord.ext import commands, tasks
import aiofiles
import json
import paginator
import pickle

database = {
    "messages": []
}


class logging(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global database
        database = json.loads(await (await aiofiles.open('database.json', mode='r', errors='ignore')).read())
        #print(f"Database: {database}")
        try:
            self.syncDatabase.start()
        except:
            self.syncDatabase.stop()
            self.syncDatabase.start()

    @tasks.loop(seconds=1)
    async def syncDatabase(self):
        await (await aiofiles.open('database.json', mode='w+')).write(
            json.dumps(database, indent=2))

    @commands.command()
    async def db(self, ctx):
        global database
        database = json.loads(await (await aiofiles.open('database.json', mode='r', errors='ignore')).read())
        output = ""
        for msg in database['messages']:
            output += msg[0] + ":\n" + msg[1] + "\n\n"
        output += ""
        pages = paginator.TextPages(ctx, output)
        await pages.paginate()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return
        database['messages'].append((message.author.name, message.content))

    def cog_unload(self):
        self.syncDatabase.stop()
        try:
            self.client.unload_extension("cogs.logging")
        except:
            pass
        try:
            self.client.load_extension("cogs.logging")
        except:
            pass


def setup(bot):
    bot.add_cog(logging(bot))
