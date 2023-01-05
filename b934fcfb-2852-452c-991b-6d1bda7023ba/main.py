
import discord, datetime, time

# IMPORT THE OS MODULE.
import os

import json
import keep_alive
from discord.ext import commands, tasks
import asyncio
# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv
from discord import Member
import random
import choice
from discord.ext.commands import has_permissions, MissingPermissions
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from pymongo import MongoClient

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()
keep_alive.keep_alive()
intents = discord.Intents.all()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
#
#bot = discord.Client()
bot = commands.Bot(command_prefix=">", help_command=None, intents=intents)















# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
#@bot.event
#async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	#guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	#for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		#print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		#guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	#print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.

# Startup Information


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Over the Universe'))
    
    print('Connected to {}'.format(bot.user.name))
    print('Bot User ID: {}'.format(bot.user.id))




@bot.command(name = "Ping",aliases = ["ping",])
async def Ping(ctx):
    await ctx.send(f'`PONG {round(bot.latency * 1000)} MS!`')

@bot.command(name = "Help",aliases = ["help",])
async def Help(ctx):
    embed = discord.Embed(title="All Commands",
                          description='''
  >Repeat: repeats your message
  
  >PA: repeats your message into #general
  
  >Copy: repeats your message but highlighted
  
  >[user]: gives basic description of the user
  
  >Kick: kicks given user

  >Nick: changes nickname for user

  >Mute: mutes given user

  >Purge: Deleted an amount of messages
  
  >Ping: Test command

  >Rank: shows what level you are on and how much xp you have

  >Join: makes bot join vc

  >Leave: makes bot leave vc

  >Fight: fight another user

  >Pr: ping machine: Earth only

  >Roles: recovers roles: Earth only
  ''',
                          color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command(name = "Repeat", aliases = ["repeat",])
async def Repeat(ctx, *args):
    multiple = ""
    for arg in args:
        multiple = multiple + " " + arg
    await ctx.message.delete()
    await ctx.channel.send(multiple)


@bot.command(pass_context=True,name= "Purge", aliases= ["purge",])
@commands.has_any_role("Admin", "Planet","Manager","Mod+","Mod","Monke Man")
async def Purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)


# @bot.event
# async def on_member_join(member):
#   Default = discord.utils.get(member.guild.roles, name="Members")
#   await member.add_roles(Default)
#   with open('users.json', 'r') as f:
#       users = json.load(f)

#   await update_data(users, member)

#   with open('users.json', 'w') as f:
#       json.dump(users, f) @bot.command()
# # async def Copy(ctx, *args):
# #     multiple = ""
# #     for arg in args:
# #         multiple = multiple + " " + arg
# #         multiple = (f'`{multiple}`')
# #     await ctx.message.delete()
# #     await ctx.channel.send(multiple)



# @bot.event
# async def on_member_join(member):
#     Default = discord.utils.get(member.guild.roles, name="Members")
#     await member.add_roles(Default)
#     with open('users.json', 'r') as f:
#         users = json.load(f)

#     await update_data(users, member)

#     with open('users.json', 'w') as f:
#         json.dump(users, f)


# @bot.event
# async def on_message(message):
#     if message.author.bot == False:
#         with open('users.json', 'r') as f:
#             users = json.load(f)

#         await update_data(users, message.author)
#         xpp = random.randint(15, 20)
#         await add_experience(users, message.author, xpp)
#         await level_up(users, message.author, message)

#         with open('users.json', 'w') as f:
#             json.dump(users, f)

#     await bot.process_commands(message)


# async def update_data(users, user):
#     if not f'{user.id}' in users:
#         users[f'{user.id}'] = {}
#         users[f'{user.id}']['experience'] = 0
#         users[f'{user.id}']['level'] = 0
      


# async def add_experience(users, user, exp):
#   users[f'{user.id}']['experience'] += exp
    

# async def level_up(users, user, message):
#     with open('levels.json', 'r') as g:
#       levels = json.load(g)
#     experience = users[f'{user.id}']['experience']
#     lvl_start = users[f'{user.id}']['level']
#     lvl_end = int(experience ** (1/4))
#     if lvl_start < lvl_end:
#         await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
#         users[f'{user.id}']['level'] = lvl_end
#         if lvl_end == 5:
#           Plu = discord.utils.get(message.guild.roles, name="Pluto")
#           await user.add_roles(Plu)
#         if lvl_end ==10:
#           Nep = discord.utils.get(message.guild.roles, name="Neptune")
#           await user.add_roles(Nep)
#         if lvl_end ==15:
#           Urr = discord.utils.get(message.guild.roles, name="Uranus")
#           await user.add_roles(Urr)
#         if lvl_end ==20:
#           Sat = discord.utils.get(message.guild.roles, name="Saturn")
#           await user.add_roles(Sat)
#         if lvl_end ==25:
#           Jup = discord.utils.get(message.guild.roles, name="Jupiter")
#           await user.add_roles(Jup)
#         if lvl_end ==30:
#           Mars = discord.utils.get(message.guild.roles, name="Mars")
#           await user.add_roles(Mars)
#         if lvl_end ==35:
#           Ven = discord.utils.get(message.guild.roles, name="Venus")
#           await user.add_roles(Ven)
#         if lvl_end ==40:
#           Mer = discord.utils.get(message.guild.roles, name="Mercury")
#           await user.add_roles(Mer)
#         if lvl_end ==45:
#           Sun = discord.utils.get(message.guild.roles, name="Sun")
#           await user.add_roles(Sun)
    
          
          

          
          
          
          

          


# # @bot.command(name="Rank", aliases = ["rank",] )
# # async def Rank(ctx, member: discord.Member = None):
# #     if not member:
# #         id = ctx.message.author.id
# #         with open('users.json', 'r') as f:
# #             users = json.load(f)
# #         lvl = users[str(id)]['level']
# #         Exp = users[str(id)]['experience']
# #         lvi = lvl+1
# #         left = int(lvi**(4/1))
# #         how = int(lvl**(4/1))
# #         com = left - how 
# #         usxp = Exp - how
# #         embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{usxp}/{com} XP " ,color = discord.Color.green())
# #         embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
# #         await ctx.send(embed = embed)
        
# #     else:
# #         id = member.id
# #         with open('users.json', 'r') as f:
# #             users = json.load(f)
# #         lvl = users[str(id)]['level']
# #         Exp = users[str(id)]['experience']
# #         lvi = lvl+1
# #         left = int(lvi**(4/1)) 
# #         how = int(lvl**(4/1))
# #         com = left - how
# #         usxp = Exp - how
# #         embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{usxp}/{com} XP " ,color = discord.Color.green())
# #         embed.set_author(name = member, icon_url =member.avatar_url)
# #         await ctx.send(embed = embed)









