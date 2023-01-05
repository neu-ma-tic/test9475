from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl
import requests
import discord
import os

token = os.getenv("TOKEN")

def main(token):
    load_dotenv(".env")

    client = commands.Bot(command_prefix=".")

    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game("Lowicz to super dzem!"))

        print(f"{client.user.name} Logged in!")

    @client.command()
    async def ping(ctx):
        embed = discord.Embed(description=f"Ping bota wynosi {round(client.latency * 1000)}ms!",color=0x00ff00)
        
        await ctx.send(embed=embed)

    @client.command()
    async def server(ctx):
        serv =                     requests.get("https://api.minetools.eu/ping/S6S9.aternos.me/54173")
        
        await ctx.channel.send(f'Obecnie na serwerze jest online: {serv.json()["players"]["online"]}/{serv.json()["players"]["max"]} graczy, ping serwera wynosi {serv.json()["latency"]} ms')
    
    @client.command()
    async def test(ctx):
        await ctx.channel.send("Testowa wiadomosc!")

    @client.command(aliases=["cvd","koronawirus"])
    async def covid(client):
        url = requests.get("https://disease.sh/v3/covid-19/countries/POL?strict=true")

        tmp = url.json()

        today_cases = int(tmp['todayCases'])

        embed_green = discord.Embed(description=f"Dzisiaj w polsce zanotowano {today_cases} zakazen!",color=discord.Colour.from_rgb(51, 184, 76))

        embed_orange = discord.Embed(description=f"Dzisiaj w polsce zanotowano {today_cases} zakazen!",color=discord.Colour.from_rgb(181, 117, 53))

        embed_red = discord.Embed(description=f"Dzisiaj w polsce zanotowano {today_cases} zakazen!",color=discord.Colour.from_rgb(171, 39, 34))

        embed_2 = discord.Embed(description="Trwa aktualizowanie bazy zakazen!",color=discord.Colour.from_rgb(63, 129, 235))
        
        if today_cases == 0:
            await client.send(embed=embed_2)
        elif today_cases >= 2000:
            await client.send(embed=embed_red)
        elif today_cases >= 1000:
            await client.send(embed=embed_orange)
        elif today_cases >= 500:
            await client.send(embed=embed_green)

    @client.command()
    async def chomik(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/817714804646608917/832524884764131358/chomik.gif')

    @client.command()
    async def pies(ctx):
        dog_url = requests.get("https://random.dog/woof.json")

        dog_tmp = dog_url.json()

        await ctx.send(dog_tmp["url"])

    @client.command()
    async def pogoda(ctx,city):
        try:
            embed = discord.Embed(color=0x00ff00)
            embed.set_image(url=(f"https://wttr.in/{city}.png?lang=pl?m"))
            
            await ctx.send(embed=embed)
        except Exception as error:
            print(error)

    @client.command()
    async def play(ctx, url : str):
        voiceChannel = ctx.message.author.voice.channel
        voice = await voiceChannel.connect()

        ydl_opts = {
            'format': 'worstaudio/worst',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '114',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        
        src = discord.FFmpegPCMAudio("song.mp3")
        player = voice.play(src)
    
    @client.command()
    async def leave(context):
        try:
            await context.voice_client.disconnect()
        except:
            pass

    @client.command()
    async def dodaj(ctx,arg_1,arg_2):
        await ctx.send(int(arg_1) + int(arg_2))

    @client.command()
    async def odejmij(ctx,arg_1,arg_2):
        await ctx.send(int(arg_1) - int(arg_2))

    @client.command()
    async def pomnoz(ctx,arg_1,arg_2):
        await ctx.send(int(arg_1) * int(arg_2))
    
    @client.command()
    async def podziel(ctx,arg_1,arg_2):
        try:
            await ctx.send(int(arg_1) // int(arg_2))
        except ZeroDivisionError:
            await ctx.send("Nie mozesz podzielic przez zero")

    client.run(token)

if __name__ == "__main__":
    try:
        keep_alive()
        main(token)
    except:
        pass