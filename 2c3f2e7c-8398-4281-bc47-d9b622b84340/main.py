import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ('!'))
bot = commands.Bot(command_prefix = ('$'))

@client.event
async def on_ready():
    print("Bot is ready.")
    print(client.user)

@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def users(ctx):
    for user in ctx.guild.members:
      print(user.status)


@client.command()
async def status(ctx):
  for user in ctx.guild.members:
    if ctx.guild.members.status_online == True:
      print('yes')

@client.command()
async def status2(ctx):
  async def get_all_members_ids(ctx, guild):
    for member in guild.members:
        yield member.id
        await ctx.send(get_all_members_ids)



token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)