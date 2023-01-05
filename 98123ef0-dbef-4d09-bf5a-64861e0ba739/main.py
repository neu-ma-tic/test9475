import discord

from discord.utils import get
from discord.ext import commands
from urllib import parse, request
import re
import asyncio

intents = discord.Intents.all()
discord.member = True
bot = commands.Bot(command_prefix="+",intents = intents)
bot.remove_command('help')


@bot.command()
async def report(ctx, user: discord.Member = None, reason: str = None):
    reportchannel = bot.get_guild(966391169938493460).get_channel(977546153442824222)
    if user == None:
        await ctx.send("gebe eine user an", delete_after=5)
        return

    if reason == None:
        await ctx.send("gebe eine grund an", delete_after=5)
        return

    embed1 = discord.Embed(
        title="ReportSystem",
        description=f"Gemeldeter user:\n@{user.name}\nGemeldet von:\n@{ctx.author.name}\nGrund:\n{reason}",
        color=discord.Color.red()
    )

    embed2 = discord.Embed(
        title="ReportSystem",
        description=f"Dein Report wurde gesendet\nGemeldeter user:\n@{user.name}",
        color=discord.Color.purple()
    )
    await reportchannel.send(embed=embed1)
    await ctx.author.send(embed=embed2)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def help(ctx):
    embed1 = discord.Embed(
        title="HelpSystem",
        description=f"kommt noch",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed1)

# Events
@bot.event
async def on_ready():
    print(f'{bot.user.name} ist aktiviert!')
    Channel = bot.get_channel(966402969878794310)
    Text= "Reagiere um die Regeln zu akzeptieren"
    Moji = await Channel.send(Text)
    await Moji.add_reaction('✅')
    bot.loop.create_task(status_task())
    
async def status_task():
        while True:
               await bot.change_presence(activity=discord.Streaming(name="YT: LoadetZeroHead", url="http://twitch.tv/Loadet0Head"))
               await asyncio.sleep(3)
               await bot.change_presence(activity=discord.Streaming(name="+help", url="http://twitch.tv/Loadet0Head"))
               await asyncio.sleep(3)

@bot.event
async def on_member_join(member):
    joinchannel = bot.get_channel(966402271611076638)
    embed=discord.Embed(title="JoinSystem", description=f":zap: {member.mention} ist dem Server beigetreten :zap: ", color=discord.Color.blue())
    await joinchannel.send(embed=embed)

@bot.event
async def on_reaction_add(reaction, user):
    Channel = bot.get_channel(966402969878794310)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "✅":
      guild = bot.get_guild(966391169938493460)
      role1 = get(guild.roles, id=975407067168903188)
      role2 = get(guild.roles, id=1005796272399192114)
      role3 = get(guild.roles, id=1005796412761583657)
      role4 = get(guild.roles, id=975409742732222504)
      await user.add_roles(role1,role2,role3,role4)

@bot.event
async def on_reaction_remove(reaction, user):
    Channel = bot.get_channel(966402969878794310)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "✅":
      guild = bot.get_guild(966391169938493460)
      role1 = get(guild.roles, id=975407067168903188)
      role2 = get(guild.roles, id=1005796272399192114)
      role3 = get(guild.roles, id=1005796412761583657)
      role4 = get(guild.roles, id=975409742732222504)
      await user.remove_roles(role1,role2,role3,role4)


@bot.listen()
async def on_message(message, amount=1):
    if "http" in message.content.lower():
        await message.channel.purge(limit=amount)
        await message.author.send('Hör auf damit!')
        await bot.process_commands(message)
    if "www" in message.content.lower():
        await message.channel.purge(limit=amount)
        await message.author.send('Hör auf damit!')
        await bot.process_commands(message)

bot.run('OTc3NTc5MzY1OTkyOTE5MDgx.Gv2_qQ.gF31_LUzrHmTvdIbow8eP-ajI_Sbtwqi_7_hto')