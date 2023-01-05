import discord
from discord.ext import commands
import random as ran
import os
import requests
import json
from bs4 import BeautifulSoup
from keep_alive import keep_alive
from replit import db
import time

TOKEN = 'ODY2MjQ1NzI1MjAxMzY3MDUw.YPPwMg.KpziWmvr7z55eIT-yF6d6ajvsTU'
intents = discord.Intents().all()
client =  commands.Bot(command_prefix='.', intents=intents)
current_time = time
blacklist = ["ZelBot#4282", "Saya#9919","DSL#8005", "PatchBot#0303","Support System#9687","Tatsu#8792","Crunchy#3276", "DISBOARD#2760","Saya#0000", "Crunchy#0000"]

water_reminder = []


signs_for_sadness = ["traurig", "depressiv", "weinen", "trauer", "heulen"]
beleidigung = ["Geringverdiener", "hochgelutschter S-Admin", "hässliger Esel", "Mongo", "Affe", "Spast", "Wichser", "Ehrenmann ♥", "Idiot", "Spacken", "noob", "Eselficker" ]


def top_messages(username):
  if username in blacklist:
    for item in blacklist:
      db[f"{item}"] = 0
      del db[f"{item}"]
    return
  if not username in db:
    db[f"{username}"] = 0
  db[f"{username}"] += 1
  return

#def watertimer():
 # for item in water_reminder:
  #  user=await client.get_user_info(f'{item}')
   # await client.send_message(user, "Your message goes here")
    # This works ^
    

def get_data():
  table = []
  for item in db.keys():
    table.append(f"{item} - {db[item]}") 
  return table

def get_news(keyword, date):
  news = requests.get(f"https://newsapi.org/v2/everything?q={keyword}&from={date}&sortBy=popularity&apiKey=a0281b7dd27b4fa9a2a56a5d5f8e4781")
  json_data = json.loads(news.text)
  new = json_data["articles"]
  return "Titel: " + new[0]["title"] + "\nAutor: " +new[0]["author"] +"\nInhalt: " + new[0]["description"] + "\n Link zum Artikel: " + new[0]["url"]
  


def math_facts(number):
    number = requests.get(f"http://numbersapi.com/{number}")
    data = BeautifulSoup(number.text, "html.parser")
    return data


def get_cat():
    cat = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(cat.text)
    cat = json_data[0]["url"]
    return cat


def get_lyric(artist, title):
    lyrics = requests.get("https://api.lyrics.ovh/v1/artist/title")


def get_quote():
    quote = requests.get("https://www.zenquotes.io/api/random")
    json_data = json.loads(quote.text)
    quote = json_data[0]['q'] + " ~ " + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print("Eingeloggt als {0.user}".format(client))


@client.command()
async def ping(ctx):
  await ctx.send("Pong!")


@client.command()
async def witz(ctx):
    await ctx.send(f'{str(ctx.author).split("#")[0]}, ich bin leider nicht lustig!')
    return


@client.command()
async def Counter(ctx):
    await ctx.send("<@284410829867057152> du bist ein " + beleidigung[ran.randrange(0,len(beleidigung))])


@client.command()
async def Zelimirus(ctx):
    await ctx.send(f'{str(ctx.author).split("#")[0]}, <@211524621579583488> ist meine Gottheit \n Link → https://www.steamcommunity.de/id/zelimirus \n http://steam.mmosvc.com/76561198271111367/v1.png')


@client.command()
async def random(ctx,span0, span1):
    await ctx.send(f'Hier ist deine Zufallszahl: {ran.randrange(int(span0),int(span1))}')


@client.command()
async def jinzey(ctx):
    await ctx.send(f'Lehrlings-Malboro sind mein go to!')


@client.command()
async def spenden(ctx):
    await ctx.send(f'{str(ctx.author).split("#")[0]}, bei Rückfragen über Spenden kannst du dich an \n  <@659920541041557524> wenden oder schreib ihm auf Steam \n http://steam.mmosvc.com/76561198217585712/v1.png')


@client.command()
async def quote(ctx):
    await ctx.send(get_quote())


