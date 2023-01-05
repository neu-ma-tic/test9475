import utils.webserver as webserver
import asyncio
import re
import os
from utils.prefix import sdprefix
import time
from asyncio import TimeoutError
from pymongo import MongoClient
import pytz
from datetime import datetime
import pyjokes
from aiohttp import ClientSession
import aiohttp
from googletrans import Translator
import urllib.request
import urllib.parse
import utils.checks as checks
import aiofiles
import discord
from discord.ext import commands, tasks
import googletrans
import requests
from utils.weather import *
from itertools import cycle
import praw
import json
from jokeapi import Jokes  # Import the Jokes class
from music import Player
from random import choice
import random

bot_channel = 849560726833987614



cluster_url = os.environ.get("mongocluster")
cluster = MongoClient(cluster_url)
db = cluster['discord']
prefix_col = db['prefix']


api_key = 'c9e0001dbaf939965745ba62f33b30bd'

intents = discord.Intents.all()

reddit = praw.Reddit(client_id="EuMYuE8P7Et9zZXg3fb5qw",
                     client_secret="qn1xVhWJCzF7ti4BIWF0gFVCwrH8FQ",
                     username="RunTheProgram",
                     password="3Ddrawing*!",
                     user_agent="RunTheProgram")




client = commands.Bot(command_prefix =  sdprefix, activity=discord.Game(name='with a Program'), intents=intents)
    


slowdown = ['Woal now, slow down','Take a chill pill','Dude stop rushing','Hold your horses...','Heeeyoo lets slow it down','Woal nelly, slow it down','Spam isnt cool fam']



@client.event
async def on_guild_join(guild):
    embed=discord.Embed(title='Thanks for adding me!',description='Server Prefix: `.`\nHelp Command: `.help`')
    embed.set_footer(text='Join the support server!',icon_url='https://cdn.discordapp.com/avatars/763315062668001301/a0117e092350cef21f457ec864a1d0d0.png?size=1024')

    view = discord.ui.View()
    view.add_item(discord.ui.Button(label='Support server', url='https://discord.gg/DQDxhpUJkH', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label="Invite Me", url='https://discord.com/api/oauth2/authorize?client_id=763315062668001301&permissions=8&scope=bot%20applications.commands', style=discord.ButtonStyle.url))


    await guild.text_channels[0].send(embed=embed,view=view)



    users = get_xp()
    users[str(guild.id)] = {}
    with open("levels.json","w") as f:
      json.dump(users,f)

    prefix_col.insert_one({"server":str(guild.id),"prefix":"."})




@client.command(aliases=['cp'])
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    prefix_col.update_one({str(ctx.guild.id): "."},{"$set":{str(ctx.guild.id):str(prefix)}})
    embed = discord.Embed(title='The prefix was changed',description=f'The prefix is: "{prefix}"')
    embed.set_footer(text=f'The embed was changed by {ctx.author}',icon_url=ctx.author.display_avatar)
    
    await ctx.send(embed=embed)



@client.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")



  

@client.event
async def on_ready():
  print("It's ready :D")
  statuses = cycle([
    discord.Game('Type .help | ProgramX.com'),
    discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} Servers"),
    discord.Activity(type=discord.ActivityType.watching, name="YOU")
  ])
  while True:
    await client.change_presence(activity=next(statuses))
    await asyncio.sleep(5)

  
    
    
    




@client.event
async def on_member_join(member):
    idchannel = 849553686811246612
    if member.guild.id == 769371376392863815:
        await client.get_channel(idchannel).send(
            f"**{member.mention}** has joined the server. Welcome!")
        role = member.guild.get_role(849547896558190593)
        await member.add_roles(role)
        role1 = member.guild.get_role(868755571757707314)
        await member.add_roles(role1)
        await client.get_channel(769371376845979673).purge(limit = 1)


@client.event
async def on_member_remove(member):
    idchannel = 849553686811246612
    if member.guild.id == 769371376392863815:
        await client.get_channel(idchannel).send(
            f"**{member.mention}** has left the server ;-; Hope you had a fun time!"
        )
global events
events = True


