import discord
from discord import channel # 將dc的模組導入
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 隨機(self,ctx):
        random_pic = random.choice(jdata['pic']) # 電腦上的檔案要上傳至DC，需透過39行將路徑轉為圖檔，否則只會上傳路徑
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
    
    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic']) # 網路上的圖檔只需上傳路徑，dc會將其轉為圖檔而不是路徑
        await ctx.send(random_pic)
        
def setup(bot):
    bot.add_cog(React(bot))