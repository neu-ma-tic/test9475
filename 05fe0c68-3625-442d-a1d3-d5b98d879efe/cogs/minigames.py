from discord.ext import commands, tasks
import random


class minigames(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def roll(self, ctx):
        #todo Würfel
        würfel = random.randint(1,6)
        await ctx.channel.send(f":game_die: Der Würfel ist auf {würfel} gefallen.")

    @commands.command()
    async def roulette(self, ctx):
        #todo Kleines Casiono
        return

    def cog_unload(self):
        print("test2")
        try:
            self.client.unload_extension("cogs.minigames")
        except:
            pass
        try:
            self.client.load_extension("cogs.minigames")
        except:
            pass

def setup(bot):
    bot.add_cog(minigames(bot))