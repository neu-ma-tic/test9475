import discord
import os
import json
import music 
from discord.ext import commands
from keep_alive import keep_alive
import requests
import random
from random import randint
from uuid import uuid4

from image_cog import image_cog

cogs = ["music"]

def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)] 

client = commands.Bot(command_prefix=",", help_command=None)

for i in cogs:
  try:
    client.load_extension(i)
    print(i + " loaded successfully!")
  except Exception as e:
    print(f'Couldn\'t load {i}')
    print(e)

@client.event
async def on_ready():
  print('Erfolgreich als {0.user} eingeloggt'.format(client))
  #await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="Mexikanischer Igel", type=1))

@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(
      title = f"Du besitzt nicht die nötige Berechtigung für diesen Befehl :no_entry_sign:",
      colour = 0xd53535
    )

    await ctx.send(embed = embed)
  elif isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(
      title = f"Bitte wähle ein passendes Symbol :pencil2: ",
      colour = 0xf1c232
    )

    await ctx.send(embed = embed)

@client.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '.'

  with open('prefixes.json', 'w') as f:
   json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
         prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(manage_guild = True)
async def changeprefix(ctx, prefix):
     if " " in prefix:
          embed =  discord.Embed(
      title = f"Unpassender Prefix :no_entry_sign:",
      colour = 0xd53535
     )

     await ctx.send(embed = embed)
     return
     with open('prefixes.json', 'r') as f:
          prefixes = json.load(f)

     prefixes[str(ctx.guild.id)] = prefix
     with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

     await ctx.send(f'Prefix wurde zu `{prefix}` geändert')

@client.command()
async def say(ctx, text="hello"):
  await ctx.send(text, tts=True)

@client.event
async def on_message(message):
  if client.user.mentioned_in(message):
    if 'everyone' in message.content:
      await client.process_commands(message)
    elif 'here' in message.content:
      await client.process_commands(message)
    else:
      embed = discord.Embed(title=f'__Mein Prefix ist__ `{get_prefix(client,message)}`', color=discord.Colour.blue())
      embed.add_field(name=f"und mehr Informationen bekommst du mit", value=f"`{get_prefix(client,message)}Help`")
      await message.channel.send(embed=embed)
  await client.process_commands(message)

@client.command()
async def hallo(ctx):
  await ctx.send('hallo')

@client.command(aliases=["Ping", "status", "Status"])
async def ping(ctx):
    embed =  discord.Embed(
      title = f"*Mein Ping ist* `{round(client.latency * 1000)}ms`  :globe_with_meridians:",
      colour = 0x3678b4
     )

    await ctx.send(embed = embed)

@client.command()
async def help(ctx):
    embed =  discord.Embed(
      title = f"Du brauchst Hilfe?",
      colour = 0x6d6f71
     )

    embed.add_field(name=f" Alle Befehle anzeigen lassen ", value=f"Mit __!Befehle__ siehst du alle Befehle mit Erklärung")
    
    embed.add_field(name=f" Im Chat Fragen ", value=f"Im öffentlichen Chat um Hilfe bitten", inline=False)
    embed.set_thumbnail(url="https://praklahom.ch/wp-content/uploads/2018/08/Beitrag_Fragezeichen.jpg")

    await ctx.send(embed = embed)

@client.command()
async def Help(ctx):
    embed =  discord.Embed(
      title = f"Du brauchst Hilfe?",
      colour = 0x6d6f71
     )

    embed.add_field(name=f" Alle Befehle anzeigen lassen ", value=f"Mit __!Befehle__ siehst du alle Befehle mit Erklärung")
    
    embed.add_field(name=f" Im Chat Fragen ", value=f"Im öffentlichen Chat um Hilfe bitten", inline=False)
    embed.set_thumbnail(url="https://praklahom.ch/wp-content/uploads/2018/08/Beitrag_Fragezeichen.jpg")

    await ctx.send(embed = embed)

@client.command()
async def info(ctx):
    embed =  discord.Embed(
      title = f"__Informationen über BreBot__",
      colour = 0xfdfdfd
     )

    embed.add_field(name="Prefix :", value=f"*{get_prefix(client,ctx)}*")
    embed.set_thumbnail(url="https://static.vecteezy.com/ti/gratis-vektor/p1/553845-ausrufezeichen-symbol-kostenlos-vektor.jpg")
    embed.add_field(name="Befehle", value=f"5")
    embed.add_field(name="Für mehr Befehle nutze", value=f"{get_prefix(client,ctx)}Befehle", inline=False)

    await ctx.send(embed = embed)

@client.command()
async def iguildsnfo(ctx):
    embed =  discord.Embed(
      title = len(client.guilds),
      colour = 0xfdfdfd
     )

    embed.add_field(name="Prefix :", value=f"*{get_prefix(client,ctx)}*")
    embed.set_thumbnail(url="https://static.vecteezy.com/ti/gratis-vektor/p1/553845-ausrufezeichen-symbol-kostenlos-vektor.jpg")
    embed.add_field(name="Befehle", value=f"5")
    embed.add_field(name="Für mehr Befehle nutze", value=f"{get_prefix(client,ctx)}Befehle", inline=False)
    listofids = []
    for guild in client.guilds:
        listofids.append(guild.id)
    await ctx.send(listofids)

    await ctx.send(embed = embed)

