import discord
from discord.ext import commands
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://emample:<king1234>@cluster0.loul6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levelling = cluster["discord"]["levelling"]

class levelsys(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("ready")
  
  @commands.Cog.listener()
  async def on_message(self, ctx):
    stats = levelling.find_one({"id" : ctx.author.id})
    if not ctx.author.bot:
      if stats is None:
        newuser = {"id" : ctx.author.id, "xp": 100}
        levelling.insert_one(newuser)
      else:
        xp = stats["xp"] + 5
        levelling.update_one({"id":ctx.author.id}, {"$set":{"xp":xp}})
        lvl = 0
        while True:
          if xp < ((50*(lvl**2))+(50*lvl)):
            break
          lvl += 1
        xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
        if xp == 0:
          embed = discord.Emded(description=f"well done {ctx.author.mention}! You leveled up to **level: {lvl}**")
          embed.set_thumbnail(url=ctx.author.avatar_url)

          await ctx.channel.send(embed=embed)

  @commands.command()
  async def rank(self, ctx):
    stats = levelling.find_one({"id" : ctx.author.id})
    if stats is None:
      embed = discord.Embed(description="You haven't sent any message, no rank! :sob:")
      await ctx.channel.send(embed=embed)
    else:
      xp = stats["xp"]
      lvl = 0
      rank = 0
      while True:
          if xp < ((50*(lvl**2))+(50*lvl)):
            break
          lvl += 1
      xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
      boxes = int((xp/(200*((1/2) * lvl)))*20)
      rankings = levelling.find().sort("xp",-1)
      for x in rankings:
        rank += 1
        if stats["id"] == x["id"]:
          break
      em = discord.Embed(title="{}'s level stats".format(ctx.author.name))
      em.add_field(name="Name", value=ctx.author.mention, inline=True)
      em.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
      em.add_field(name="Rank", value=f"{rank}/{ctx.guild.menber_count}", inline=True)
      em.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_spuare:" + (20-boxes) * ":white_large_spuare:", inline=True)
      embed.set_thumbnail(url=ctx.author.avatar_url)
      await ctx.channel.send(em=embed)

def setup(client):
  client.add_cog(levelsys(client))