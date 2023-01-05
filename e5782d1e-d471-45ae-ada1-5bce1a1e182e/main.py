#import discord
import re, unicodedata
import os
import time
import datetime
from discord.ext import commands
from webserver import keep_alive

  
fakeMute = []

start_time = time.time()

def Find(string):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]


def Contains(arr,mess,must=False):
    
    mess = ''.join(filter( lambda x: x in '0123456789abcdefghijklmnopqrstuvwxyz', mess ))
    Contains = True
    for i in arr:
        Contains = i in mess and (must and Contains or True) or False

    
    return Contains
def AlphanumericScan(arr):
    for mess in arr:
        for char in mess:
            try:
              char = unicodedata.name(char)
              if 'SMALL LETTER' in char and not char.startswith("LATIN"):
                  return True
            except:
              pass
client = commands.Bot(command_prefix='.', yycase_insensitive=True)

@client.command()
async def test():
  print("hi")

def scamCheck(message):
    embeds = message.embeds
    Scam = 0
    Message = ""
    if 'discord.gg/' in message.content:
        if message.content.split("discord.gg/")[1].split(" ")[0] != "":
            Scam = True
            Message = "Discord invite detected"
            return Scam, Message
    if len(embeds) == 0:
        if ('free' and 'nitro' in message.content.lower()):
            urls = Find(message.content.lower())
            
            for i in urls:
                i = i.replace("https://","")
                i = i.replace("http://","")
                if not Contains(['free','nitro'],i,True):
                    if not i.startswith("discord.gift") and not i.startswith("discord.com") and not i.startswith('discordapp.com'):
                        Scam += 1
                        Message = "Possible scam link detected."
    else:
        for embed in embeds:
           jsonEmbed = embed.to_dict()
           if not 'url' in jsonEmbed: return (False, False)
           url = jsonEmbed['url'].replace("https://","")
           url = jsonEmbed['url'].replace("http://","")               
           if 'provider' not in jsonEmbed:
               jsonEmbed['provider'] = {}
               jsonEmbed['provider']['name'] = ""
           if not url.startswith("discord.com") and not url.startswith("discord.gift"):
                result = AlphanumericScan([jsonEmbed['title'].lower(),jsonEmbed['description'].lower(),jsonEmbed['provider']['name'].lower()])
                if result:
                    Scam += 5
                    break
                
                if 'nitro' in jsonEmbed['title'].lower() and 'free' in jsonEmbed['title'].lower() and 'month' in jsonEmbed['title'].lower():
                    Scam += 5
                elif 'discord has gifted' in jsonEmbed['title'].lower() and jsonEmbed['provider']['name'].lower() == 'disсоrd':
                    Scam += 5
                elif Contains(['upgrade','emoji','file','stand','favourite'],jsonEmbed['description'].lower()) and jsonEmbed['provider']['name'].lower() == 'disсоrd':
                    Scam += 5
                elif Contains(['month','nitro','from'],jsonEmbed['title'].lower()):
                    Scam += 5
                elif Contains(['you','gifted'],jsonEmbed['title'].lower()):
                    Scam += 5
    if Scam > 0:
        org = str((Scam/7)*100+0.5)
        Chance = float(org.split(".")[0]+'.'+org.split(".")[1][0:2])
    if Scam > 0 and Scam < 2:
        return (True, f'Possible scam link detected.')
    elif Scam > 1:
        return (True, f'Scam link detected. {Chance}%')
    return (False, False)
    

@client.event
async def on_ready():
    
    print(f"Logged in as {client.user.name}\n{client.user.id}")
  

@client.command(pass_context=True)
async def uptime(ctx):
    print("hi")
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=0xc8dc6c)
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text="<bot name>")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("Current uptime: " + text)

@client.event
async def on_message(message):
   
    if message.content.startswith(".checkmark"):
      await message.add_reaction("<:Tick:926436686173454356>")
    Scam, Message = scamCheck(message)
    if Scam:
        print(message.author.name)
        await message.author.send(Message)
        await message.delete()
        #await message.add_reaction("<:Cross:926436660911144990>")
        #await message.remove_reaction("<:Tick:926436686173454356>", client.user)
        #await message.reply(Message, mention_author = True)
    else:
        if "http" in message.content:
            await message.add_reaction("<:Tick:926436686173454356>")

@client.event
async def on_message_edit(before, after):
    Scam, Message = scamCheck(after)
    if Scam:
        print(after.author.name)
        await after.author.send(Message)
        await after.delete()
        #await after.add_reaction("<:Cross:926436660911144990>")
        
    else:
        if "http" in after.content:
            await after.add_reaction("<:Tick:926436686173454356>")
    
            

keep_alive()

TOKEN = os.environ['DISCORD_BOT_SECRET']

client.run(TOKEN) 



