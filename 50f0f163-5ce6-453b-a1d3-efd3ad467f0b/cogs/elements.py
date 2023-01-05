import discord
from discord.ext import commands
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://botprogram:shop3able@cluster0.bxok8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['discord']
collection = db["elements"]

class elements(commands.Cog):
  def __init__(self, client):
      self.client=client

  @commands.command()
  async def start(self,ctx):


    embed = discord.Embed(title="Welcome to the game of **Elements** ",description="First, you will choose an element as your power source\n**CHOOSE WISELY**", color=discord.Color.random())
    embed.add_field(name='🔥Fire',value="You'll be able to control any form of FIRE🔥🔥🔥")
    embed.add_field(name=':thunder_cloud_rain: Thunder',value="You'll have the power to control weather")
    embed.add_field(name='<:internet:921929358115999805>Internet',value="You'll have the power to manuplate the internet")
    embed.add_field(name='<:water:921924304587853874>Water',value="You'll have the power to control **any** form of water")
    embed.add_field(name='<a:soil:921930557355589664>Soil',value="You'll have the power to control **any** form of soil")
    embed.set_footer(text="definitely not copied from avatar", icon_url="https://cdn.discordapp.com/avatars/763315062668001301/a0117e092350cef21f457ec864a1d0d0.png?size=1024")
    await ctx.send(embed=embed)

    if collection.find({"name":str(ctx.author.id)}).count() > 0:
      await ctx.send("You already chose your element, if you want to change your element\nUse `.chel` to change your element")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await self.client.wait_for('message', check=check)
    if msg.content.lower() == 'water':
      await ctx.send("You have chosen water<:water:921924304587853874>! Great Choice!")
      collection.insert_one({"_id":collection.find().count(),"name":str(ctx.author.id),"element1":msg.content.lower(), "level":1})
    elif msg.content.lower() == 'fire':
      await ctx.send("You have chosen fire🔥! Great Choice!")
      collection.insert_one({"_id":collection.find().count(),"name":str(ctx.author.id),"element1":msg.content.lower(), "level":1})
    elif msg.content.lower() == 'thunder':
      await ctx.send("You have chosen thunder⛈️! Great Choice!")
      collection.insert_one({"_id":collection.find().count(),"name":str(ctx.author.id),"element1":msg.content.lower(), "level":1})
    elif msg.content.lower() == 'internet':
      await ctx.send("You have chosen internet<:internet:921929358115999805>! Great Choice!")
      collection.insert_one({"_id":collection.find().count(),"name":str(ctx.author.id),"element1":msg.content.lower(), "level":1})
    elif msg.content.lower() == 'soil':
      await ctx.send("You have chosen soil<a:soil:921930557355589664>! Great Choice!")
      collection.insert_one({"_id":collection.find().count(),"name":str(ctx.author.id),"element1":msg.content.lower(), "level":1})
    else:
      await ctx.send("Please choose a proper element bruh<:bruh:899799039401414676>\nUse the command again and type in a proper element please")




def setup(client):
  client.add_cog(elements(client))