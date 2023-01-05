import discord
import requests
import json
from discord.ext import commands

class Inspire(commands.Cog):
    def __init__(self, client):
        # super().__init__()
        self.client = client

    def get_quote(self):
        qdata=requests.get("https://zenquotes.io/api/random")
        # print(qdata.text)
        jsondata=json.loads(qdata.text)
        return(jsondata[0]['q']+" -"+jsondata[0]['a'])

    @commands.Cog.listener()
    async def on_ready(self):
        print('Inspire cog ready')

    @commands.command(aliases=['inspire'])
    async def _inspire(self, ctx):
        await ctx.send(self.get_quote())
    
def setup(client):
    client.add_cog(Inspire(client))