@client.event
async def on_message(message):
  if message.author == client.user:
        return



  if message.guild.id != 681882711945641997:  


    msg = message.content
    text_list = ['shutup', 'f**koff']

    #comeback machine lol
    if message.author.id == owner_id:
        if any(text in msg for text in text_list):
            comeback = [
                'Yeah exactly! Now shut up or Ill shut you up',
                'Yeah! Would you just shut up?',
                'Exactly! Please stop being a retard',
                'Yeah! Stop being so toxic'
            ]
            await message.channel.send(random.choice(comeback))
  await client.process_commands(message)










def get_xp():
  with open("levels.json","r") as f:
    xp = json.load(f)
  return xp

async def open_rank(user, guild):
    users = get_xp()
    if str(user.id) in users[str(guild)]:
      return False
    else:
        print(user)
        users[str(guild)][str(user.id)] = {}
        users[str(guild)][str(user.id)]["xp"] = 0
        users[str(guild)][str(user.id)]["level"] = 1
    with open("levels.json", "w") as f:
        json.dump(users, f)
    return True

@client.command()
@commands.check(checks.is_it_me)
async def givelvl(ctx,amount:int,member:discord.Member=None):
  if member is None:
    member = ctx.author
  user=get_xp()
  user[ctx.guild.id][str(member.id)]["level"] += amount
  with open("levels.json", "w") as f:
        json.dump(user, f)

@givelvl.error
async def whoami_error(error, ctx):
    if isinstance(error, commands.MissingPermissions):
        msg = "You really think that would work? <:lol:899484944512991262>"
        await ctx.send(msg)





  





@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def kill(ctx,member:discord.Member=None):

  death_messages = [' has fell into the void', ' was pricked to death', ' drowned', ' blew up', ' was killed by [Intentional Game Design]', ' hit ground too hard', ' tried to swim in lava', ' fell off a high place', 'death.fell.accident.water']
  rand_death = random.choice(death_messages)
  if member is None:
    await ctx.send(f"** **{ctx.author.name}{rand_death}")

  if member.id == 696617859580690512:
    await ctx.send("https://tenor.com/view/reverse-card-uno-uno-cards-gif-13032597")
    await ctx.send(f"** **{ctx.author.name}{rand_death}")

  else:
    await ctx.send(f"** **{member.name}{rand_death}")

@kill.error
async def kill_error(ctx,error):
  if isinstance(error, commands.CommandOnCooldown):
    embed=discord.Embed(title="Still on cooldown ",description="You can retry in {:.2f}s\nThe cooldown is `3s` but patrons only `1s`".format(
            error.retry_after))
    await ctx.send(embed=embed)
    

