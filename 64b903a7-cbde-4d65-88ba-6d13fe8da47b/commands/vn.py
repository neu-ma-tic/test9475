import discord

from discord.ext import commands
from random import choice

class VN(commands.Cog, description='Vietnamese stuffs'):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    
    @commands.command(description='Lấy 1 văn mẫu ngấu nhiên', help='vanmau')
    async def vanmau(self, ctx: commands.Context):
      with open('data_file/vanmau.txt', 'r') as file:
        return await ctx.send(choice(file.read().split('|<>|')))
    
    @commands.command(description='Thêm 1 văn mẫu (chỉ áp dụng cho admin)', help='vanmauadd [van mau]')
    @commands.has_guild_permissions(administrator=True)
    async def vanmauadd(self, ctx: commands.Context, *, vanmau: str):
      with open('data_file/vanmau.txt', 'a+') as file:
        if vanmau in file.read().split('|<>|'):
          return await ctx.send('Văn mẫu đã tồn tại')
        if len(vanmau) > 1998:
          return await ctx.send('Văn mẫu dài hơn 2000 kí tự. Xin hãy thử lại')
        string = '|<>|' + vanmau
        file.write(string)
        return await ctx.send('Văn mẫu đã được thêm')
    
    @vanmauadd.error
    async def vanmauadd_error(self, ctx: commands.Context, error: commands.CommandError):
      if isinstance(error, commands.MissingPermissions):
        return await ctx.send("You don't have administration permission")