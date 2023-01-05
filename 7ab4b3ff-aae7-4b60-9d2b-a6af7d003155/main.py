import discord
import os
# import requests
# import json
from discord.ext import commands, tasks
from itertools import cycle
from ka import keep_alive

client=commands.Bot(command_prefix='$')
statl=cycle(['stat_1','stat_2'])

# def get_quote():
#     qdata=requests.get("https://zenquotes.io/api/random")
#     # print(qdata.text)
#     jsondata=json.loads(qdata.text)
#     return(jsondata[0]['q']+" -"+jsondata[0]['a'])

@client.event
async def on_ready():
  print("{0.user} is ready and logged in.".format(client))
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Peek-a-Boo'))
  change_stat.start()

@tasks.loop(seconds=10)
async def change_stat():
  await client.change_presence(activity=discord.Game(next(statl)))

@client.command()
async def heya(ctx, *, name1=""):
  if name1 =="" or name1 == " ":
    await ctx.send(f"Hello {ctx.author.name}")
  elif name1.lower() =="bot1":
    await ctx.send(f"Hello to you :) {ctx.author.mention}")
  else:
    await ctx.send(f"You said hello to {name1}")# "+str(mes.author).split("#")[0])

@client.command()
async def ping(ctx):  
  await ctx.send(f"{round(client.latency*1000)}ms Pong!")

@client.command()
async def id(ctx):  
  await ctx.send(f"Your user id is {ctx.message.author.id}!")

# @client.command(aliases=['inspire'])
# async def _inspire(ctx):
#   await ctx.send(get_quote())

@client.command()
async def clear(ctx, amount=5):
  if ctx.message.author.id == 691251613179838475:
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def kick(ctx,member: discord.Member, *, reason=None):
  if ctx.message.author.id == 691251613179838475:
    await member.kick(reason=reason)

@client.command()
async def ban(ctx,member: discord.Member, *, reason=None):
  if ctx.message.author.id == 691251613179838475:
    await member.ban(reason=reason)
    await ctx.send(f"Unbanned {member.mention}")

@client.command()
async def unban(ctx, *, member):
  if ctx.message.author.id == 691251613179838475:
    banned_users= await ctx.guild.bans()
    member_name, member_discriminator=member.split('#')

    for ban_entry in banned_users:
      user=ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user.mention}")
        return

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'Extension {extension} loaded')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send(f'Extension {extension} unloaded')

for cog in os.listdir('./cogs'):
  if cog.endswith('.py'):
    client.load_extension(f'cogs.{cog[:-3]}')

@client.command()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'Extension {extension} reloaded')

# @client.event
# async def on_message(mes):
#   if mes.author == client.user:
#     return
#   await mes.channel.send("My Chatting ability is yet to be developed.")

@client.command()
async def own(ctx):
  if ctx.message.author.id == 691251613179838475: #replace OWNERID with your user id
    await ctx.send("Hello maker!")
  else:
    await ctx.send("You do not own me, stupid fuck!")


# @client.command()
# async def shutdown(ctx):
#   if ctx.message.author.id == 691251613179838475: #replace OWNERID with your user id
#     print("shutdown")
#     try:
#       await self.bot.logout()
#     except:
#       print("EnvironmentError")
#       self.bot.clear()
#   else:
#     await ctx.send("You do not own this bot!")
keep_alive()
client.run(os.getenv('TOKEN'))
