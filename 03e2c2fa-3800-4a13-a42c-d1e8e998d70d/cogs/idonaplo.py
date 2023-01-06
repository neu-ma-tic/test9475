import discord
from discord.ext import commands
import datetime
import pytz

class idonaplo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.enabled = False

    @commands.command()
    async def belepes(self, ctx):
        await ctx.message.delete()
        enabled = True
        d1 = datetime.datetime.now().astimezone(pytz.timezone("Europe/Budapest"))
        d2 = datetime.date.today()
        mbed = discord.Embed(
          colour = (discord.Colour.magenta()),
          title = f'CSSOS Szolgálati időnapló - {ctx.message.author.name}',
          description = f"Szolgálatba lépett **{d2.year}.{d2.month}.{d2.day}**-án/én **{d1.hour}** óra **{d1.minute}** perckor.\n **Jelenleg szolgálatban van** "
        )
        message = await ctx.send(embed = mbed)

        def check(m):
          return m.content == "!kilepes"

        while enabled:
          msg = await self.bot.wait_for("message", check=check)
          if msg.author == ctx.author:
            d3 = datetime.datetime.now().astimezone(pytz.timezone("Europe/Budapest"))
            d4 = datetime.date.today()
            if d1.minute > d3.minute :
              new_mbed = discord.Embed(
                colour = (discord.Colour.magenta()),
                title = f'CSSOS Szolgálati időnapló - {ctx.message.author.name}',
                description = f"Szolgálatba lépett **{d2.year}.{d2.month}.{d2.day}**-án/én **{d1.hour}** óra **{d1.minute}** perckor\n Leadta a szolgálatot **{d4.year}.{d4.month}.{d4.day}**-án/én **{d3.hour}** óra **{d3.minute}** perckor.\n**Összesen {d3.hour - d1.hour - 1} órát és {d3.minute + 60 - d1.minute} percet volt szolgálatban!** "
              )
              await message.edit(embed = new_mbed)
              return

            else :
              new_mbed = discord.Embed(
                colour = (discord.Colour.magenta()),
                title = f'CSSOS Szolgálati időnapló - {ctx.message.author.name}',
                description = f"Szolgálatba lépett **{d2.year}.{d2.month}.{d2.day}**-án/én **{d1.hour}** óra **{d1.minute}** perckor\n Leadta a szolgálatot **{d4.year}.{d4.month}.{d4.day}**-án/én **{d3.hour}** óra **{d3.minute}** perckor.\n**Összesen {d3.hour - d1.hour} órát és {d3.minute - d1.minute} percet volt szolgálatban!** "
              )
              await message.edit(embed = new_mbed)
              return


    @commands.command()
    async def kilepes(self, ctx):
      await ctx.message.delete()
      self.enabled = False

def setup(client):
  client.add_cog(idonaplo(client))