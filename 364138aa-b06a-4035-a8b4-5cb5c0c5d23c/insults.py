from discord.ext import commands
import random
from replit import db

class Insults(commands.Cog):
  starting_insults = [
  "You have a small brain sir"
  ]
  def __init__(self, bot):
    self.bot = bot

  def get_insult(self):
    options = self.starting_insults
    if "insults" in db.keys():
      options = db["insults"]
    response = random.choice(options)
    return response

  def _update_insults(self,message):
    if "insults" in db.keys():
      insults = db["insults"]
      insults.append(message)
      db["insults"] = insults
    else:
      db["insults"] = [message]

  def _delete_insult(self,index):
    insults = db["insults"]
    if len(insults)>index:
      del insults[index]
      db["insults"] = insults
      return 1
    return 0


  @commands.command(name='insult', help='Gerald will say a random insult')
  async def sayInsult(self,ctx):
    await ctx.send(self.get_insult())
  
  @commands.command(name='insult-new', help="Adds a new insult to Gerald's list")
  async def new_insult(self,ctx,*,arg):
    self._update_insults(arg)
    await ctx.send("New insult added. Thanks!")

  @commands.command(name='insult-delete', help="Deletes insult number given")
  async def del_insult(self, ctx, index:int):
    if "insults" in db.keys():
      if self._delete_insult(index):
        await ctx.send("Insult deleted")
        return
      else:
        await ctx.send("Sorry there isn't an insult at that index")
        return
    await ctx.send("No insults exist in database :(") 

  @commands.command(name='insult-list', help="Shows a list of all Gerald's known insults")
  async def all_insults(self, ctx):
    insults = []
    if "insults" in db.keys():
      insults = db["insults"]
    await ctx.send("```\nInsult List:\n" + "\n".join(insults) + "\n```")
