import discord
from discord.ext import commands 
import json,random
from  core.classes import Cog_Extension
from discord.ext.commands.cog import _cog_special_method 
from collections import OrderedDict


with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(861484284925837355)
        await channel.send(f'{member} 自虛空中誕生!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel =self.bot.get_channel(861484284925837355)
        await channel.send(f'{member} 溜走了!')

    @commands.Cog.listener()
    async def on_message(self,msg):
      if 'Siesta' in msg.content and msg.author!=self.bot.user:
        await msg.channel.send('你是笨蛋嗎?')
      for item in jdata['keyword']:
        if item in msg.content and msg.author != self.bot.user:
            await msg.channel.send('不開啦幹')

   
    @commands.Cog.listener()
    async def on_member_gaming(self,member):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
      #判斷新增反映貼圖
      if data.message_id == 891656921646514226:
        if str(data.emoji) == '👌':
          guild=self.bot.get_guild(data.guild_id) #獲取頻道
          role=guild.get_role(891617945241911317) #獲取指定身分組
          await data.member.add_roles(role) #給予指定身分組 
          await data.member.send(f"您取得了 {role} 身分組")
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
      #判斷新增反映貼圖
      if data.message_id == 891656921646514226:
        if str(data.emoji) == '👌':
          guild = self.bot.get_guild(data.guild_id)
          user = await guild.fetch_member(data.user_id)
          role=guild.get_role(891617945241911317) #獲取指定身分組
          await user.remove_roles(role) #給予指定身分組 
          await user.send(f"您移除了 {role} 身分組")
  
      
      

def setup(bot):
  bot.add_cog(Event(bot))
 