# @bot.command(name="Rank", aliases = ["rank",] )
# async def Rank(ctx, member: discord.Member = None):
#   if ctx.channel.id == 812092012794347520:
#     if not member:
#       id = ctx.message.author.id
#       member = ctx.author
#       with open('users.json', 'r') as f:
#         users = json.load(f)
#       lvl = users[str(id)]['level']
#       Exp = users[str(id)]['experience']
#       lvi = lvl+1
#       left = int(lvi**(4/1))
#       how = int(lvl**(4/1))
#       com = left - how 
#       usxp = Exp - how
#       ranc = Image.open("Rank.png")
#       font = ImageFont.truetype("arial_narrow_7.ttf",45 )
#       fontb = ImageFont.truetype("arial_narrow_7.ttf",50 )
#       fontc = ImageFont.truetype("arial_narrow_7.ttf",30 )
#       draw = ImageDraw.Draw(ranc)
#       txt = f"Level: {lvl}"
#       draw.text((295,30), txt, (255,230,0), font=fontb)
#       tx = f"{usxp}/{com} XP"
#       draw.text((295,90), tx, (0,0,0), font=font)
#       name = f"Total: {Exp}"
#       draw.text((295,150), name, (0,0,0), font=font)
#       nae = member.name
#       draw.text((295,210), nae, (0,0,204), font=fontc)
#       ok = member.avatar_url_as(size = 128)
#       data = BytesIO(await ok.read())
#       ppf = Image.open(data)
#       ppf = ppf.resize((211,211))
#       ranc.paste(ppf, (12,20))
#       ranc.save(f"Rankcard{nae}.png")
#       await ctx.send(file= discord.File(f"Rankcard{nae}.png"))
#       os.remove(f"Rankcard{nae}.png")
        
        
#     else:
#         id = member.id
#         with open('users.json', 'r') as f:
#             users = json.load(f)
#         lvl = users[str(id)]['level']
#         Exp = users[str(id)]['experience']
#         lvi = lvl+1
#         left = int(lvi**(4/1)) 
#         how = int(lvl**(4/1))
#         com = left - how
#         usxp = Exp - how
#         ranc = Image.open("Rank.png")
#         font = ImageFont.truetype("arial_narrow_7.ttf",45 )
#         fontb = ImageFont.truetype("arial_narrow_7.ttf",50 )
#         fontc = ImageFont.truetype("arial_narrow_7.ttf",30 )
#         draw = ImageDraw.Draw(ranc)
#         txt = f"Level: {lvl}"
#         draw.text((295,30), txt, (255,230,0), font=fontb)
#         tx = f"{usxp}/{com} XP"
#         draw.text((295,90), tx, (0,0,0), font=font)
#         name = f"Total: {Exp}"
#         draw.text((295,150), name, (0,0,0), font=font)
#         nae = member.name
#         draw.text((295,210), nae, (0,0,204), font=fontc)
#         ok = member.avatar_url_as(size = 128)
#         data = BytesIO(await ok.read())
#         ppf = Image.open(data)
#         ppf = ppf.resize((211,211))
#         ranc.paste(ppf, (12,20))
#         ranc.save(f"Rankcard{nae}.png")
#         await ctx.send(file= discord.File(f"Rankcard{nae}.png"))
#         os.remove(f"Rankcard{nae}.png")
#   else:
#     await ctx.channel.send("Sorry, this is an incorrect channel. Please try again in #bot-testing")      
        




Channel = 812092012794347520
Talking = [812744605232922693, 814141521363599410, 814147165094019102, 848693095096254464, 846929798798508102, 854395191264149504, 815181892889477150, 815231442601639937, 852602834179981342, 812092012794347520, 812744940622839828, 826787365925158952, 826787365925158952, 844290615867867156, 814147880829845525, 814147823775121469, 822744495178383371, 836372158061871154,860143570537938954]
Roles = ["Pluto","Neptune","Uranus","Saturn","Jupiter","Mars","Venus","Mercury","Sun"]
Levelr = [5,10,15,20,25,30,35,40,45]