@client.listen('on_message')
async def cat(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    if message.author == client.user:
        return
    if any(word in user_message for word in signs_for_sadness):
        await message.channel.send(f'{username} ♥! Kein Grund traurig zu sein, hier eine Katze!')
        await message.channel.send(get_cat())
    
        return

@client.listen('on_message')
async def highscore_list(message):
  if message.content.startswith(".") or message.content.startswith("/"):
    return  
  username = str(message.author)
  top_messages(username)
  return
  
    
@client.command()
async def Wassertimer(ctx):

  if client.user in water_reminder:
    water_reminder.remove(client.user)
    await ctx.send(f"{ctx.author} du wurdest in den auf die Wasser Erinnerungsliste entfernt")
    return
    
  if not client.user in water_reminder:
    water_reminder.append(client.user)
    await ctx.send(f"{ctx.author} du wurdest in den auf die Wasser Erinnerungsliste hinzugefügt" )
    return   

  




@client.command()
async def highscore(ctx):
  d = {}
  keys = db.keys()
  for item in keys:
    d[int(db[item])] = item
  listerino = sorted(d,reverse=True)
  #keystop = list(d.keys())
  #values = list(d.values())
  await ctx.send(f'💎💎 Message Highscore 💎💎\n\n👑 {listerino[0]} → {d[listerino[0]]} \n 💰 {listerino[1]} → {d[listerino[1]]} \n 🎈 {listerino[2]} → {d[listerino[2]]}  ')
  #await ctx.send(f'⨀ {keystop[0]} → {values[0]} ⨀')
  #for element in sorted(d,reverse=True):
    #await ctx.send(f'⨀ {d[element]} → {element} ⨀')
  
  



@client.listen('on_message')
async def nigger(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    if message.author == client.user:
      return
    if 'nigger' in user_message.lower() or 'neger' in user_message.lower():
      await message.delete()
      return

@client.command()
async def Bratan(ctx):
    await ctx.send("<@646845595495170071> ist schlecht in League und hat lange Haare. Habe ich schon erwähnt das er Jasmin heißt?")


@client.command()
async def steamgroup(ctx):
    await ctx.send("https://steamcommunity.com/groups/rbz-community")


@client.command()
async def group(ctx):
    await ctx.send("https://steamcommunity.com/groups/rbz-community")


@client.command()
async def Potcorn(ctx):
    await ctx.send("<@569683154982666242> kommt aus Ghana")


@client.command()
async def eXo(ctx):
    await ctx.send("<@398580923546992642> ist unser Gottkaiser")


@client.command()
async def Arr0w(ctx):
    await ctx.send("<@480729581230358538> der Mann mit dem Fickerblick")


@client.command()
async def zukrass(ctx):
    await ctx.send("<@659920541041557524> gibt dir dein VIP bald.")


@client.command()
async def math_fact(ctx, num):
    await ctx.send(math_facts(int(num)))


@client.command()
async def mathe(ctx, zahl, rechenzeichen, zahl2):
  if rechenzeichen == "+":
    await ctx.send(f"Dein Ergebnis lautet {int(zahl)+int(zahl2)}")
  elif rechenzeichen == "-":
    await ctx.send(f"Dein Ergebnis lautet {int(zahl)-int(zahl2)}")
  elif rechenzeichen == "*":
    await ctx.send(f"Dein Ergebnis lautet {int(zahl)*int(zahl2)}")
  elif rechenzeichen == "/":
    await ctx.send(f"Dein Ergebnis lautet {int(zahl)/int(zahl2)}")
  else:
    await ctx.send("Ich kann diese Rechnung noch nicht bearbeiten, sorry ╯︿╰")


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='🎮 Gamer')
    role2 = discord.utils.get(member.guild.roles, name='⊶▬⊶▬ 🎮 Gamer ▬⊷▬⊷')
    await member.add_roles(role, role2)



@client.command()
async def news(ctx, *args):
    await ctx.send(get_news(*args))

#@client.command()
#async def accept(ctx):
#    member = ctx.message.author  
#    role = discord.utils.get(member.server.roles, name='🎮 Gamer')
#    role2 = discord.utils.get(member.server.roles, name='⊶▬⊶▬ 🎮 Gamer ▬⊷▬⊷')
#    await member.add_roles(role, role2)
    

@client.command()
async def catbomb(ctx):
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())
  await ctx.send(get_cat())

keep_alive()
client.run(TOKEN)