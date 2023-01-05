import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
import youtube_dl
import asyncio
import urllib.parse
import urllib.request
import re
from django.core.validators import URLValidator, ValidationError
from itertools import cycle

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your bot is ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix=";")
status = cycle(['your Mom','your Dad', 'your emotions'])


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(type=discord.ActivityType.watching, name="you in your sleep."))

    print(str(client.user) + " is connected")


@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))


# DONE
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="arrivee-depart")

    embed = discord.Embed(title="Nouvel Arrivant",
                          url="https://discord.com/channels/664247730113085445/791015412438794280",
                          description=member.mention + " viens de **rejoindre** le serveur.",
                          color=0x10FF10)

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name=member.name, url="https://discord.com/channels/664247730113085445/791015412438794280",
                     icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="UID", value=str(member.id), inline=False)
    embed.add_field(name="Nametag", value=str(member.name) + "#" +
                       str(member.discriminator), inline=False)
    embed.add_field(name="Crée le", value=str(member.created_at), inline=False)

    await channel.send(embed=embed)


# DONE
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="arrivee-depart")

    embed = discord.Embed(title="Nouveau Depart",
                          url="https://discord.com/channels/664247730113085445/791015412438794280",
                          description=member.mention + " viens de **quitter** le serveur.",
                          color=0xFF0000)

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name=member.name, url="https://discord.com/channels/664247730113085445/791015412438794280",
                     icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="UID", value=str(member.id), inline=False)
    embed.add_field(name="Nametag", value=str(member.name) + "#" +
                       str(member.discriminator), inline=False)
    embed.add_field(name="Crée le", value=str(member.created_at), inline=False)

    await channel.send(embed=embed)


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    responses = []
    f = open("responses.txt", "r")
    for line in f.readlines():
        sentence, response = line.split(sep="==")
        responses.append((sentence.strip().lower(), response.strip()))

    for response in responses:
        if response[0] in message.content.lower():
            await message.channel.send(response[1])

    await client.process_commands(message)


"""@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("Vous n'avez pas les droits necessaires pour cette action.")"""


# DONE
@client.command(help="'$ping' gives the current bot's latency. Use if you suspect some lag is from the bot itself.")
async def ping(ctx):
    await ctx.send("Pong! ... " + str(round(client.latency * 1000)) + "ms")


# DONE
@client.command(help="'$clear n' with n being an integer, deletes the latest n messages in the channel it is written "
                     "in. The command deletes the command message itself as well as n other messages, effectively "
                     "deleting n+1 messages.")
@commands.has_role('admin')
async def clear(ctx, num):
    msgs = await ctx.history(limit=int(num) + 1).flatten()
    for msg in msgs:
        await msg.delete()


# DONE
@client.command(help="'$rename old-channel new-channel' renames the channel which name is in the first parameters, "
                     "with a new name in the second parameter.")
@commands.has_role('admin')
async def rename(ctx, name, *newargs):
    channel = discord.utils.get(ctx.guild.text_channels, name=name)
    print(" ".join(newargs))
    await channel.edit(name=" ".join(newargs))


# DONE
@client.command(help="';created Name#2509' writes the date of creation of the provided discord account. The account"
                     "in question needs to be in the server in which the command is executed for it to work. "
                     "';created ID' writes the date of creation of the provided ID's discord account. The account "
                     " in question does not need to be in the server in which the command is executed for it to work.")
async def created(ctx, *, args):
    if "#" in args:
        username, userdescrim = args.strip().split("#")
        userid = discord.utils.get(ctx.guild.members, name=username, discriminator=userdescrim).id
        user = client.get_user(userid)
        await ctx.send(user.created_at)
    else:
        user = client.get_user(int(args.strip()))
        await ctx.send(user.created_at)


queue = []
Skip = False


# DONE
@client.command(help="'$play https://www.youtube.com/watch?v=oWidxg_YCIU' connects to the voice channel the user is"
                     " connected to, and plays the audio from the youtube url.\n'$play Dabin - Bloom' connects "
                     "to the voice channel the user is connected to, and plays the audio from the first search result"
                     " on youtube for the title provided.", aliases=["p"])
async def play(ctx, *, url):
    global queue, Skip

    validate = URLValidator()
    isurl = True
    try:
        validate(url)
    except ValidationError:
        isurl = False

    if isurl:
        if "list" in url:
            await ctx.send(
                "Je n'accepte pas les playlist ! C'est trop long ! Il faut de la place pour tout le monde :D. "
                "Si tu veux tout de même écouter cette musique, essaye de me donner un lien qui n'est pas une "
                "playlist.")
            return
        queue.append(url)
    else:
        query_string = urllib.parse.urlencode({'search_query': url})
        htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
        url1 = 'http://www.youtube.com/watch?v=' + search_results[0]
        if "list" in url1:
            ctx.send("Je n'accepte pas les playlist ! C'est trop long ! Il faut de la place pour tout le monde :D. "
                     "Si tu veux tout de même écouter cette musique, essaye de me donner un lien qui n'est pas une "
                     "playlist")
            return
        queue.append(url1)

    channel = ctx.author.voice.channel

    vc = ""
    alreadyin = False
    members = channel.members
    for mem in members:
        if mem.id == 790861880809226260:
            alreadyin = True

    if not alreadyin:
        vc = await channel.connect()
    else:
        vc = client.voice_clients[0]

    while True:
        Skip = False
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            if len(queue) > 5:
                await ctx.send(
                    "La file d'attente est pleine. Il est impossible d'ajouter des musiques supplémentaires. "
                    "Veuillez vider la liste d'attente ou bien patienter que les musiques de la liste soient "
                    "jouées.")
                queue = queue[:-1]
                return
            await ctx.send("Ajoutée a la file (" + str(len(queue)) + "/5)")
            return

        await ctx.send("Chargement de la musique en cours")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([queue[0]])
            except youtube_dl.utils.DownloadError:
                vc.disconnect()

        name = ""
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                os.rename(file, "song.mp3")

        vc.play(discord.FFmpegPCMAudio("song.mp3"))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.2

        nname = name.rsplit("-", 1)
        await ctx.send(f"Playing: {nname[0]}")

        while vc.is_playing():
            if Skip:
                vc.stop()
                break
            await asyncio.sleep(1)
        queue = queue[1:]
        await ctx.send("Next!")

        if len(queue) == 0:
            await vc.disconnect()
            return


# DONE
@client.command(help="'$stop' stops playing music in the voice channel and disconnects.")
async def stop(ctx):
    global queue
    voices = client.voice_clients
    if len(voices) > 0:
        vc = client.voice_clients[0]
        await ctx.send("Arrêt de la musique et déconnexion du canal.")
        await vc.disconnect()

    queue.clear()


@client.command(help="';skip' skips the music currently playing")
async def skip(ctx):
    global Skip
    Skip = True


@client.command(help="';clist' clears the queue")
async def clist(ctx):
    global queue
    queue.clear()
    await ctx.send("File d'attente vidée.")


# DONE
@client.command(help="'$custom This Sentence == This Response' will make the bot response by 'This Response' every"
                     "time a message containing 'This Sentence'is sent in the server.")
async def custom(ctx, *, args):
    sentence, response = args.split(sep="==")
    sentence = sentence.strip()
    response = response.strip()

    f = open("responses.txt", "a")
    f.write(sentence + "==" + response + "\n")
    f.close()

    await ctx.send("Réponse personnalisée ajoutée")


@client.command()
@commands.has_role('admin')
async def add_role(ctx, member: discord.Member, role):
    await member.add_roles(discord.utils.get(ctx.guild.roles, name=role))

client.run(TOKEN)

 