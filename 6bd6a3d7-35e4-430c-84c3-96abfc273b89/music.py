import discord
from discord.ext import commands
import youtube_dl 

client = commands.Bot(command_prefix='$')
 
class music(commands.Cog):
    self.client = client
    def __init__(self, client):
        

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("אתה לא בחדר ידפוק")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
           await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format' : "bestaudio"}
        VC = ctx.voice_client

        with youtube_dl.Youtube_dl(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['format'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, 
            **FFMPEG_OPTIONS)
            vc.play(source)

       
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("נעצרתי יזין")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("יאללה ממשיך לשיר")    
                      
def setup(client):
   client.add_cog(music(client))