#slash rank
@client.slash_command()
async def rank(ctx, member:discord.Member = None):
  
  if member == None:
    await open_rank(ctx.author, ctx.author.guild.id)
    users = get_xp()
    txp = 100 * users[str(ctx.author.guild.id)][str(ctx.author.id)]["level"]
    xp = users[str(ctx.author.guild.id)][str(ctx.author.id)]["xp"]
    level = users[str(ctx.author.guild.id)][str(ctx.author.id)]["level"]


    users = get_xp()
    leader_board = {}
    total = []
    for user in users[str(ctx.guild.id)]:
        name = int(user)
        total_amount = users[str(ctx.guild.id)][str(user)]["xp"] + (users[str(ctx.guild.id)][str(user)]["level"] * 100)
        leader_board[total_amount] = name

        total.append(total_amount)
    total = sorted(total,reverse=True) 
    rank = 1
    for amt in total:
      id_ = leader_board[amt]
      member = client.get_user(id_)
      if member is None:
        continue
      if ctx.author != member:
        rank += 1
      else:
        break
      
      



    tbox = 20
    sxp = xp/txp
    boxes = int(sxp*tbox)
    embed = discord.Embed(title="{}'s level  stats".format(ctx.author.name), color=discord.Color.random())
    embed.add_field(name="Name", value=ctx.author.mention, inline=True)
    embed.add_field(name="XP", value=f"{xp}/{txp}", inline=True)
    embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
    embed.add_field(name="level", value=f"{level}")
    embed.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_square:" + (tbox-boxes) * ":white_large_square:",
                        inline=False)
    try:
      embed.set_thumbnail(url=ctx.author.display_avatar)
    except:
      embed.set_thumbnail(url='https://static.wikia.nocookie.net/discordian-republic/images/1/10/3.png/revision/latest?cb=20210327224009')
    
    await ctx.respond(embed=embed)
  else:
      await open_rank(member, member.guild.id)
      users = get_xp()
      xp = users[str(member.guild.id)][str(member.id)]["xp"]
      level = users[str(member.guild.id)][str(member.id)]["level"]
      txp = 100 * users[str(member.guild.id)][str(member.id)]["level"]


      users = get_xp()
      leader_board = {}
      total = []
      for user in users[str(ctx.guild.id)]:
          name = int(user)
          total_amount = users[str(ctx.guild.id)][str(user)]["xp"] + (users[str(ctx.guild.id)][str(user)]["level"] *   100)
          leader_board[total_amount] = name

          total.append(total_amount)
      total = sorted(total,reverse=True) 
      rank = 1
      for amt in total:
        id_ = leader_board[amt]
        membersss = client.get_user(id_)
        if membersss is None:
          continue
        if member.id != id_:
          rank += 1
        else:
          break
      


      tbox = 20
      sxp = xp/txp
      boxes = int(sxp*tbox)
      embed = discord.Embed(title="{}'s level  stats".format(member.name), color=discord.Color.random())
      embed.add_field(name="Name", value=member.mention, inline=True)
      embed.add_field(name="XP", value=f"{xp}/{txp}", inline=True)
      embed.add_field(name="Rank", value=f"{rank}/{member.guild.member_count}", inline=True)
      embed.add_field(name="level", value=f"{level}")
      embed.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_square:" + (tbox-boxes) * ":white_large_square:",
                          inline=False)
      try:
        embed.set_thumbnail(url=member.display_avatar)
      except:
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/discordian-republic/images/1/10/3.png/revision/latest?cb=20210327224009')
      await ctx.respond(embed=embed)

  

@client.slash_command(aliases = ["lb"])
async def leaderboard(ctx,x = 5):
        users = get_xp()
        leader_board = {}
        bom = {}
        total = []
        for user in users[str(ctx.guild.id)]:
            name = int(user)
            total_amount = users[str(ctx.guild.id)][str(user)]["xp"] + (users[str(ctx.guild.id)][str(user)]["level"] * 100)
            leader_board[total_amount] = name
            bom[total_amount] = users[str(ctx.guild.id)][str(user)]["level"]
            total.append(total_amount)
   
        total = sorted(total,reverse=True)    

        em = discord.Embed(title = f"{ctx.guild.name}'s Leader Board" , description = "This is decided on the basis of how active you are on the server",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
          id_ = leader_board[amt]
          member = client.get_user(id_)
          if member is None:
              continue
          if member not in ctx.guild.members:
            continue

          name = member.name
          em.add_field(name = f"{index}. {name}" , value = "Level {:.0f}".format(bom[amt]),  inline = False)
          if index == x:
                break
          else:
                index += 1
        
        em.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.display_avatar)
        await ctx.respond(embed = em)




@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title='ProgramX invitation',
        description=
        '[Click Here](https://discord.com/api/oauth2/authorize?client_id=763315062668001301&permissions=8&scope=bot%20applications.commands)\n[Learn how to make a bot yourself](https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1)',
        color=discord.Color.red())
    embed.set_footer(text=f'Requested by {ctx.author.name}',
                     icon_url=ctx.author.display_avatar)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label='YouTube Channel', url='https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label="Invite me", url='https://discord.com/api/oauth2/authorize?client_id=763315062668001301&permissions=8&scope=bot%20applications.commands', style=discord.ButtonStyle.url))
    await ctx.send(
        embed=embed,view=view
    )
@client.command()
async def leaveg(ctx, *, guild_name=None):
    guild = discord.utils.get(client.guilds, name=guild_name) # Get the guild by name
    guildc = ctx.guild


    if guild is None:
        print("No guild with that name found.") # No guild found
        return
    if guild_name is None:
      await guildc.leave()
    await guild.leave() # Guild found
    await ctx.send(f"I left: {guild.name}!")

