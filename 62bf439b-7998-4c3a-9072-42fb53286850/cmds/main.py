import discord, random, asyncio
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'延遲為：{round(self.bot.latency*1000)}(ms)')
        
    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit = num + 1)

    @commands.command()
    async def ban(self, ctx, name:discord.Member=None):
        role = discord.utils.get(ctx.guild.roles, name="mute")
        role2 = discord.utils.get(ctx.guild.roles, name="1")
        role3 = discord.utils.get(ctx.guild.roles, name="888")
        role3_count = 0
        if (ctx.author.name == 'Juice'):
          member = name
          await member.add_roles(role)
          await member.remove_roles(role2)
          if (role3 in member.roles):
              await member.remove_roles(role3)
              role3_count += 1
          mute_time = random.randint(1, 600)
          await ctx.send(f'你可以體驗呼吸的可貴'+ str(mute_time) + f'秒')
          await asyncio.sleep(mute_time)
          await member.remove_roles(role)
          await member.add_roles(role2)
          if (role3_count != 0):
            await member.add_roles(role3)
            role3_count == 0
        else:
          await ctx.send(f'沒權限ban你麻痺')
          member = ctx.author
          await member.add_roles(role)
          await member.remove_roles(role2)
          if (role3 in member.roles):
              await member.remove_roles(role3)
              role3_count += 1
          mute_time = random.randint(1, 600)
          await ctx.send(f'你可以體驗呼吸的可貴'+ str(mute_time) + f'秒')
          await asyncio.sleep(mute_time)
          await member.remove_roles(role)
          await member.add_roles(role2)
          if (role3_count != 0):
            await member.add_roles(role3)
            role3_count == 0


def setup(bot):
    bot.add_cog(Main(bot))