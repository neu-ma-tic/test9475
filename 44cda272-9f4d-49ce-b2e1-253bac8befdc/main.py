from os import name
import discord
from discord import player
from discord.colour import Color
from discord.ext import commands
import time
import asyncio
from discord.ext import tasks
from discord import Embed, Member
from datetime import datetime
import random
import string
from discord.ext.commands.core import command
from discord.message import Message
import requests
import urllib.request
from requests.api import request
import youtube_dl
from colorama import Fore
import re
from googlesearch import search
import aiohttp
from keep_alive import keep_alive
# set the apikey and limit
apikey = "LIVDSRZULELA"  # test value
lmt = 8

# our test search
search_term = "excited"


client = commands.Bot(command_prefix= "p.")
client.remove_command("help")
activeservers = client.guilds
@client.event
async def on_ready():

    print(f'''
Developer : DySecurity
 мяєχρℓσιт & ᴛᴇꜱꜱ

                                ''' )

#-----------------------------------------------------------------------------
# error system & random


@client.event
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title="PentCode Bot System Error",
    color=0x9B59B6)
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Error:', value=f'You dont have permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f'Error:', value = f"```{error}```")
        await ctx.send(embed = embed)

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))



#-----------------------------------------------------------------------------
# ADmin System
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=20):
      await ctx.channel.purge(limit=amount)
      embed=discord.Embed(title="Cleared Chat", description='`' + str(amount) + " massege has been cleared`", color=discord.Color.blue())
      await ctx.send(embed=embed)

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    embed=discord.Embed(title="muted", description=f"muted {member.mention} for reason {reason}.", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

    await member.remove_roles(mutedRole)
    embed=discord.Embed(title="Unmuted", description=f"Unmuted {member.mention}", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed=discord.Embed(title="Banned", description=f"{member} was Banned From Server !", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed=discord.Embed(title="kicked", description=f"{member} was kicked From Server !", color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command(name='dc', help='To make the bot leave the voice channel')
async def dc(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


def Ali(ctx):
    return ctx.author.id == 815161361793417287

def Tess(ctx):
    return ctx.author.id == 828537840131637260

@client.command()
@commands.check(Tess)
async def Tess_playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)

@client.command()
@commands.check(Ali)
async def Ali_playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)


#-----------------------------------------------------------------------------
#  System Public
@client.command()
async def avatar(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
        em = discord.Embed(description="Avatar System")
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Avatar Of", value=user.mention)
        await ctx.send(embed=em)
@client.command()
async def id(ctx):
    embed=discord.Embed(title="DySecurity", description=f"Your Developer ID : {ctx.author.id}", color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
async def info(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

# #@client.command(description="Gets info about the user")
# async def myinfo(ctx):
#     user = ctx.author

#     embed=discord.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=RandomColor())
#     embed.set_thumbnail(url=user.avatar_url)
#     embed.add_field(name="Name", value=user.name, inline=True)
#     embed.add_field(name="Nickname", value=user.nick, inline=True)
#     embed.add_field(name="ID", value=user.id, inline=True)
#     embed.add_field(name="Top role", value=user.top_role.name, inline=True)
#     await ctx.send(embed=embed)


@client.command()
async def invites(ctx, member:discord.Member=None):
      if member == None:
          member = ctx.message.author
      totalInvites = 0
      for i in await ctx.guild.invites():
          if i.inviter == member:
              totalInvites += i.uses
      embed=discord.Embed(title="Your Invites", description="**" + member.mention + " has invited `" + str(totalInvites) + " User` to `" + str(ctx.guild.name) + "`**", color=RandomColor())
      await ctx.send(embed=embed)

@client.command()
async def stream(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} Please Connect To a Voice Channel :D & Using This Command".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()



@client.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"client_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"PentCode-2.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"PentCode-1.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def wallpaper(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"PentCode-2.gif"))
    except:
        em = discord.Embed(description="PentCode Bot Wallpaper")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)#6S24K27YK4TP
@client.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"PentCode-2.gif"))
    except:
        em = discord.Embed(description="PentCode Bot Wallpaper")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@client.command()
async def inviteme(ctx, *, user: discord.Member = None):
        if user is None:
            await ctx.send(f"**DySecurity Official Server** :  https://discord.gg/dWSkje5Jwt")



@client.command()
async def addbot(ctx, *, user: discord.Member = None):
    if user is None:
        await ctx.send(f"**PentCode addBot Link :** https://discord.com/oauth2/authorize?client_id=838436903887306772&permissions=42949672878&scope=bot")



#---------------------------------------Music Bot -----------------------------------------
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

#-----------------------------------------------------------------------------------

@client.command()
async def announce(self, ctx, message):
    # Find a channel from the guilds `text channels` (Rather then voice channels)
    # with the name announcements
    channel = discord.utils.get(ctx.guild.text_channels, name="announcements")
    if channel: # If a channel exists with the name

                embed = discord.Embed(color=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
                embed.set_author(name="Announcement", icon_url=self.client.user.avatar_url)
                embed.add_field(name=f"Sent by {ctx.message.author}", value=str(message), inline=False)
                embed.set_thumbnail(url=self.client.user.avatar_url)
                embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.message.add_reaction(emoji="✅")
                await channel.send(embed=embed)

#--------------------------------------------------------------------------------------

@client.command()
async def developer(ctx):
    await ctx.send("***Developers :*** `MrExploit & Tess`")

@client.command()
@commands.has_permissions(administrator=True)
async def nitro(ctx):
     code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
     await ctx.send(f'https://discord.gift/{code}')

@client.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@client.command()
async def play(ctx,url):
    if not ctx.message.author.voice:
        await ctx.send("{} Please Connect To a Voice Channel :D & Using This Command".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
    try :
        url.strip()
        url = url.replace(' ','+')
        urlmusic = "https://youtube.com/results?search_query="+url
        html = urllib.request.urlopen(urlmusic)
        video_url = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        url = "https://youtube.com/watch?v=" + video_url[1]
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=client.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("Error ! - VPS is  Or Bot is Not Connected To a Voice Channel.")



#--------------------------------------------

@client.command(helpinfo='Info about servers PentCode Bot is in', aliases=['server', 'num', 'count'])
@commands.check(Ali)
async def servers(ctx):
    '''
    Info about servers PentCode Bot is in
    '''
    servers = client.guilds
    servers.sort(key=lambda x: x.member_count, reverse=True)
    await ctx.send('***Top servers with PentCode Bot:***')
    for x in servers[:5]:
        await ctx.send('**{}**, **{}** Members, {} region, Owned by <@{}>, Created at {}\n{}'.format(x.name, x.member_count, x.region, x.owner_id, x.created_at, x.icon_url_as(format='png',size=32)))
    y = 0
    for x in client.guilds:
        y += x.member_count
    await ctx.send('**Total number of PentCode Bot users:** ***{}***!\n**Number of servers:** ***{}***!'.format(y, len(client.guilds)))



@client.command()
async def website(ctx):
    '''
    PentCode Bot WebSite :D
    '''
    await ctx.send('***DySecurity WebSite : `DySecurity.net`')

#-------------------------------------------



@client.command()
async def wikipedia(ctx, *, query: str):
    '''
    Uses Wikipedia APIs to summarise search
    '''
    sea = requests.get(
        ('https://en.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Sorry, your search could not be found.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://en.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Sorry, your search could not be found.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://en.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=embed)

@client.command()
async def wikifarsi(ctx, *, query: str):
    '''
    Uses Wikipedia APIs to summarise search
    '''
    sea = requests.get(
        ('https://fa.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Sorry, your search could not be found.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://fa.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Sorry, your search could not be found.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://fa.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://fa.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)
@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@client.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@client.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
#---------------------------------------------------------------------------------------------
# system help
# 19 Gh 182:25

@client.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(colour=discord.Color.blue())
        embed.set_author(name=f"PentCode Bot Commands")
        embed.add_field(name="[Admins Commands]", value="-------------------------", inline=False)
        embed.add_field(name="p.clear [Amount]", value="Clear Messages💬", inline=False)
        embed.add_field(name="p.slowmode [time]" , value="Set the slowmode delay in a channel")
        embed.add_field(name="p.mute [user] [reason]", value="mute user -> the user can't Send massege and see channels🔇", inline=False)
        embed.add_field(name="p.unmute [user] [reason]", value="Unmute The Muted Users🔊", inline=False)
        embed.add_field(name="p.kick [user] [reason]", value="For Kicking a User🛑", inline=False)
        embed.add_field(name="p.ban [user] [reason]", value="For Banned a User🛑", inline=False)
        embed.add_field(name="[Public commands]", value="-------------------------", inline=False)
        embed.add_field(name="p.id", value="Get Your Developer ID✔️", inline=False)
        embed.add_field(name="p.addbot", value="Add Bot in Your Servers",inline=False)
        embed.add_field(name="p.info [user]", value="Get The User Info✔️", inline=False)
        embed.add_field(name="p.myinfo", value="Get Your Inf✔️o", inline=False)
        embed.add_field(name="p.invites", value="Your Invites✔️", inline=False)
        embed.add_field(name="p.inviteme", value="Official DySecurity Discord Server💕", inline=False)
        embed.add_field(name="[ Fun commands ]", value="-------------------------", inline=False)
        embed.add_field(name="p.slap [user]", value="For Slaping any User💔", inline=False)
        embed.add_field(name="p.kiss [user]", value="For Kissing any User👄", inline=False)
        embed.add_field(name="p.hug [user]", value="For Hug any User🙌", inline=False)
        embed.add_field(name="p.avatar" , value="Send Your Avatar 🙂" , inline=False)
        embed.add_field(name="p.mooz" , value="Send a Banana Picture And Say Mooz is Here :D🙂" , inline=False)
        embed.add_field(name="p.joon" , value="Send a Mr.Joon Picture And Say Mr.Joon is Here :D🙂" , inline=False)
        embed.add_field(name="[ Music ]", value="-------------------------", inline=False)
        embed.add_field(name="p.dc", value="For Disconnecting Bot From Voice Channel🔴", inline=False)
        embed.add_field(name="p.play [MusicName]" , value="For Play a Music From Youtube 🙂" , inline=False)
        embed.add_field(name="p.pause" , value="For Pause Music🙂" , inline=False)
        embed.add_field(name="p.resume" , value="For Resume Music🙂" , inline=False)
        embed2 = discord.Embed(colour=discord.Color.blue())
        embed.set_author(name=f"PentCode Bot Commands")
        embed.add_field(name="[ +18 Commands ]" , value="---------------------------" , inline=False)
        embed.add_field(name="p.blowjob" , value="BlowJob Gif :) " , inline=False)
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)
# https://discord.com/oauth2/authorize?client_id=838436903887306772&permissions=42949672878&scope=bot
keep_alive()
client.run("ODc5MzAxMTg2MTI0MTQ4ODE3.YSNvCw.ejUADWZkEQygam5ZyvFNxk_MB54")
