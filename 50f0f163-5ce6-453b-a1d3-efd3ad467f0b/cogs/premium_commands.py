from discord.ext import commands
import discord
import urllib.request
import urllib.parse
import pafy
import re
import pyshorteners
import os
import random
import requests
from utils.checks import is_patron




class premium(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    with open('/opt/virtualenvs/python3/lib/python3.8/site-packages/pafy/backend_youtube_dl.py', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace("self._dislikes = self._ydl_info['dislike_count']", "self._dislikes = self._ydl_info.get('dislike_count',0)")

    with open('/opt/virtualenvs/python3/lib/python3.8/site-packages/pafy/backend_youtube_dl.py', 'w') as file :
      file.write(filedata)


  @commands.command(aliases=['short','shrunk','shorten','redirect'])
  async def shrink(self,ctx,link=None):
    if link is None:
      await ctx.send('Bro.. what link do you want to shrink')
    aliase = random.choice(range(1,999999))
    r = requests.get(f'https://shrinkme.io/api?api=f7eef40c7d8b2bdae8d53861271b4de5373c8f63&url={link}&alias={aliase}')
    await ctx.send(f"Here's your shrunken link: {r.json()['shortenedUrl']}")

  @commands.command(aliases=['ytd'])
  async def youtube_download(self,ctx,*,video:str=None):
    if video is None:
      await ctx.send("Please specify your video to download..")
    if 'http' in video:
      message = await ctx.send('Searching for video.. <a:vibing:883535371709845515>')

      avideo = pafy.new(video)
      stream=avideo.getbestvideo(preftype="any", ftypestrict=False)

      value = stream.url_https

      shortener = pyshorteners.Shortener()
      shortened = shortener.tinyurl.short(str(value))

      embed = discord.Embed(title=f"{avideo.title}",url=str(shortened),color=discord.Color.red())
      embed.set_author(name=f'{str(avideo.author)}')
      embed.set_image(url=avideo.thumb)
      embed.set_footer(text="Click the title link to download the video",icon_url=ctx.author.display_avatar)
      await message.edit(content="video found",embed=embed)
    
    else:
      search_keyword=video.replace(" ", "+")
      html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + search_keyword)
      video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())

      message = await ctx.send('Searching for video.. <a:vibing:883535371709845515>')

      avideo=pafy.new("https://www.youtube.com/watch?v=" + video_ids[0])
      stream=avideo.getbestvideo(preftype="any", ftypestrict=False)

      value = stream.url_https

      shortener = pyshorteners.Shortener()
      shortened = shortener.tinyurl.short(str(value))

      embed = discord.Embed(title=f"{avideo.title}",url=str(shortened),color=discord.Color.red())
      embed.set_author(name=f'{str(avideo.author)}')
      embed.set_image(url=avideo.thumb)
      embed.set_footer(text="Click the title link to download the video",icon_url=ctx.author.display_avatar)
      await message.edit(content="video found",embed=embed)


      

  @commands.command(aliases=['dl_audio'])
  async def audio_download(self,ctx,*,video: str=None):
    if video is None:
      await ctx.send('dude.. what video audio do you want to download?')
    if 'http' in video:
      await ctx.send('Searching for video.. <a:vibing:883535371709845515>')

      avideo=pafy.new(video)
      audiostreams=avideo.audiostreams
      if audiostreams[1].get_filesize() >= 10000000:
        await ctx.send('Your file is wayy to thicc\nhttps://tenor.com/view/im-just-too-thick-thicc-im-big-corlhorl-corl-gif-14674944') 
      else:
        async with ctx.typing():
          await ctx.send('Downloading video... <a:CoolDoge:903409660571291729>')
          audiostreams[1].download()
        await ctx.send(content="Here's your audio file :D",file=discord.File(f'/home/runner/DiscordBot-3/{audiostreams[1].filename}'))
        os.remove((f'/home/runner/DiscordBot-3/{audiostreams[1].filename}'))

    else:
      search_keyword=video.replace(" ", "+")
      html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + search_keyword)
      video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())

      await ctx.send('Searching for video.. <a:vibing:883535371709845515>')

      avideo=pafy.new("https://www.youtube.com/watch?v=" + video_ids[0])
      audiostreams=avideo.audiostreams
      if audiostreams[1].get_filesize() >= 10000000:
        await ctx.send('Your file is wayy to thicc\nhttps://tenor.com/view/im-just-too-thick-thicc-im-big-corlhorl-corl-gif-14674944') 
      else:
        async with ctx.typing():
          await ctx.send('Downloading video... <a:CoolDoge:903409660571291729>')
          audiostreams[1].download()
        await ctx.send(content="Here's your audio file :D",file=discord.File(f'/home/runner/DiscordBot-3/{audiostreams[1].filename}'))
        os.remove((f'/home/runner/DiscordBot-3/{audiostreams[1].filename}'))

  @commands.command()
  async def e(self,ctx):
    await ctx.send('d')
        
      
#https://www.patreon.com/oauth2/authorize?response_type=code&client_id=0WT1d8kW8-C7fQgWvbIiIZ_wWbqTwzBeXy4ABbAnCmzeoThAAEVJYMtwtiGhvUmn&redirect_uri=https://www.patreon.com/join/botprogram/checkout
def setup(client):
  client.add_cog(premium(client))
