import discord
from discord.ext import commands
from discord.utils import get
from replit import db
import random

def addFriend(name,display_name):
  if "friends" in db.keys():
    friends = db["friends"]
    friends.append([name,display_name,70])
    db["friends"] = friends
  else:
    db["friends"] = [[name,display_name,70]]

def inData(name):
  if "friends" in db.keys():
    friends = db["friends"]
    for f in friends:
      if name == f[0]:
        disp = f[1]
        points = f[2]
        del friends[friends.index(f)]
        return friends,disp,points
    return friends,'',-1
  return[],'',-1
  
def addPoints(name,amount):
  friends,display_name,points = inData(name)
  friendship = int(points)
  if friends:
    if friendship != -1:
      if friendship + amount > 100:
        friendship = 100
      else:
        friendship += amount
      friends.append([name,display_name,friendship])
      db["friends"] = friends
    print("error 1")
  print("error 2")
      

#   def removePoints(self,amount):
#     if self.friendship - amount < 0:
#       self.friendship = 0
#     else:
#       self.friendship -= amount

def points(name):
  if "friends" in db.keys():
    friends = db["friends"]
    for f in friends:
      if name == f[0]:
        return f[2]
    return -1
  return -2

#   def status(self):
#     if self.friendship > 66:
#       return 2
#     elif self.friendship < 33:
#       return 0
#     else:
#       return 1

#   def willIgnore(self):
#     s = self.status()
#     if s == 2:
#       return 0
#     elif s == 0:
#       return random.choices([0,1],[50,50])
#     else:
#       return random.choices([0,1],[70,30])



class UserInfo(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command(name='profile', help='Show the profile of a specific member (DEV)')
  @commands.has_role("BotDev")
  async def getInfo(self,ctx,*,arg):
    name = arg.split(' ')[0]
    print(name)
    if name:
      user = get(ctx.message.guild.members, name = name)
      if user == None:
        user = get(ctx.message.guild.members, display_name = name)
        if user == None:
          await ctx.send("That user isn't in our town")
          return
      await ctx.send(self._getProfile(user))
    return

  @commands.command(name='myprofile', help='Show your profile (DEV)')
  @commands.has_role("BotDev")
  async def myInfo(self,ctx):
    user = ctx.author
    await ctx.send(self._getProfile(user))