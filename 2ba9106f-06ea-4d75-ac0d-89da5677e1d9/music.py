import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def _init_(self,client):
    self.client = client
  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None :
      await ctx.send("You are not in a voice channel :p")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connec()
    else:
      await ctx.voice_client.move_to(voice_channel)
  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self,ctx,url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = ('before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn')
    YDL_OPTIONs = {'format':"bestaudio"}
    vc = ctx.voice)_client

    with youtube_dl.YoutubeDL(YDL_OPTIONs) as yet:
      info = ydl.extract_info(url, download= False)
      url2 = info ['formats'][0]['url']
      source = await discord.FFmegOpusAudio.from_probr(url2, ** FFMPEG_OPTIONS)
      vc.play(source)
  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause()
    await ctx.send("paused😑")
  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume()
    await ctx.send("resume😮")



def setup(client):
  client.add_cog(music(client))
  