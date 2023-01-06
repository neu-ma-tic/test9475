import discord
import random 
from discord.ext import commands 
from core.classes import Cog_Extension
import random,json 

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class React(Cog_Extension):
    
    @commands.command()
    async def IDK(self,ctx):
        random_pic=random.choice(jdata['pic_WTM'])
        await ctx.send(random_pic)

    @commands.command()
    async def omikuji(self,ctx,*,msg):
      lucky_number=random.randint(1,99)
      luc_state=0  
      luc=""
      print(lucky_number)
      print(ctx.author)      
      if lucky_number>=87:
          luc="大吉"
          luc_state=0
      elif lucky_number<87 and lucky_number>=73:
          luc="中吉"
          luc_state=1
      elif lucky_number<73 and lucky_number>=59:
          luc="小吉"
          luc_state=2
      elif lucky_number<59 and lucky_number>=45:
          luc="吉"
          luc_state=3
      elif lucky_number<45 and lucky_number>=31:
          luc="末吉"
          luc_state=4
      elif lucky_number<31 and lucky_number>=1:
          luc="凶"
          luc_state=5
      embed=discord.Embed(title="今日運勢 "+luc, color=0x27ecd5)
      embed.add_field(name=ctx.author, value=msg+"的運勢是", inline=False)
      embed.set_image(url=jdata['omi'][luc_state])
      await ctx.send(embed=embed)
     


def setup(bot):
    bot.add_cog(React(bot))

