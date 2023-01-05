import discord
from discord.ext import commands
from random import randrange

class Meme(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  # @commands.Cog.listener()
  # async def on_ready(self):
  #   print("Bot is online.")

  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong Pong Pong!')

  @commands.command()
  async def Đức(self, ctx):
    await ctx.send('Ấu Dâm Hàn Quốc <:daxem:767391655161757698>')

  @commands.command()
  async def ỏ(self, ctx, name):
      await ctx.send('ỏoooooo. Love u ' +name)

  @commands.command()
  async def thapnhang(self, ctx):
    await ctx.send('<:830102437083086888:879378105364541440>')

  @commands.command()
  async def ailàbồĐức(self, ctx):
    await ctx.send(f'Đức có bồ hả :v')

  @commands.command()
  async def xinso(self, ctx):
    await ctx.send(randrange(10))
  
def setup(client):
  client.add_cog(Meme(client))