
from discord.ext import commands

token = 'Nzk0MzEzNjYwNDYxNjEzMDY4.X-5APg.l8i4f-ibB5Xdivgbwp_z-c89pYs'
bot = commands.Bot('!')

@bot.command()
async def test(ctx):
  await ctx.send('test')

bot.run(token)