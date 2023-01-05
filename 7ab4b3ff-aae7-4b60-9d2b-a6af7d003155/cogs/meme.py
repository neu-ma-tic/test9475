import discord
import requests
import json
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self, client):
        # super().__init__()
        self.client = client

    def get_meme(self,c):
      qdata=requests.get("https://meme-api.herokuapp.com/gimme/"+str(c))
      # print(qdata.text)
      l=[]
      jsondata=json.loads(qdata.text)
      
      for meme in jsondata["memes"]:
        l.append(meme["url"])

      return "\n".join(l)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Inspire cog ready')

    @commands.command(aliases=['meme'])
    async def _meme(self, ctx, count=1):
        await ctx.send(self.get_meme(count))
    
def setup(client):
    client.add_cog(Meme(client))