page1 = discord.Embed(
    title="Bot Help 1",
    description="Use the buttons below to navigate between help pages.",
    colour=discord.Color.orange())
page2 = discord.Embed(title="Bot Help 2",
                      description="Page 2",
                      colour=discord.Color.orange())
page3 = discord.Embed(title="Bot Help 3",
                      description="Page 3",
                      colour=discord.Color.orange())

client.help_pages = [page1, page2, page3]


@client.command()
async def Help(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1",
               u"\u23E9"]  # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=client.help_pages[current])

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        try:
            reaction, user = await client.wait_for(
                "reaction_add",
                check=lambda reaction, user: user == ctx.author and reaction.
                emoji in buttons,
                timeout=60.0) 

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0

            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1

            elif reaction.emoji == u"\u27A1":
                if current < len(client.help_pages) - 1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(client.help_pages) - 1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])



@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

@client.command()
async def test(ctx):
  
  class MyView(discord.ui.View):
        @discord.ui.button(emoji='😀', label="Button 1", style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
            for child in self.children:
                child.disabled = True
            button.label = 'No more pressing either button!'
            await interaction.response.edit_message(view=self)
        @discord.ui.button(label="Button 2", style=discord.ButtonStyle.primary)
        async def second_button_callback(self, button, interaction):
            for child in self.children:
                child.disabled = True
            button.label = 'No more pressing either button!'
            await interaction.response.edit_message(view=self)

  # somewhere else...
  view = MyView()
  await ctx.send('Press the button!', view=view)
        


@client.command()
async def ping(ctx):
    await ctx.send(f'🏓**Pong!** Latency: {round(client.latency * 1000)}ms')


@client.command()
async def aibot(ctx, *, args):
    message = args
    key = "k5eOddS5Uj9t"
    header = {"x-api-key": key}
    type = "stable"
    params = {'type': type, 'message': message}
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(url='https://api.pgamerx.com/v3/ai/response',
                               params=params) as resp:
            text = await resp.json()
            print(resp.status)
            await ctx.send(text[0]['message'])


@client.command()
async def programmer_joke(ctx):
    joke = pyjokes.get_joke()
    await ctx.send(joke)


owner_id = 934299415622078474


@client.command()
async def joke(ctx):

    urls = "https://dad-jokes.p.rapidapi.com/random/jokes"

    headers = {
        'x-rapidapi-key': "288fd18848mshb066f43d241c797p1603dejsne3b93c3e4352",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

    responsed = requests.request("GET", urls, headers=headers)
    json_thing = json.loads(responsed.text)
    await ctx.send(
        f"**{json_thing['body'][0]['setup']}**\n\n||{json_thing['body'][0]['punchline']}||"
    )


@client.command(aliases=['tr'])
async def translate(ctx, lang, *, args):
    lang = lang.lower()
    if lang not in googletrans.LANGUAGES and lang not in googletrans.LANGCODES:
        raise commands.BadArgument('Invalid language to translate text to')
    translator = googletrans.Translator()
    text_translated = translator.translate(args, dest=lang).text
    await ctx.send(f"Text: {args}\nTranslated text: {text_translated}")




def getquote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.command(name='inspire', help='this command inspires people')
async def inspire(ctx):
    quote = getquote()
    await ctx.send(quote)


@client.command()
async def musichelp(ctx):
    await ctx.send('Use .play and then the video of your choice')


@client.command()
async def minecraft(ctx, arg):
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()

    description = json_data["server"]["motd"]
    online = str(json_data["server"]["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(title=arg + " Server Info",
                          description='Description: ' + description +
                          '\nOnline: ' + online + '\nPlayers: ' + playerCount,
                          color=discord.Color.dark_green())
    embed.set_thumbnail(
        url=
        "https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1"
    )

    await ctx.send(embed=embed)







@client.command()
@commands.check(checks.is_it_me)
async def dm(ctx, member: discord.Member, *, args):
    await member.send(args)
    await ctx.send(f"'{args}' sent to {member}")


@client.command()
async def say(ctx, *, args):
    if ctx.author.id == owner_id:
        await ctx.send(args)
    else:
      list = ['bruh no', 'why should I?','no u','no thanks','no']
      random_sd = random.choice(list)
      await ctx.send(random_sd)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def altmeme(ctx, topic=None):
  if topic is None:
    await ctx.send(embed=discord.Embed(description='please specify the topic of meme'))
  else:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://meme-api.herokuapp.com/gimme/{topic}') as r:
            res = await r.json()
            embed = discord.Embed(title=res['title'],
                                  color=discord.Color.random())
            embed.set_image(url=res['preview'][-1])
            embed.set_footer(text=f"👍 {res['ups']} • Requested by {ctx.author.name}",             icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
tz_NY = pytz.timezone('Australia/Melbourne') 
t = datetime.now(tz_NY)
current_time = t.strftime("%H:%M")
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://meme-api.herokuapp.com/gimme/') as r:
            res = await r.json()
            if res['nsfw'] == True:
              pass
            else:
              embed = discord.Embed(title=res['title'],
                                    color=discord.Color.random())
              embed.set_image(url=res['preview'][-1])
              embed.set_footer(text=f"👍{res['ups']} • Requested by {ctx.author.name}",             icon_url=ctx.author.display_avatar)
              emojis = ['👍', '👎']
              message = await ctx.send(embed=embed)
              for emoji in emojis:
                await message.add_reaction(emoji)


@meme.error
async def meme_error(ctx,error):
  if isinstance(error, commands.CommandOnCooldown):
    r_slowdown = random.choice(slowdown)
    embed=discord.Embed(title=r_slowdown,description="You can run this command in **{:.2f} second**\nThe default cooldown is `3s` but [subscribers](https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1) only need to wait `1s`!".format(
            error.retry_after))
    await ctx.send(embed=embed)

@client.command()
async def stevenhe(ctx):
    await ctx.send("You Faliure!")
    subreddit = reddit.subreddit("StevenHe")
    all_subs = []
    top = subreddit.top(limit=200)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)


@client.command(name="hello", help="this command returns a welcome message")
async def hello(ctx):
    await ctx.send(f'***grumble*** Why did you wake me up?')


@client.command(name="credit", help="this command returns the credit")
async def credit(ctx):
    embed = discord.Embed(
        title='Credit',
        description=
        "**Made by `Andy` aka RunTheProgram**\nAlso make sure to check out Andy's YouTube Channel and Discord server!\nIf you need any help with the bot you can join the ProgramX support server!",
        color=discord.Color.random())
    embed.set_footer(text=f'Requested by {ctx.author.name}',
                     icon_url=ctx.author.display_avatar)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label='YouTube Channel', url='https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label="Dev's Server", url='https://discord.gg/DQDxhpUJkH', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label='ProgramX Support', url='https://discord.gg/6SepjBwx38', style=discord.ButtonStyle.url))

    await ctx.send(
        embed=embed,view=view
    )


@client.command()
async def weather(ctx, country, location):
    state = 'randomshit'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location},{state},{country}&appid={api_key}&units=metric'
    try:
        data = parse_data(json.loads(requests.get(url).content)['main'])
        await ctx.send(embed=weather_message(data, location))
    except KeyError:
        await ctx.send(embed=error_message(location))




@client.command()
async def AndyBot(ctx, *, question):
    if ctx.author.id == owner_id:
        await ctx.send("I AM REALLY SORRY I WON'T DO IT AGAIN")
    else:
        return False


@client.command()
async def hack(ctx, member: discord.Member):
    m = await ctx.send(f'Hacking {member} right now!!')
    await asyncio.sleep(2)
    await m.edit('Bypassing 2fa discord login')
    await asyncio.sleep(2)
    await m.edit('Metasploit reverse shell injection')
    await asyncio.sleep(2)
    await m.edit('clickjacking html json excution')
    await asyncio.sleep(2)
    await m.edit('ip = 127.0.0.7')
    await asyncio.sleep(2)
    await m.edit('stealing nitro')
    await asyncio.sleep(2)
    await m.edit('reporting user to discord for breaking discord TOS')
    await asyncio.sleep(2)
    await m.edit('getting social security number')
    await asyncio.sleep(2)
    await m.edit('social security number: 6969696969420')
    await asyncio.sleep(2)
    await m.edit('the super realistic hack is finished')




@client.slash_command()
async def eightball(ctx, *, question):
    reponses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    await ctx.respond(f'Question: {question}\nAnswer: {random.choice(reponses)}')


  

@client.slash_command()
async def invite(ctx):
    embed = discord.Embed(
        title='ProgramX invitation',
        description=
        '[Click Here](https://discord.com/api/oauth2/authorize?client_id=763315062668001301&permissions=8&scope=bot%20applications.commands)\n[Learn how to make a bot yourself](https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1)',
        color=discord.Color.red())
    embed.set_footer(text=f'Requested by {ctx.author.name}',
                     icon_url=ctx.author.display_avatar)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label='YouTube Channel', url='https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label="Dev's Server", url='https://discord.com/api/oauth2/authorize?client_id=763315062668001301&permissions=8&scope=bot%20applications.commands', style=discord.ButtonStyle.url))
    await ctx.respond(
        embed=embed,view=view
    )


@client.command()
async def avatar(ctx,user:discord.Member=None):
  if user == None:
    embed = discord.Embed(title="Your avatar")
    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
    embed.set_image(url=ctx.author.display_avatar)
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title=f"{user.name}'s avatar'")
    embed.set_author(name=user,icon_url=user.display_avatar)
    embed.set_image(url=user.display_avatar)
    await ctx.send(embed=embed)

@client.slash_command()
async def avatar(ctx,user:discord.Member=None):
  if user == None:
    embed = discord.Embed(title="Your avatar")
    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
    embed.set_image(url=ctx.author.display_avatar)
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title=f"{user.name}'s avatar'")
    embed.set_author(name=user,icon_url=user.display_avatar)
    embed.set_image(url=user.display_avatar)
    await ctx.send(embed=embed)