@client.command()
async def Info(ctx):
    embed =  discord.Embed(
      title = f"__Informationen über BreBot__",
      colour = 0xfdfdfd
     )

    embed.add_field(name="Prefix :", value=f"*{get_prefix(client,ctx)}*")
    embed.set_thumbnail(url="https://static.vecteezy.com/ti/gratis-vektor/p1/553845-ausrufezeichen-symbol-kostenlos-vektor.jpg")
    embed.add_field(name="Befehle", value=f"5")
    embed.add_field(name="Für mehr Befehle nutze", value=f"{get_prefix(client,ctx)}Befehle", inline=False)

    await ctx.send(embed = embed)

@client.event
async def on_member_join(member):
  guild = client.get_guild(900038689659433020)
  
  welcomeEmbed = discord.Embed(title = f"Neues Mitglied!", description = f"{member.mention} ist dem Server beigetreten!", color = discord.Color.blue())

  await client.get_channel(900038689659433023).send(embed = welcomeEmbed)

@client.event
async def on_member_leave(member):
  guild = client.get_guild(900038689659433020)
  
  welcomeEmbed = discord.Embed(title = f"Neues Mitglied!", description = f"{member.mention} ist dem Server beigetreten!", color = discord.Color.blue())

  await client.get_channel(900038689659433023).send(embed = welcomeEmbed)

def is_not_pinned(mess):
  return not mess.pinned

@client.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    if amount==None:
     amount=0
    if amount>=101 or amount <=0:
     amount=2


    await channel.delete_messages(messages)
    embed =  discord.Embed(
      title = f" {amount} **Nachricht(en) erfolgreich entfernt**  :wastebasket: ", 
      colour = 0x8f8f8e
     )

    await ctx.send(embed = embed)


@client.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def Clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    if amount==None:
     amount=0
    if amount>=101 or amount <=0:
     amount=2


    await channel.delete_messages(messages)
    embed =  discord.Embed(
      title = f" {amount} **Nachricht(en) erfolgreich entfernt**  :wastebasket: ", 
      colour = 0x8f8f8e
     )

    await ctx.send(embed = embed)

@client.command(aliases = ["Befehle"])
async def befehle(ctx):
    embed =  discord.Embed(
      title = f"Hier ist eine Liste meiner Befehle",
      colour = 0x0500ff
     )

    embed.add_field(name=f"**-----------------------------------------------**", value=f"**__ALLGEMEINES__**",  inline=False)
    embed.add_field(name=f"{get_prefix(client,ctx)}Info ", value=f"Zeigt Informationen über den Bot")
    embed.add_field(name=f"{get_prefix(client,ctx)}Help", value=f"Zeigt eine Hilfs-Nachricht")
    embed.add_field(name=f"{get_prefix(client,ctx)}Changeprefix [Prefix]", value=f"Ändert den Prefix des Bots")
    embed.add_field(name=f"{get_prefix(client,ctx)}Clear [Zahl]", value=f"Löscht eine gewünschte Anzahl an Nachrichten")
    embed.add_field(name=f"{get_prefix(client,ctx)}Ping", value=f"Zeigt den Ping des Bots")
    embed.add_field(name=f"{get_prefix(client,ctx)}balalab", value=f"baab rindedrnhgk")
    embed.add_field(name=f"**-----------------------------------------------**", value=f"**__MUSIK__**",  inline=False)
    embed.add_field(name=f"{get_prefix(client,ctx)}Join ", value=f"juckt mich nicht")
    embed.add_field(name=f"{get_prefix(client,ctx)}Disconnect ", value=f"juckt mich nicht")
    embed.add_field(name=f"{get_prefix(client,ctx)}Play ", value=f"juckt mich nicht")

    await ctx.send(embed = embed)

@client.command(aliases = ["spieler"])
async def Spielerzahl(ctx):
    embed =  discord.Embed(
      title = f"GommeHD.net Spieleranzahl",
      colour = 0x0500ff
     )
      
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
      "Accept": "*/*",
      "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
      "Content-Type": "application/json",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-site",
      "DNT": "1",
      "Sec-GPC": "1"
    }
    payload = {"operationName":None,"variables":{},"query":"{\n  clan {\n    totalCount\n    __typename\n  }\n}\n"}

    r = requests.post("https://www.gommehd.net/graphql", data=payload, headers=headers)
    print(r.text)
    embed.description = r.json()

    await ctx.send(embed = embed)

#https://aws.random.cat/meow?ref=apilist.fun

@client.command(aliases = ["cat", "Katze"])
async def cats(ctx):
    embed =  discord.Embed(
      title = f"Katze↓",
      colour = 0x0500ff
     )
    r = requests.post("https://aws.random.cat/meow?ref=apilist.fun").json()
    print(r)
    embed.set_image(url=r["file"])
    await ctx.send(embed = embed)
"""
@client.command(aliases = ["cat", "Katze"])
async def cats(ctx):
    embed =  discord.Embed(
      title = f"Random Bild↓",
      colour = 0x0500ff
     )
    print(r)
    embed.set_image(url=r["file"])
    await ctx.send(embed = embed)
"""
@client.command(aliases = ["im", "bild"])
async def image(ctx):
    uuid = uuid4()
    print(uuid)
    string = str(uuid)[0: 6]
    print(string)
    await ctx.send(f"https://prnt.sc/{string}")

@client.command(aliases = ["wysi", "roll"])
async def rollen(ctx):
    number = randint(0,1100)
    if number > 1000:
      number = 727
    await ctx.send(str(number))


keep_alive()
client.run(os.environ['TOKEN'])
