import discord
from discord.ext import commands
import youtube_dl

#
class music(commands.Cog):
    def __init__(self, client):
       self.client = client

      #makes bot join voice channel
    @commands.command()
    async def join(self,ctx):   
        # check if voice channel is empty
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        # check if bot is in voice channel 
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)  

       
       # disconnects bot
    @commands.command()
    async def disconnect(self,ctx): 
        await ctx.voice_client.disconnect()    
        
    @commands.command()
    async def play(self,ctx,url):
        global queue
        
        # play new song
        ctx.voice_client.stop()
        
        # declarations
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        # streams audio
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

            #plays audio in vc
            vc.play(source)


      # pauses music
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send('Paused')

    # resumes music
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send('resume')

    @commands.command()
    async def  queue(ctx,*, url):
      global queue

      queue.append(url)
      await ctx.send(f'`{url}` added to queue!')

  


#adds client as cog
def setup(client):
    client.add_cog(music(client))