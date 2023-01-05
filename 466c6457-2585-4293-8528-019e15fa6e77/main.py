import discord
import typing
from discord.ext import commands, tasks
import os

from keep_alive import keep_alive

client = discord.Client()

client = commands.Bot(command_prefix = 'DE!')
client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help Commands", description="*Hey looks like you found the command center!*", color=0xFFFF00)
    embed.add_field(name="🛠️Moderation", value="`DE!help_moderation`")
    embed.add_field(name="🤖bot info", value="`DE!bot_info`")
    embed.add_field(name="🤪Fun", value="`DE!help_fun`")
    embed.set_footer(text="add my bot")
    embed.set_author(name="Dragon Elite")     

    await ctx.send(embed=embed)

@client.command()
async def help_fun(ctx):
    embed = discord.Embed(title="Fun area", description="This is the fun area commands!", color=0x0000FF)
    embed.add_field(name="slap", value="`DE! slap <user> <reason>")
    embed.add_field(name="something else", value="something")
    embed.add_field(name="something", value="something")
    embed.set_footer(text="Add my bot")
    embed.set_author(name="Dragon Elite")     

    await ctx.send(embed=embed)
    
@client.command()
async def help_moderation(ctx):
    embed = discord.Embed(title="Moderation Area", description="Hi welcome to moderation area commands!", color=0x00FF00)
    embed.add_field(name="Kick", value="`DE!kick <user> <reason>`")
    embed.add_field(name="purge", value="`DE!purge <number>`")
    embed.add_field(name="Ban", value="`DE!ban <user> <reason>`")
    embed.set_footer(text="Add my bot")
    embed.set_author(name="Dragon Elite")     

    await ctx.send(embed=embed)

4389387947328498324344434344
@client.event
async def on_ready():
    print("Bot is ready/Update is working!")
    print(client.user)

@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')
558345954345353535355
@client.command()
async def bottles(ctx, amount: typing.Optional[int] = 55, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))

@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)
  
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that! You don't have the perms for this!")

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.online, activity=discord.game('DE!help | 2021!'))
dddvcxf
keep_alive()3487573589353785858358348953858487538758973487548435567897655678976578976546789765e467897657897654567877777390948248330482403924820394820423402842094820984209840942840284029482042843204823042403284032948
token = os.environ.get("DISCORD_BOT_SECRET")
client.run("Nzk5NDUzMDM4NTMxNzA2OTQw.YADyqQ.cCGZUnOxqr2vl-gI8H-SLn9SFRw")erturtirseyeruotuyesrtuetur;tuidzurtutuot;ozyuaerziotozdrtdrcuxzgdfufxdiudifzdxrfliutrrgfiulsegiudLGRrduzgyhd;g.zdhrguzrtyzldrt