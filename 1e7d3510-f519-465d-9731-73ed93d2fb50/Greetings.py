import discord
from discord.ext import commands

# for testing using delays
import time
import asyncio

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     channel = member.guild.system_channel
    #     if channel is not None:
    #         await channel.send(f'Welcome {member.mention}.')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}! {member.id}')
        else:
            await ctx.send(f'Hello {member.name}... It\'s you. {member.id}')
        self._last_member = member


# https://discordpy.readthedocs.io/en/latest/api.html#discord.Member.activities
    @commands.command()
    async def member(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        joined_at = member.joined_at
        activities = member.activities
        guild = member.guild
        nick = member.nick
        pending = member.pending # pending member verification
        await ctx.send(f"Joined at {joined_at}, doing {activities}, in guild {guild}, nickname: {nick}, pending: {pending}")
        self._last_member = member

    @commands.command()
    async def last_5_channel_messages_in_uol_general(self, ctx):
      # member = member or ctx.author
      channel = self.bot.get_channel(721014626753576970)
      current_channel = self.bot.get_channel(671384378517094400)
      messages = await channel.history(limit=5).flatten()
      # await ctx.send(messages)
      async with current_channel.typing():
        for msg in messages:
          await asyncio.sleep(1) # wait for 1s without blocking the whole thread
          await ctx.send(msg.content)

        # if word in msg.content:
        #   print(msg.jump_url)

    @commands.command()
    async def get_channel_id_from_name(self, ctx, *, channel_name: str = None):

      if channel_name is None:
        await ctx.send("Please call the function with channel name!")
      else: 
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        channel_id = channel.id
        await ctx.send(f"channel: {channel} channel_id: {channel_id}")

# context https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context.channel
    @commands.command()
    async def get_user_id_from_name(self, ctx, *, user_name: str = None):

      if user_name is None:
        await ctx.send("Please call the function with channel name!")
      else: 
        # channel = self.bot.get_channel(ctx.channel)
        channel = ctx.channel
        channel_id = channel.id

        # member = discord.utils.get(message.guild.members, name=user_name)

        await ctx.send(f"channel: {channel} channel_id: {channel_id}")

    @commands.command()
    async def reply_to_me(self, ctx):
      await ctx.reply("Yes, you got it, this is my reply.")




    @commands.command()
    async def reply_to_me(self, ctx):
      await ctx.reply("Yes, you got it, this is my reply.")

    # @commands.command()
    # async def bot_is_in(self, ctx, *, member: discord.Member = None):
    #   async for guild in self.bot.fetch_guilds(limit=150):
    #     print(guild.name)
    #   await ctx.send(f"I can't tell you where I am in...")

    # @commands.command()
    # async def im_really_in(self, ctx, *, member:discord.Member = None):
    #   guilds = await self.bot.fetch_guilds(limit=150).flatten()
    #   await ctx.send(f"{guilds}")
    #   await ctx.send(f"{type(guilds[0])}")

    # @commands.command()
    # async def msg(self, ctx, *, member:discord.Member = None, message):
    #   await ctx.send(f"{member}")
    #   await self.bot.send_message(member, message)

    # @commands.command()
    # async def whoami(self, ctx, *, member:discord.Member = None):

    #   member = member or ctx.author # either the argument is specified or the current author
    #   await ctx.send(f"You are {member}")



    # Must enable intents
    @commands.command()
    async def get_some_members(self, ctx, *, number_of_users_to_get: int = None):
      members_list = []
      members_count = 0
      number_of_users_to_get = number_of_users_to_get or 10
      async for member in ctx.guild.fetch_members(limit=number_of_users_to_get):
        members_list.append(member.name)
        members_count += 1
      await ctx.reply(f"{members_list}")
      await ctx.send(f"Total members count got: {members_count}. Be aware of character limit in Discord!")
    

    @commands.command()
    async def member_info(self, ctx, *, discord_member: discord.User = None):
      member = discord_member or ctx.author
      message: str = "" # message to send to the chatroom
      message = message + "Created date: " + str(member.created_at) + "\n" #created account
      message = message + "Joined date: " + str(member.joined_at) + "\n" #joined guild
      await ctx.send(message)


# https://discordpy.readthedocs.io/en/stable/api.html#embed
# https://python.plainenglish.io/send-an-embed-with-a-discord-bot-in-python-61d34c711046
    @commands.command()
    async def generate_embed(self, ctx):
      embed = discord.Embed(title="Generated embed", )
      await ctx.send(embed = embed)