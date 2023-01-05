import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
       await ctx.send("You're not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
       await voice_channel.connect()
    else:
       await ctx.voice_client.move_to(voice_channel)
  
  @commands.command()
  async def disconnect(self,ctx):

def setup(client):
  client.add_cog(music(client))