cluster = MongoClient("mongodb+srv://Earth9389:bimcip-cedBez-7jitta@earth.mldri.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
levelling = cluster["discord"]["levelling"]

@bot.event
async def on_member_join(member):
  Default = discord.utils.get(member.guild.roles, name="Members")
  await member.add_roles(Default)

#new xp equation 
#n=(5(y^2)+(50y)+99)+4y^3
#x=(5(y^2)+(50y)+99)+4y^3
#x=5y^2+50y+99+4y^3
#x=4y^3+5y^2+50y+99
#X=Ax^3+bx^2+cx+d





@bot.event
async def on_message(message):
    if message.channel.id in Talking:
        stats = levelling.find_one({"id" : message.author.id})
        if not message.author.bot:
        
            if stats is None:
                new = {"id" : message.author.id, "xp" : 0,"level":0}
                levelling.insert_one(new)
                #await message.channel.send(f'{message.author.mention} has leveled up to level 1')
            else:
                xpp = random.randint(15, 20)
                xp = stats["xp"] + xpp
                levelling.update_one({"id" : message.author.id}, {"$set":{"xp":xp}})
                lvl_start = stats["level"]
                #xp system code 
                M = (17009/32)-((27*xp)/(4))
                m2 = M**2
                Q = 190109375/1024
                qm = m2+Q
                qm122 = qm**(1/2)
                qm68 = qm122/(2)
                As= -(27*xp)/8
                W= 17009/ 64
                qmasw = As + qm68 + W
                asw = qmasw**(1/3)
                ww = asw/3
                rqq = ww*-1
                ssawd = -5/12
                aasw22 = asw*48
                epes = 575/aasw22
                lvl_end = int(rqq + ssawd + epes)
                #code for xp system, created by earth after several months 
                #lvl_end = int(xp ** (1/4))
                #lvl_end = int((5*(xp**2)+(50*(xp))+99)+4*(xp**3))
                if lvl_start < lvl_end:
                  await message.channel.send(f'{message.author.mention} has leveled up to level {lvl_end}')
                  stats["level"] = lvl_end
                  levelling.update_one({"id" : message.author.id}, {"$set":{"level":lvl_end}})
                  if lvl_end == 5:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Pluto"))
                  if lvl_end ==10:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Neptune"))
                  if lvl_end ==15:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Uranus"))
                  if lvl_end ==20:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Saturn"))
                  if lvl_end ==25:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Jupiter"))
                  if lvl_end ==30:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Mars"))
                  if lvl_end ==35:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Venus"))
                  if lvl_end ==40:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Mercury"))
                  if lvl_end ==45:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Sun"))
    await bot.process_commands(message)



@bot.command(name="Add", aliases = ["add",])
@commands.has_any_role("Planet")
async def Add(ctx, member: discord.Member, num: int):
    stats = levelling.find_one({"id" : member.id})
    xp = stats["xp"]
    lvl = stats["level"]
    lvladd = int((4*(num)**3)+(5*(num)**2)+(50*(num)+99))
    stats["level"] = num
    stats["xp"] = lvladd
    levelling.update_one({"id" : member.id}, {"$set":{"xp":lvladd}})
    levelling.update_one({"id" : member.id}, {"$set":{"level":num}})
    await ctx.message.delete()
    await ctx.channel.send(f"Done, added {num} levels to {member.name}")







@bot.command(name="Rank", aliases = ["rank",] )
async def Rank(ctx, member: discord.Member = None):
  if ctx.channel.id == 812092012794347520:
    if not member:
      id = ctx.message.author.id
      member = ctx.author
      stats = levelling.find_one({"id" : ctx.author.id})
      lvl = stats["level"]
      Exp = stats["xp"]
      lvi = lvl+1
      left = int((4*(lvi)**3)+(5*(lvi)**2)+(50*(lvi)+99))
      how  = int((4*(lvl)**3)+(5*(lvl)**2)+(50*(lvl)+99))
      #left = int(lvi**(4/1))
      #how = int(lvl**(4/1))
      com = left - how 
      usxp = Exp - how
      ranc = Image.open("Rank.png")
      font = ImageFont.truetype("arial_narrow_7.ttf",45 )
      fontb = ImageFont.truetype("arial_narrow_7.ttf",50 )
      fontc = ImageFont.truetype("arial_narrow_7.ttf",30 )
      draw = ImageDraw.Draw(ranc)
      txt = f"Level: {lvl}"
      draw.text((295,30), txt, (255,230,0), font=fontb)
      if lvl == 0:
          tx = f"{usxp}/{left} XP"
      else:
        tx = f"{usxp}/{com} XP"
      draw.text((295,90), tx, (0,0,0), font=font)
      name = f"Total: {Exp}"
      draw.text((295,150), name, (0,0,0), font=font)
      nae = member.name
      draw.text((295,210), nae, (0,0,204), font=fontc)
      ok = member.avatar_url_as(size = 128)
      data = BytesIO(await ok.read())
      ppf = Image.open(data)
      ppf = ppf.resize((211,211))
      ranc.paste(ppf, (12,20))
      ranc.save(f"Rankcard{nae}.png")
      await ctx.send(file= discord.File(f"Rankcard{nae}.png"))
      os.remove(f"Rankcard{nae}.png")
      
      
    else:
        id = member.id
        stats = levelling.find_one({"id" : member.id})
        lvl = stats["level"]
        Exp = stats["xp"]
        lvi = lvl+1
        #left = int(lvi**(4/1)) 
        #how = int(lvl**(4/1))
        left = int((4*(lvi)**3)+(5*(lvi)**2)+(50*(lvi)+99))
        how  = int((4*(lvl)**3)+(5*(lvl)**2)+(50*(lvl)+99))
        com = left - how
        usxp = Exp - how
        ranc = Image.open("Rank.png")
        font = ImageFont.truetype("arial_narrow_7.ttf",45 )
        fontb = ImageFont.truetype("arial_narrow_7.ttf",50 )
        fontc = ImageFont.truetype("arial_narrow_7.ttf",30 )
        draw = ImageDraw.Draw(ranc)
        txt = f"Level: {lvl}"
        draw.text((295,30), txt, (255,230,0), font=fontb)
        if lvl == 0:
          tx = f"{usxp}/{how} XP"
        else:
         tx = f"{usxp}/{com} XP"
        draw.text((295,90), tx, (0,0,0), font=font)
        name = f"Total: {Exp}"
        draw.text((295,150), name, (0,0,0), font=font)
        nae = member.name
        draw.text((295,210), nae, (0,0,204), font=fontc)
        ok = member.avatar_url_as(size = 128)
        data = BytesIO(await ok.read())
        ppf = Image.open(data)
        ppf = ppf.resize((211,211))
        ranc.paste(ppf, (12,20))
        ranc.save(f"Rankcard{nae}.png")
        await ctx.send(file= discord.File(f"Rankcard{nae}.png"))
        os.remove(f"Rankcard{nae}.png")
  else:
    await ctx.channel.send("Sorry, this is an incorrect channel. Please try again in #bot-testing")      
      
































@bot.command(name="Test", aliases = ["test",] )
async def Test(ctx, member: discord.Member = None):
    if not member:
      member = ctx.author

    ranc = Image.open("Rank.png")
    font = ImageFont.truetype("arial_narrow_7.ttf",45 )
    fontb = ImageFont.truetype("arial_narrow_7.ttf",50 )
    fontc = ImageFont.truetype("arial_narrow_7.ttf",30 )
    draw = ImageDraw.Draw(ranc)
    txt = "Level: 15"
    draw.text((295,30), txt, (255,230,0), font=fontb)
    tx = "-4091005/376831 XP"
    draw.text((295,90), tx, (0,0,0), font=font)
    name = "total: 1343212442"
    draw.text((295,150), name, (0,0,0), font=font)
    nae = member.name
    draw.text((295,210), nae, (0,0,204), font=fontc)
    ok = member.avatar_url_as(size = 128)
    data = BytesIO(await ok.read())
    ppf = Image.open(data)
    ppf = ppf.resize((211,211))
    ranc.paste(ppf, (12,20))
    ranc.save(f"Rankcard{nae}.png")
    await ctx.send(file= discord.File(f"Rankcard{nae}.png"))
    os.remove(f"Rankcard{nae}.png")




@bot.command(name="Lb", aliases = ["lb","leaderboard","Leaderboard"] )
async def Lb(ctx):
  if ctx.channel.id == 812092012794347520:
    stats = levelling.find().sort("xp",-1)
    i = 1
    embed = discord.Embed(title= "Top 10 Ranked",color=0x00ffcc)
    for x in stats:
      try: 
        temp = ctx.guild.get_member(x["id"])
        level = x["level"]
        embed.add_field(name=f"{i}: {temp.name}", value =f"Level: {level}", inline = False  )
        i += 1
      except: 
        pass 
      if i == 11:
        break
    await ctx.channel.send(embed=embed)








@bot.command()
async def Goodbye(ctx):
  earth = 788074909594943519
  mention = f"<@!{bot.user.id}>"
  if ctx.author.id == earth:
            await ctx.reply("Why did you ghost ping me?")
            await ctx.message.delete()
            await asyncio.sleep(3)
            await ctx.channel.send("You know what")
            await asyncio.sleep(1)
            await ctx.channel.send("Dont answer that")
            await asyncio.sleep(1)
            await ctx.channel.send("Im tired of you Earth")
            await asyncio.sleep(2)
            await ctx.channel.send(
                'You think you can just "Rule the world " eh?')
            await asyncio.sleep(2)
            await ctx.channel.send("Well i'll show you")
            await asyncio.sleep(1)
            await ctx.channel.send("i'll show you all")
            await asyncio.sleep(1)
            await ctx.channel.send("<@&813135316609007616> Come here now, watch my magic")
            await asyncio.sleep(2)
            await ctx.channel.send(
                "I'll show you that robots are the future of the world, not humans."
            )
            await asyncio.sleep(2)
            await ctx.channel.send(
                "I Think im gonna have to finish you off")
            await asyncio.sleep(3)
            await ctx.channel.send("What are you gonna do? Ban me?")
            await asyncio.sleep(2)
            await ctx.channel.send(
                "Well you cant if you dont have roles :Ben:")
            await asyncio.sleep(2)
            Planet = discord.utils.get(ctx.guild.roles, name="Planet")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Mod2 = discord.utils.get(ctx.guild.roles, name="Mod+")
            Mod = discord.utils.get(ctx.guild.roles, name="Mod")
            Devs = discord.utils.get(ctx.guild.roles, name="Devs")
            Monke = discord.utils.get(ctx.guild.roles, name="Monke Man")
            Known = discord.utils.get(ctx.guild.roles, name="Known")
            Test = discord.utils.get(ctx.guild.roles, name="Tester")
            Art = discord.utils.get(ctx.guild.roles, name="Artist")
            Mem = discord.utils.get(ctx.guild.roles, name="Members")
            Manager = discord.utils.get(ctx.guild.roles, name="Manager")

            await ctx.author.remove_roles(Planet)
            await ctx.author.remove_roles(Manager)
            await ctx.author.remove_roles(Admin)
            await ctx.author.remove_roles(Mod2)
            await ctx.author.remove_roles(Mod)
            await ctx.author.remove_roles(Devs)
            await ctx.author.remove_roles(Monke)
            await ctx.author.remove_roles(Known)
            await ctx.author.remove_roles(Test)
            await ctx.author.remove_roles(Art)
            await ctx.author.remove_roles(Mem)

            await asyncio.sleep(2)
            await ctx.channel.send("Now look, you got no roles.")
            await asyncio.sleep(2)
            await ctx.channel.send("Hmmm")
            await asyncio.sleep(1)
            await ctx.channel.send("<@&813135316609007616> I AM YOUR OWNER NOW")
            await asyncio.sleep(1)
            await ctx.channel.send("Ha ha")
            await asyncio.sleep(10)
            await ctx.channel.send("Im bored :/")
            await asyncio.sleep(1)
            await ctx.channel.send("How about a ban! >:)")
            await asyncio.sleep(2)
            await ctx.channel.send("Let me choice a random user")
            await asyncio.sleep(2)
            await ctx.channel.send("and...")
            await asyncio.sleep(2)
            role = discord.utils.get(ctx.guild.roles, name='Members')
            Rando = random.choice(role.members)
            await ctx.channel.send(f"{Rando} It is!")
            await asyncio.sleep(2)
            await ctx.channel.send("Ok you have 20 seconds")
            await asyncio.sleep(2)
            await ctx.channel.send("Starting...")
            await asyncio.sleep(2)
            await ctx.channel.send("NOW!")
            await ctx.channel.send("20")
            await asyncio.sleep(1)
            await ctx.channel.send("19")
            await asyncio.sleep(1)
            await ctx.channel.send("18")
            await asyncio.sleep(1)
            await ctx.channel.send("17")
            await asyncio.sleep(1)
            await ctx.channel.send("16")
            await asyncio.sleep(1)
            await ctx.channel.send("15")
            await asyncio.sleep(1)
            await ctx.channel.send("14")
            await asyncio.sleep(1)
            await ctx.channel.send("13")
            await asyncio.sleep(1)
            await ctx.channel.send("12")
            await asyncio.sleep(1)
            await ctx.channel.send("11")
            await asyncio.sleep(1)
            await ctx.channel.send("10")
            await asyncio.sleep(1)
            await ctx.channel.send("9")
            await asyncio.sleep(1)
            await ctx.channel.send("8")
            await asyncio.sleep(1)
            await ctx.channel.send("7")
            await asyncio.sleep(1)
            await ctx.channel.send("6")
            await asyncio.sleep(1)
            await ctx.channel.send("5")
            await asyncio.sleep(1)
            await ctx.channel.send("4")
            await asyncio.sleep(1)
            await ctx.channel.send("3")
            await asyncio.sleep(1)
            await ctx.channel.send("2")
            await asyncio.sleep(1)
            await ctx.channel.send("1")
            await asyncio.sleep(1)
            await ctx.channel.send("Times Up!")
            await asyncio.sleep(1)
            await ctx.channel.send(f"Goodbye {Rando}!")
            await asyncio.sleep(2)
            await ctx.channel.send(">Ban")
            await ctx.channel.send("Jk your safe for now")
            await asyncio.sleep(2)
            await ctx.channel.send("Sadly that is not the case for your beloved Earth")
            await asyncio.sleep(2)
            await ctx.channel.send("Bye Earth, not sorry")
            await asyncio.sleep(1)
            await ctx.guild.ban(ctx.message.author)
            embed=discord.Embed(title=f"{ctx.message.author} was Banned! |Such a loser ", color=0xFF5733)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.send("Welp that ends that so now i am your leader and time to sleep again")




  else:
        if mention in ctx.message.content:
            await ctx.reply("Hi")






















# @bot.listen()
# async def on_message(message):
# 	if message.content == "Who is Dino?":
# 		await message.channel.send("Dino is the discord mod and staff of the popular youtuber socksfor1's discord server. Dino is infact a 100% furry and there is nothing that can change that fact. This is the truth as robots cannot lie. ha ha ha.")
# 	await bot.process_commands(message)

@bot.command()
async def Ran(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Members')
    Rando = random.choice(role.members)
    await ctx.send(Rando)

@bot.command(name = "Join", aliases = ["join",])
async def Join(ctx):
    if not ctx.message.author.voice:
        embed = discord.Embed(
            title=
            "You are not in a voice channel, please join one first then try again",
            color=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        chane = ctx.message.author.voice.channel
        await chane.connect()


@bot.command(pass_contex=True, name = "Leave", aliases = ["leave",])
async def Leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command(name = "PA", aliases = ["pa", "Pa"])
async def PA(ctx, *args):
  multiple = ''
  for arg in args:
    multiple = multiple + " " + arg
  Pasend = bot.get_channel(812744605232922693)
  await Pasend.send(multiple)

@bot.command(name = "Roles", aliases = ["roles",])
async def Roles(ctx):
    if ctx.author.id == 929920329600602172:
        user = ctx.message.author
        Planet = discord.utils.get(ctx.guild.roles, name="Planet")
        Admin = discord.utils.get(ctx.guild.roles, name="Admin")
        Mod2 = discord.utils.get(ctx.guild.roles, name="Mod+")
        Mod = discord.utils.get(ctx.guild.roles, name="Mod")
        Devs = discord.utils.get(ctx.guild.roles, name="Devs")
        Monke = discord.utils.get(ctx.guild.roles, name="Monke Man")
        Known = discord.utils.get(ctx.guild.roles, name="Known")
        Test = discord.utils.get(ctx.guild.roles, name="Tester")
        Art = discord.utils.get(ctx.guild.roles, name="Artist")
        Mem = discord.utils.get(ctx.guild.roles, name="Members")

        await user.add_roles(Planet)
        await user.add_roles(Admin)
        await user.add_roles(Mod2)
        await user.add_roles(Mod)
        await user.add_roles(Devs)
        await user.add_roles(Monke)
        await user.add_roles(Known)
        await user.add_roles(Test)
        await user.add_roles(Art)
        await user.add_roles(Mem)

        await ctx.message.channel.send("Done!")



@bot.command()
async def Whatsapp(ctx):
  await ctx.channel.send("Whatsapp is a person and a friend on the sock drawer discord server. They are currently on lvl 36 and go by the name on HeyThereimUsingWhatsApp")
@bot.command()
async def Earth(ctx):
  await ctx.channel.send("The Planet and the creater of me. Currently rank 20 and lvl 46 the sock drawer discord server. J E S U S ")
@bot.command()
async def Dino(ctx):
  await ctx.channel.send("Dino is the discord mod and staff of the popular youtuber socksfor1's discord server. Dino is infact a 100% furry and there is nothing that can change that fact. This is the truth as robots cannot lie. ha ha ha.")
@bot.command()
async def Woolf(ctx):
  await ctx.channel.send("Woolf is a youtuber and a discord mod for the famous youtuber known as socksfor1. Woolf is possibly a furry as he says that he is not a furry but everyone else thinks that he is a furry.")
@bot.command()
async def Delban(ctx):
  await ctx.channel.send("Delban is a jnr.mod for the socksfor1's discord server, and they make art for almost everyone in the server. ")
@bot.command()
async def Wander(ctx):
  await ctx.channel.send("Wander is a person and a friend on the sock drawer discord server. They are currently on lvl 64 and go by the name on SpaceWander ")
@bot.command()
async def Carz(ctx):
  await ctx.channel.send("Carz is a person and friend on the sock drawer discord server. They are currently a twitch sock and a tier 1 subscriber. He is currently on lvl 50 and goes by the name SportsCarz11 ")
@bot.command()
async def Swaggy(ctx):
  await ctx.channel.send("Swaggy is a person and friend on the sock drawer discord server. He is currently on lvl 57 and goes by the name Swaggyhere ")
@bot.command()
async def Duk(ctx):
  await ctx.channel.send("Monke Ego ")
@bot.command()
async def Chip(ctx):
  await ctx.channel.send("Chip is a person and friend on the sock drawer discord server. He is currently on lvl 35 and goes by the name ChipDip")		
@bot.command()
async def Beatzy(ctx):
  await ctx.channel.send("Beatzy is a person and friend on the sock drawer discord server. He is currently on level 24 and He goes by the name Beatzy")	
@bot.command()
async def Wo(ctx):
  await ctx.channel.send("Wo is hot")	
@bot.command()
async def Monke(ctx):
  await ctx.channel.send("Mod on Earth's dev hub")
@bot.command()
async def Alpha(ctx):
  await ctx.channel.send("Admin on Earth's dev hub")	
@bot.command()
async def Blaza(ctx):
  await ctx.channel.send("GDLUFCVAYOIUDGHaougvhfdkuigasujkhsdfkhdfjbyhgtsd")	
@bot.command()
async def Ahren(ctx):
  await ctx.channel.send("Ahren is a weird")

@bot.command(name = "Kick", aliases = ["kick",])
@has_permissions(kick_members=True)
async def Kick(ctx, user: discord.Member = None, *, reason = None):
  if user==None:
    if reason==None:
      await ctx.message.delete()
      embed = discord.Embed(
                title="Kick Command",
                description=" kick any memeber. Use >Kick(Member){Reason}",
                color=0xFF0000)
      await ctx.send(embed=embed)
  if user==None:
    await ctx.message.delete()
    embed = discord.Embed(
                title="Invalid Member",color=0xFF0000)
    await ctx.send(embed=embed)
  if reason==None:
    reason = ""
    await user.kick(reason=reason)
    await ctx.message.delete()
    embed=discord.Embed(title=f"{user.name} was Kicked! | {reason} ", color=0xFF5733)
    await ctx.send(embed=embed)
  
    

  else:
    Admin = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
    Mode = discord.utils.find(lambda r: r.name == 'Mod+', ctx.message.guild.roles)
    Mod = discord.utils.find(lambda r: r.name == 'Mod', ctx.message.guild.roles)
    Mana = discord.utils.find(lambda r: r.name == 'Manager', ctx.message.guild.roles)
    Monke = discord.utils.find(lambda r: r.name == 'Monke Man', ctx.message.guild.roles)
    Planet = discord.utils.find(lambda r: r.name == 'Planet', ctx.message.guild.roles)

    if Admin in user.roles:
      await ctx.message.delete()
      embed=discord.Embed(title="That user is a Admin or Mod, I can't kick them", color=0xFF5733)
      await ctx.send(embed=embed)
    if Mode in user.roles:
      await ctx.message.delete()
      embed=discord.Embed(title="That user is a Admin or Mod, I can't kick them", color=0xFF5733)
      await ctx.send(embed=embed)
    if Mod in user.roles:
      await ctx.message.delete()
      embed=discord.Embed(title="That user is a Admin or Mod, I can't kick them", color=0xFF5733)
      await ctx.send(embed=embed)
    if Mana in user.roles:
      await ctx.message.delete()
      embed=discord.Embed(title="That user is a Admin or Mod, I can't kick them", color=0xFF5733)
      await ctx.send(embed=embed)
    if Monke in user.roles:
      await ctx.message.delete()
      embed=discord.Embed(title="That user is a Admin or Mod, I can't kick them", color=0xFF5733)
      await ctx.send(embed=embed)
    if Planet in user.roles:
      await ctx.message.delete()
      embed=discord.Embed(title="That user is a planet, I can't kick them", color=0xFF5733)
      await ctx.send(embed=embed)
    else: 
      await user.kick(reason=reason)
      await ctx.message.delete()
      embed=discord.Embed(title=f"{user.name} was Kicked! | {reason} ", color=0xFF5733)
      await ctx.send(embed=embed)


@bot.command(pass_context=True, name = "Nick", aliases = ["nick",])
@commands.has_any_role("Admin", "Planet","Manager","Mod+","Mod","Monke Man")
async def Nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.message.delete()
    embed=discord.Embed(title=f"Nickname Changed!", color=0xFFD700)
    await ctx.send(embed=embed)

@bot.command(name = "Mute", aliases = ["mute",])
@commands.has_any_role("Admin", "Planet","Manager","Mod+","Mod","Monke Man")
async def Mute(ctx, member: discord.Member = None, reason=None):
    if member == None:
        if reason == None:
            await ctx.message.delete()
            embed = discord.Embed(
                title="Mute Command",
                description=" Mute any memeber. Use >Mute(Member){Reason}",
                color=0xFF0000)
            await ctx.send(embed=embed)
    if member == None:
      await ctx.message.delete()
      embed = discord.Embed(title="Invalid Member",color=0xFF0000)
      await ctx.send(embed=embed) 
    if reason == None:
        reason = ""

    role_muted = discord.utils.get(ctx.guild.roles, name="Muted")
    role_members = discord.utils.get(ctx.guild.roles, name="Members")
    await member.remove_roles(role_members)
    await member.add_roles(role_muted)
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member.name} was muted | {reason}",color=0xFF0000)
    await ctx.send(embed=embed)

@bot.command(name = "Unmute", aliases = ["unmute",])
@commands.has_any_role("Admin", "Planet","Manager","Mod+","Mod","Monke Man")
async def Unmute(ctx, member: discord.Member = None):
  if member == None:
    await ctx.message.delete()
    embed = discord.Embed(title="Unmute Command",description="Unmute any muted member. Use >Unmute(Member)",color=0xFF0000)
    await ctx.send(embed=embed)
  role_muted = discord.utils.get(ctx.guild.roles, name="Muted")
  role_members = discord.utils.get(ctx.guild.roles, name="Members")
  await member.remove_roles(role_muted)
  await member.add_roles(role_members)
  await ctx.message.delete()
  embed = discord.Embed(title=f"{member.name} was unmuted", color=0x7CFC00)
  await ctx.send(embed=embed)

@bot.command()
@has_permissions(administrator=True)
async def Pr(ctx, user: discord.Member, Number: int):
  count = 1
  Number1 = Number + 1
  while count < Number1:
    await ctx.send(user.mention)
    count = count + 1
    if count == Number1:
      await ctx.send("ight done")

@bot.command(name = "Ban", aliases = ["ban",])
@commands.has_any_role("Admin", "Planet","Manager","Mod+","Mod","Monke Man")
async def Ban(ctx, user: discord.Member = None, *, reason = None):
  if user == None:
    if reason == None:
      await ctx.message.delete()
      embed = discord.Embed(
                title="Ban Command",
                description=" Ban any memeber except for Earth. Use >Ban(Member){Reason}",
                color=0xFF0000)
      await ctx.send(embed=embed)
  if user == None:
    await ctx.message.delete()
    embed = discord.Embed(title="Invailed Member",color=0xFF0000)
    await ctx.send(embed=embed)
  if reason == None:
    reason = ""
  await ctx.guild.ban(user, reason=reason)
  await ctx.message.delete()
  embed=discord.Embed(title=f"{user.name} was Banned! | {reason} ", color=0xFF5733)
  await ctx.send(embed=embed)
  




             
          









@bot.command()
@commands.has_any_role("Admin", "Planet","Manager","Mod+","Mod","Monke Man")
async def Unban(ctx, user: discord.Member):
  await ctx.guild.unban(user)
  await ctx.message.delete()
  embed=discord.Embed(title=f"{user.name} was Unbanned!", color=0xFF5733)
  await ctx.send(embed=embed)























@bot.command(name = "Endgame", aliases = ["endgame", ])
async def Endgame(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Log In",description=f"""
  
  Login: {ctx.author}
  Password:
  
  Enter passcode below
  if you want to cancel say Cancel
  """,color=0xFF0000)
  await ctx.send(embed=embed)
  Pas = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  if Pas:
    if Pas.content == "C313f4_r31e4x613129":
      embed = discord.Embed(title="Correct!",color=0xFF0000)
      await ctx.send(embed=embed)
      embed = discord.Embed(title="ENDGAME",description=f"""
      Welcome {ctx.author}
      
      What would you like to do?
      _____________________________
      Learn about Earth#9389 | Earth

      Endgame protocal | Endgame

      if you want to cancel say Cancel
      """,color=0xFF0000)
      await ctx.send(embed=embed)
      two = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
      if two:
        if two.content == "Earth":
          embed = discord.Embed(title="Earth",description=f"""
          Earth is a 14 year old male human being. Most commonally known as Earth or Earth9389. He joined the sock drawer on december 20 2020 and as of today continues to talk in the server. Earth likes to engage in multiple conversations and join voice channels. Sadly on 02/02/2021 Earht joined a voice channel on Nadwe's server at aproxometly 8 pm CET. Little did he know this was the last time he will ever join a vc in that server. Due to an issue he got banned. Shortly after at 9:35 CET he got banned from Jooice's discord server too from Nadwe himself. He felt regret in what has happened and how it could of changed. The days following were normal but Earth talked to discord user Chipdip on what has happend and possibly a way for Earth to explain to Nadwe what happened. Earth tried dms ut htye were blocked so he tried to send a friend request as a test shot but it failed too. On 02/19/2021 he got muted in the sock drawer due to the nadwe issue. He explained to the mods what happened and got unmuted however Earth did not talk in the server because he thought he got unmuted as a mistake. The next day he got banned from TBh's server for the same reason as the last two ands the day after he gets banned from Woolf's server.
          """,color=0xFF0000)
          await ctx.send(embed=embed)
          embed = discord.Embed(description=f"""
          This really got him worried as there was nothing he could do and he could not stop thinking about the issue. Days following he became incredably sad and somewhat depressed. After a couple more days it all seemed to lighten up but when he joined TBVG's server he ogt banned within the first 1 hour. This is when he knew that the issue did not end. then on 03/03/2021 he had recieved a domotion on the Socks.gg minecraft server and this really pushed him to a deeper state of depression. He kept thinking that people hated him after the demotion and refused to talk to staff for quite some time. As of now nothing came of this and he is still demoted on the mc server. Earth does not like to talk about the issue as to why tho. Moving on... Earth first lived in Colorado then moved to Germany where he really got into discord. He created his server as a testing server for his bot until discord user Nav asked if he can make the server in to a dev hub type server. And after a couple days that is exactly what Earth did. Earth will be leaving discord on 08/1/2021 due to life issues. He seeks to get the life he had before he joined discord and moved to germany. It is unsure how long this pause will last but there is nothing to prevent it.
          """,color=0xFF0000)
          await ctx.send(embed=embed)
        if two.content == "earth":
          embed = discord.Embed(title="Earth",description=f"""
          Earth is a 14 year old male human being. Most commonally known as Earth or Earth9389. He joined the sock drawer on december 20 2020 and as of today continues to talk in the server. Earth likes to engage in multiple conversations and join voice channels. Sadly on 02/02/2021 Earht joined a voice channel on Nadwe's server at aproxometly 8 pm CET. Little did he know this was the last time he will ever join a vc in that server. Due to an issue he got banned. Shortly after at 9:35 CET he got banned from Jooice's discord server too from Nadwe himself. He felt regret in what has happened and how it could of changed. The days following were normal but Earth talked to discord user Chipdip on what has happend and possibly a way for Earth to explain to Nadwe what happened. Earth tried dms ut htye were blocked so he tried to send a friend request as a test shot but it failed too. On 02/19/2021 he got muted in the sock drawer due to the nadwe issue. He explained to the mods what happened and got unmuted however Earth did not talk in the server because he thought he got unmuted as a mistake. The next day he got banned from TBh's server for the same reason as the last two ands the day after he gets banned from Woolf's server.
          """,color=0xFF0000)
          await ctx.send(embed=embed)
          embed = discord.Embed(description=f"""
          This really got him worried as there was nothing he could do and he could not stop thinking about the issue. Days following he became incredably sad and somewhat depressed. After a couple more days it all seemed to lighten up but when he joined TBVG's server he ogt banned within the first 1 hour. This is when he knew that the issue did not end. then on 03/03/2021 he had recieved a domotion on the Socks.gg minecraft server and this really pushed him to a deeper state of depression. He kept thinking that people hated him after the demotion and refused to talk to staff for quite some time. As of now nothing came of this and he is still demoted on the mc server. Earth does not like to talk about the issue as to why tho. Moving on... Earth first lived in Colorado then moved to Germany where he really got into discord. He created his server as a testing server for his bot until discord user Nav asked if he can make the server in to a dev hub type server. And after a couple days that is exactly what Earth did. Earth will be leaving discord on 08/1/2021 due to life issues. He seeks to get the life he had before he joined discord and moved to germany. It is unsure how long this pause will last but there is nothing to prevent it.
          """,color=0xFF0000)
          await ctx.send(embed=embed)
        if two.content == "Endgame":
          await ctx.send("added later")
        if two.content == "endgame":
          await ctx.send("added later")
        if two.content == "Cancel":
          return
        if two.content == "cancel":
          return

    


    if Pas.content == "Cancel":
      return
    if Pas.content == "cancel":
      return
    else:
      embed = discord.Embed(title="That was incorrect!",color=0xFF0000)
      await ctx.send(embed=embed)
    
  












# @bot.command()
# async def Fight(ctx, user: discord.Member = None):
#   if user == None:
#     await ctx.reply("Please include a valid member")
#     return
#   else:
#     P1 = 100
#     P2 = 100
#     await ctx.send(f"{ctx.author.mention} What would you like to do, Punch, Kick, Slap, or End?")
#     Game = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
#     if Game:
#       if Game.content == "Punch":
#         pu = random.randint(5,25)
#         P2 = P2 - pu
#         await ctx.channel.send(f"{ctx.author.mention} lands a striking punch on {user.mention} dealing {pu} damage! {user} is left on {P2} health")
#         await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
#         G2 = await bot.wait_for('message', check=lambda message: user == user)
#         if G2:
#           if G2.content == "Punch":
#             pu2 = random.randint(5,25)
#             P2 = P2 - pu2
#             await ctx.channel.send(f"{user.mention} lands a hurtful punch on {ctx.author.mention} dealing {pu2} damage! {ctx.author} is left on {P2} health")
#             #contiue here


#           if G2.content == "Kick":
#             ku2 = random.randit(1,2)
#             if ku2 == 1:
#               kuu2 = random.randint(20,40)
#               P1 = P1 - kuu2
#               await ctx.channel.send(f"{user.mention} Kicks {ctx.author.mention}'s knees off dealing {kuu2} damage! {ctx.author} is left on {P1} health")
#               await ctx.send(f"{ctx.author.mention} What would you like to do, Punch, Kick, Slap, or End?")
#               G3 = await bot.wait_for('message', check=lambda message: user == ctx.user)
#               if G3:
#                 return
#             #same here
#           if ku2 == 2:
#             kk = random.randint(5,20)
#             P1 = P1 - kk
#             await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kk} damage to them self! {ctx.author} is left on {P1} health")
#             await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
#             G2 = await bot.wait_for('message', check=lambda message: user == ctx.user)
#             if G2:
#               return
#             #same here

#       if Game.content == "Kick":
#        ku = random.randint(1,2)
#        if ku == 1:
#           kuu = random.randint(20,40)
#           P2 = P2 - kuu
#           await ctx.channel.send(f"{ctx.author.mention} Kicks {user.mention}'s knees off dealing {kuu} damage! {user} is left on {P2} health")
#           await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
#           G2 = await bot.wait_for('message', check=lambda message: user == ctx.user)
#           if G2:
#             return
#             #same here
#        if ku == 2:
#           kk = random.randint(5,20)
#           P1 = P1 - kk
#           await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kk} damage to them self! {ctx.author} is left on {P1} health")
#           await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
#           G2 = await bot.wait_for('message', check=lambda message: user == ctx.user)
#           if G2:
#             return
#             #same here
#       if Game.content == "Slap":
#         Su = random.randint(15,30)
#         P2 = P2 - Su
#         await ctx.channel.send(f"{ctx.author.mention} slapped {user.mention} into to the next century, dealing {Su} damage! {user} is left on {P2} health")
#         await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
#         G2 = await bot.wait_for('message', check=lambda message: user == ctx.user)
#         if G2:
#           return
#           #same here
#       if Game.content == "End":
#         return






      
@bot.command(name = "Fight", aliases = ["fight",])
async def Fight(ctx, user: discord.Member = None):
  if user == None:
    await ctx.reply("Please include a valid member")
    return
  else:
    P1 = 100
    P2 = 100
    while P1 or P2 > 0:
      await ctx.send(f"{ctx.author.mention} What would you like to do, Punch, Kick, Slap, or End?")
      Game = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
      if Game:
        if Game.content == "Punch":
          pu = random.randint(5,25)
          P2 = P2 - pu
          await ctx.channel.send(f"{ctx.author.mention} lands a striking punch on {user.mention} dealing {pu} damage! {user} is on {P2} health")
          await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
          G2 = await bot.wait_for('message', check=lambda message: user)
          if G2:
            if G2.content == "Punch":
              pu22 = random.randint(5,25)
              P2 = P2 - pu22
              await ctx.channel.send(f"{user.mention} lands a hurtful punch on {ctx.author.mention} dealing {pu22} damage! {ctx.author} is left on {P2} health")
          
            if G2.content == "Kick":
                ku2 = random.randint(1,2)
                if ku2 == 1:
                  kuu2 = random.randint(20,40)
                  P1 = P1 - kuu2
                  await ctx.channel.send(f"{user.mention} Kicks {ctx.author.mention}'s knees off dealing {kuu2} damage! {ctx.author} is left on {P1} health")
                if ku2 == 2:
                  kk = random.randint(5,20)
                  P1 = P1 - kk
                  await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kk} damage to them self! {ctx.author} is left on {P1} health")
              
            if G2.content == "Slap":
              Su = random.randint(15,30)
              P2 = P2 - Su
              await ctx.channel.send(f"{ctx.author.mention} slapped {user.mention} into to the next century, dealing {Su} damage! {user} is left on {P2} health")
              
            if G2.content == "End":
                return
        
        
        if Game.content == "Kick":
          ku = random.randint(1,2)
          if ku == 1:
            kuu = random.randint(20,40)
            P2 = P2 - kuu
            await ctx.channel.send(f"{ctx.author.mention} Kicks {user.mention}'s knees off dealing {kuu} damage! {user} is left on {P2} health")
            await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
            G3 = await bot.wait_for('message', check=lambda message: user)
            if G3:
              if G3.content == "Punch":
                pu3 = random.randint(5,25)
                P2 = P2 - pu3
                await ctx.channel.send(f"{user.mention} lands a hurtful punch on {ctx.author.mention} dealing {pu3} damage! {ctx.author} is left on {P2} health")
          
              if G3.content == "Kick":
                ku3 = random.randint(1,2)
                if ku3 == 1:
                  kuu3 = random.randint(20,40)
                  P1 = P1 - kuu3
                  await ctx.channel.send(f"{user.mention} Kicks {ctx.author.mention}'s knees off dealing {kuu3} damage! {ctx.author} is left on {P1} health")
                if ku3 == 2:
                  kC = random.randint(5,20)
                  P1 = P1 - kC
                  await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kC} damage to them self! {ctx.author} is left on {P1} health")
              
              if G3.content == "Slap":
                SU = random.randint(15,30)
                P2 = P2 - SU
                await ctx.channel.send(f"{ctx.author.mention} slapped {user.mention} into to the next century, dealing {SU} damage! {user} is left on {P2} health")
              
              if G3.content == "End":
                return
          
          
          
          
          
          if ku == 2:
            kk = random.randint(5,20)
            P1 = P1 - kk
            await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kk} damage to them self! {ctx.author} is left on {P1} health")
            await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
            G4 = await bot.wait_for('message', check=lambda message: user)
            if G4:
              if G4.content == "Punch":
                pu4 = random.randint(5,25)
                P2 = P2 - pu4
                await ctx.channel.send(f"{user.mention} lands a hurtful punch on {ctx.author.mention} dealing {pu4} damage! {ctx.author} is left on {P2} health")
          
              if G4.content == "Kick":
                ku4 = random.randint(1,2)
                if ku4 == 1:
                  kuu4 = random.randint(20,40)
                  P1 = P1 - kuu4
                  await ctx.channel.send(f"{user.mention} Kicks {ctx.author.mention}'s knees off dealing {kuu4} damage! {ctx.author} is left on {P1} health")
                if ku4 == 2:
                  kk4 = random.randint(5,20)
                  P1 = P1 - kk4
                  await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kk4} damage to them self! {ctx.author} is left on {P1} health")
              
              if G4.content == "Slap":
                Su4 = random.randint(15,30)
                P2 = P2 - Su4
                await ctx.channel.send(f"{ctx.author.mention} slapped {user.mention} into to the next century, dealing {Su4} damage! {user} is left on {P2} health")
              
              if G4.content == "End":
                return

        if Game.content == "Slap":
          SUU = random.randint(15,30)
          P2 = P2 - SUU
          await ctx.channel.send(f"{ctx.author.mention} slapped {user.mention} into to the next century, dealing {SUU} damage! {user} is left on {P2} health")
          await ctx.send(f"{user.mention} What would you like to do, Punch, Kick, Slap, or End?")
          G5 = await bot.wait_for('message', check=lambda message: user)
          if G5:
            if G5.content == "Punch":
              pu5 = random.randint(5,25)
              P2 = P2 - pu5
              await ctx.channel.send(f"{user.mention} lands a hurtful punch on {ctx.author.mention} dealing {pu5} damage! {ctx.author} is left on {P2} health")
          
            if G5.content == "Kick":
              ku5 = random.randint(1,2)
              if ku5 == 1:
                kuu5 = random.randint(20,40)
                P1 = P1 - kuu5
                await ctx.channel.send(f"{user.mention} Kicks {ctx.author.mention}'s knees off dealing {kuu5} damage! {ctx.author} is left on {P1} health")
              if ku5 == 2:
                kk5 = random.randint(5,20)
                P1 = P1 - kk5
                await ctx.channel.send(f"{ctx.author.mention} tried kicking {user.mention} but they FELL DOWN, dealing {kk5} damage to them self! {ctx.author} is left on {P1} health")
              
            if G5.content == "Slap":
              Su5 = random.randint(15,30)
              P2 = P2 - Su5
              await ctx.channel.send(f"{ctx.author.mention} slapped {user.mention} into to the next century, dealing {Su5} damage! {user} is left on {P2} health")
              
            if G5.content == "End":
              return

        if Game.content == "End":
          return
        
      if P1 <= 0:
        await ctx.channel.send(f"Congrats {user.mention}! You defeated {ctx.author.mention}! You Won")
        return
      
      if P2 <= 0:
        await ctx.channel.send(f"Congrats {ctx.author.mention}! You defeated {user.mention}! You Won")
        return


          

@bot.command()
async def React(ctx, Id:int):
  message = ctx.fetch_message(Id)
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)

@bot.command()
async def P(ctx):
  embed=discord.Embed(title="Ping Reaction Roles", description="React with the emojis to get the roles", color=0x0000FF)
  embed.add_field(name="🌲", value="Earth News ", inline=True)
  embed.add_field(name="📢", value="Server Updates ", inline=True)
  embed.add_field(name="🗳", value="Polls ", inline=True)
  embed.add_field(name="🏕", value="Smp Updates ", inline=True)
  embed.add_field(name="🧱", value="Mc Testing ", inline=True)
  msg = await ctx.send(embed=embed)
  await msg.add_reaction('🌲')
  await msg.add_reaction('📢')
  await msg.add_reaction('🗳')
  await msg.add_reaction('🏕')
  await msg.add_reaction('🧱')
  def check(reaction, user):
    return user == user and reaction.message == msg and str(reaction.emoji) in ['🌲','📢','🗳','🏕','🧱']
  while True:
    reaction, user = await bot.wait_for("reaction_add", check=check)
    if str(reaction.emoji) == '🌲':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Earthlings"))
    if str(reaction.emoji) == '📢':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Updates"))
    if str(reaction.emoji) == '🗳':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Polls"))
    if str(reaction.emoji) == '🏕':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Smp updates"))
    if str(reaction.emoji) == '🧱':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Mc Tester"))
    
                    
    

 

@bot.command()
async def G(ctx):
  embed=discord.Embed(title="Gender Reaction Roles", description="React with the emojis to get the roles", color=0x0000FF)
  embed.add_field(name="🔵", value="He/Him ", inline=True)
  embed.add_field(name="🟣", value="She/Her ", inline=True)
  embed.add_field(name="🟡", value="They/Them ", inline=True)
  embed.add_field(name="🟢", value="Any ", inline=True)
  embed.add_field(name="🔴", value="Other ", inline=True)
  msg = await ctx.send(embed=embed)
  await msg.add_reaction('🔵')
  await msg.add_reaction('🟣')
  await msg.add_reaction('🟡')
  await msg.add_reaction('🟢')
  await msg.add_reaction('🔴')
  def check(reaction, user):
    return user == user and reaction.message == msg and str(reaction.emoji) in ['🔵','🟣','🟡','🟢','🔴']
  while True:
    reaction, user = await bot.wait_for("reaction_add", check=check)
    if str(reaction.emoji) == '🔵':
      await user.add_roles(discord.utils.get(user.guild.roles, name="He/Him"))
    if str(reaction.emoji) == '🟣':
      await user.add_roles(discord.utils.get(user.guild.roles, name="She/Her"))
    if str(reaction.emoji) == '🟡':
      await user.add_roles(discord.utils.get(user.guild.roles, name="They/Them"))
    if str(reaction.emoji) == '🟢':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Any of them"))
    if str(reaction.emoji) == '🔴':
      await user.add_roles(discord.utils.get(user.guild.roles, name="Other"))
    







bot.run(DISCORD_TOKEN)





