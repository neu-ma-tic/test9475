import discord
from discord.ext import commands
import random
from replit import db
import members

class Chatting(commands.Cog):

  greetings = [
    "Hello friend!",
    "Hey buddy!",
    "How are you champ?",
    "Nice to see you fellow citizen!"
  ]
  chatting = [
    "I remember the days when redstone was used as currency. Can you imagine how much money we would have if that was still legal?",
    "Hey have you ever tried glow? You know, like glowdust? Uh I mean I totally haven't.",
    "Carrots are yummy, but the blood of my cattle is yummier",
    "I wonder if zombies would leave me alone if I removed my brain...",
    "Have you met this guy named Brian? I heard he was run out of his own town by an angry mob.",
    "I don't like the dark.",
    "When I was a Miner I was too scared to fall in lava. So I never went undergroud! Yep, I found any exposed ore on the surface and mined that instead. I still don't know why I was fired.",
    "Have you seen my dog anywhere?"
  ]
  whisperChat = [
    "Don't you think this town could benefit from a little Communist take over??",
    "Hey you wanna buy some glow?",
    "I hear security around here is pretty lax. You want to rob a bank or something?",
    "Finally... we're alone.",
    "Hey just between friends...does this look a little small to you? Oh its regular sized? Thank god!",
    "Everythin Brian says is fake news. Spread the word."
  ]

  def __init__(self,bot):
    self.bot = bot
    db["alive"] = True


  @commands.command(name='hello', help='Say hello to Gerald')
  async def greet(self,ctx):
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the town"))
    response = random.choice(self.greetings)
    await ctx.send(response)
  
  @commands.command(name='chat', help='Chat with Gerald')
  async def chat(self,ctx):
    response = random.choice(self.chatting)
    await ctx.send(response)

  @commands.command(name='whisper', help='Ask Gerald to whisper something to you in private')
  async def whisper(self,ctx):
    user = ctx.author
    response = random.choice(self.whisperChat)
    await user.send(response)

  @commands.command(name='add-mem', help='Add member to database (DEV)')
  @commands.has_role("BotDev")
  async def getInfo(self,ctx):
    user = ctx.author
    members.addFriend(user.name,user.display_name)
    await ctx.send(user.name)

  @commands.command(name='add-points', help='Add friendship points (DEV)')
  @commands.has_role("BotDev")
  async def addPoints(self,ctx):
    user = ctx.author
    members.addPoints(user.name,5)
    await ctx.send("Added")

  @commands.command(name='see-points', help='See friendship points (DEV)')
  @commands.has_role("BotDev")
  async def seePoints(self,ctx):
    user = ctx.author
    points = members.points(user.name)
    await ctx.send(points)

  @commands.command(name='kill', help='Kill Gerald (DEV)')
  @commands.has_role("BotDev")
  async def kill(self,ctx):
    if db["alive"]:
      fp = open('Zombie.jpg', 'rb')
      image = fp.read()
      db["alive"] = False
      await self.bot.user.edit(avatar=image)
    await ctx.send("I'm already dead jerk!")
  
  @commands.command(name='revive', help='Revive Gerald (DEV)')
  @commands.has_role("BotDev")
  async def revive(self,ctx):
    if not db["alive"]:
      fp = open('Gerald.png', 'rb')
      image = fp.read()
      db["alive"] = True
      await self.bot.user.edit(avatar=image)
    else:
      await ctx.send("I'm still alive...but thanks")