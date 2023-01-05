import discord, json, asyncio

from random import choice
from discord.ext import commands
from hashlib import md5

class Tools(commands.Cog, description='Some tools'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def lhq(self, ctx: commands.Context):
      loop = 5

      for _ in range(loop):
        await ctx.send(f"lhq {choice(self.bot.emojis)}")


    @commands.command()
    async def timer(self, ctx: commands.Context, timer: int):
      message = await ctx.send(f'**{timer}**')
      for i in range(timer - 1, -1, -1):
        await asyncio.sleep(1.0)
        await message.edit(f'**{i}**')

    @commands.command(description="Change server's prefix", help='prefix <new prefix>', aliases=['changeprefix', 'prefixchange'])
    @commands.has_guild_permissions(administrator=True)
    async def prefix(self, ctx: commands.Context, prefix: str):
      if ' ' in prefix:
        return await ctx.send("You cannot set a prefix with space")
      with open('data_file/prefixes.json', 'r') as f:
        prefixes = json.load(f)

      key = md5(str(ctx.guild.id).encode()).hexdigest()
      prefixes[key] = prefix

      with open('data_file/prefixes.json', 'w') as f:
          json.dump(prefixes, f, indent=4)

      try:
        bot_as_member = await ctx.guild.fetch_member(self.bot.user.id)
        quote_index = bot_as_member.display_name.find('\"')
        nickname = bot_as_member.display_name[:quote_index]
        await bot_as_member.edit(nick=f'{nickname}"{prefix}"')
      except:
        pass

      return await ctx.send(f'Prefix changed to: {prefix}')

    @commands.command(description='Evaluate a basic math equation', help='calc <equation>\nEg: t.calc 1+1')
    async def calc(self, ctx: commands.Context, *, equation: str):
      try:
        return await ctx.reply(str(eval(equation.replace('x','*').replace(':','/').replace('mod','%').replace(',','.'))))
      except:
        return await ctx.reply('Please use correct syntax and make sure you evaluate basic operation only (+-*/%)(+-x:mod)')

    @commands.command(description='Fetch member avatar', help='avatar <user mention>')
    async def avatar(self, ctx: commands.Context, user: discord.Member):
      try:
        to_member = commands.MemberConverter()
        member = await to_member.convert(ctx, str(user))
        pfp = str(member.avatar_url)
        embed = discord.Embed(title=f"{member.display_name}'s avatar",
        description='', color=discord.Colour.blurple())
        embed.set_image(url=pfp)
        return await ctx.send(embed=embed)
      except commands.BadArgument or commands.CommandError:
        return await ctx.send('Not a valid member')
      except commands.UserNotFound:
        return await ctx.send('Member not found')