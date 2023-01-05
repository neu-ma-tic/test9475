import discord, os 
from discord.ext import commands
   
bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())  

class Test(commands.Cog):
     def __init__(self, bot):
         self.bot = bot

     @commands.command()
     async def ping(self, ctx):
         await ctx.send("Pong")

bot.add_cog(Test(bot))  

token = os.environ['TOKEN']
bot.run(token)