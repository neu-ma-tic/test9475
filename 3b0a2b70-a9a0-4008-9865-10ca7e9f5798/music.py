import discord
from discord.ext import commands
import youtube_dl

class music(commands.cog):
  def __innit__(self, client):
    self.client = client
    @commands.command()
    async def join(self,ctx):
      if ctx.author.voice is None:
        await ctx.send("You're not in a VC you fucking monkey bitch.")
    voice_channel = ctx.author.voice.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
      else:
        wait
    
    

    

def setup(client):
  client.add_cog(music(client))