@client.slash_command()
@commands.check(checks.is_it_me)
async def server(ctx):
    await ctx.respond("\n".join([i.name for i in client.guilds]))




@client.slash_command()
async def test(ctx):
    await ctx.respond(discord.__version__)


@client.slash_command()
async def ping(ctx):
    await ctx.respond(f'🏓**Pong!** Latency: {round(client.latency * 1000)}ms')


@client.slash_command()
async def aibot(ctx, *, args):
    message = args
    key = "k5eOddS5Uj9t"
    header = {"x-api-key": key}
    type = "stable"
    params = {'type': type, 'message': message}
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(url='https://api.pgamerx.com/v3/ai/response',
                               params=params) as resp:
            text = await resp.json()
            print(resp.status)
            await ctx.respond(text[0]['message'])


@client.slash_command()
async def programmerjoke(ctx):
    joke = pyjokes.get_joke()
    await ctx.respond(joke)




@client.slash_command()
async def joke(ctx):

    urls = "https://dad-jokes.p.rapidapi.com/random/jokes"

    headers = {
        'x-rapidapi-key': "288fd18848mshb066f43d241c797p1603dejsne3b93c3e4352",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

    responsed = requests.request("GET", urls, headers=headers)
    json_thing = json.loads(responsed.text)
    await ctx.respond(
        f"**{json_thing['body'][0]['setup']}**\n\n||{json_thing['body'][0]['punchline']}||"
    )


@client.slash_command(aliases=['tr'])
async def translate(ctx, lang, *, args):
    lang = lang.lower()
    if lang not in googletrans.LANGUAGES and lang not in googletrans.LANGCODES:
        raise commands.BadArgument('Invalid language to translate text to')
    translator = googletrans.Translator()
    text_translated = translator.translate(args, dest=lang).text
    await ctx.respond(text_translated)


@client.slash_command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = [
        'why have you brought my short life to an end',
        'i could have done so much more', 'i have a family, kill them instead'
    ]
    await ctx.respond(random.choice(responses))


@client.slash_command(name='inspire', help='this command inspires people')
async def inspire(ctx):
    quote = getquote()
    await ctx.respond(quote)


@client.slash_command()
async def musichelp(ctx):
    await ctx.respond('Use .play and then the video of your choice')


@client.slash_command()
async def minecraft(ctx, arg):
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()

    description = json_data["server"]["motd"]
    online = str(json_data["server"]["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(title=arg + " Server Info",
                          description='Description: ' + description +
                          '\nOnline: ' + online + '\nPlayers: ' + playerCount,
                          color=discord.Color.dark_green())
    embed.set_thumbnail(
        url=
        "https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1"
    )

    await ctx.respond(embed=embed)







@client.slash_command()
async def say(ctx, *, args):
    if ctx.author.id == owner_id:
        await ctx.respond(args)
    else:
      list = ['bruh no', 'why should I?','no u','no thanks','no']
      random_sd = random.choice(list)
      await ctx.respond(random_sd)




@client.slash_command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://meme-api.herokuapp.com/gimme/') as r:
            res = await r.json()
            embed = discord.Embed(title=res['title'],
                                  color=discord.Color.random())
            embed.set_image(url=res['preview'][-1])
            embed.set_footer(text=f"👍 {res['ups']} • Requested by {ctx.author.name}",             icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)



@client.slash_command(name="credit", help="this command returns the credit")
async def credit(ctx):
    embed = discord.Embed(
        title='Credit',
        description=
        "**Made by `Andy` aka RunTheProgram**\nAlso make sure to check out Andy's YouTube Channel and Discord server!\nIf you need any help with the bot you can join the Andy-Bot support server!",
        color=discord.Color.random())
    embed.set_footer(text=f'Requested by {ctx.author.name}',
                     icon_url=ctx.author.display_avatar)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label='YouTube Channel', url='https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label="Dev's Discord Server", url='https://discord.gg/DQDxhpUJkH', style=discord.ButtonStyle.url))
    view.add_item(discord.ui.Button(label='ProgramX Support', url='https://discord.gg/6SepjBwx38', style=discord.ButtonStyle.url))

    await ctx.respond(
        embed=embed,view=view
    )







@client.slash_command(help="Using this command, you can type forever in whatever channel you want!")
async def typing(ctx,token,channel_id):
    await ctx.respond("Typing Initialted :D")
    url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
    headers = {
    'authorization': token
    }
    while True:
        response = requests.request("POST", url, headers=headers)
        if response.status_code != 204:
            await ctx.author.send(f"{response.text}")
            await ctx.author.send("Stopped sending typing packets")
            break
        time.sleep(8)





@client.slash_command()
async def andybot(ctx, *, question):
    if ctx.author.id == owner_id:
        await ctx.respond("I AM REALLY SORRY I WON'T DO IT AGAIN")
    else:
        return False


@client.slash_command()
async def hack(ctx, member: discord.Member):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []
        for i in users[str(user.id)]:
          if "<:command_block:894349809027252244>command block" not in i:
            embed=discord.Embed(title="Dude.. you nee d a command block to hack",description="that's definitely how you hack lol")
            await ctx.send(embed=embed)



        




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        title_error_one = 'You have not entered anything after the command'
        desc_error_one = 'Use **.help** to see all the functionalities avalible'
        embed_var_one = discord.Embed(title=title_error_one,
                                      description=desc_error_one,
                                      color=0xFF0000)
        await ctx.send(embed=embed_var_one)
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Still on cooldown**, please try again in {:.2f}s'.format(
            error.retry_after)
        await ctx.send(msg)

    if isinstance(error,commands.MissingPermissions):
      await ctx.send(f":x:**{ctx.author.name}** You do not have permission to do that!")


    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry, you don't have permission to do that lol")

    raise error


@client.command()
@commands.check(checks.is_it_me)
async def load(ctx,cog:str):
  try:
    client.load_extension(cog)
  except Exception as e:
    await ctx.send("Could not load this cog")
    return

  await ctx.send('Cog loaded')

@client.command()
@commands.check(checks.is_it_me)
async def unload(ctx,cog:str):
  try:
    client.unload_extension(cog)
  except Exception as e:
    await ctx.send("Could not unload this cog")
    return

  await ctx.send('Cog unloaded')
@client.command()
@commands.check(checks.is_it_me)
async def reload(ctx,cog:str):
  try:
    client.unload_extension(cog)
    client.load_extension(cog)
  except Exception as e:
    await ctx.send("Could not reload this cog")
    return

  await ctx.send('Cog reloaded')


async def setup():
    await client.wait_until_ready()
    client.add_cog(Player(client))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.loop.create_task(setup())

webserver.keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)
