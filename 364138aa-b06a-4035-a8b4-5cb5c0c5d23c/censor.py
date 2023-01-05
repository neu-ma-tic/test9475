from replit import db
from discord.ext import commands


class Censor(commands.Cog):

  mean_words = ["shut up","dumbass"]

  def __init__(self, bot):
    if "responding" not in db.keys():
      db["responding"] = True
    if "mean_words" not in db.keys():
      db["mean_words"] = self.mean_words
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self,message):
    meanWords = db['mean_words']
    msg = message.content.lower().split(' ')
    if db['responding'] and any(word in msg for word in meanWords):
      await message.channel.send("Language!")
  
  @commands.command(name='censor', help='Toggle censoring feature')
  async def toggle_censor(self,ctx):
    if db["responding"]:
      db["responding"] = False
      await ctx.send("Censoring is turned off. Enjoy the freedom while it lasts...")
    else:
      db["responding"] = True
      await ctx.send("Censoring is on. Watch your language!")

  @commands.command(name='censor-add', help='Add a new word to sensor')
  async def add_censor(self,ctx,word):
    word = word.lower()
    if word in db['mean_words']:
      await ctx.send("I'm already censoring that word")
    else:
      words = db['mean_words']
      words.append(word)
      db['mean_words'] = words
      await ctx.send("Ok I\'ll start censoring that word now")
