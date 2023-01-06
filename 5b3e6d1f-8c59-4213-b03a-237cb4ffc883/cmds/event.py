import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
class Event(Cog_Extension):
    @commands.Cog.listener()# 成員加入
    async def on_member_join(self,member):
        print(f'{member} join!')
        channel = self.bot.get_channel((int(jdata['Welcome_channel'])))
        await channel.send(f'{member} 歡迎加入!')
    
    @commands.Cog.listener()# 成員離開
    async def on_member_remove(self,member):
        print(f'{member} leave!')
        channel = self.bot.get_channel((int(jdata['Leave_channel'])))
        await channel.send(f'{member} 離開了...')
    
    @commands.Cog.listener()
    async def on_message(self,msg): # 關鍵字觸發
        if msg.content in jdata['keyword'] and msg.author !=self.bot.user:
            await msg.channel.send('HI')
        if msg.content == '風寶':
            await msg.channel.send('不存在')
        if msg.content.endswith('努力'):
            await msg.channel.send('廢物:thumbsdown: ')
                
def setup(bot):
    bot.add_cog(Event(bot))