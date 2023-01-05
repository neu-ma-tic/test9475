import discord
import random
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os


client = commands.Bot(command_prefix = 'Adde ')
client.remove_command('help')

@client.event
async def on_message(message):
    print('Someone sent a message huh weird i though the server was dead')
    await client.process_commands(message)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Do Adde help. [Adde ]'))
    print('Single and ready to mingle.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'**I Unbanned** {user.mention} :thumbsup:')
            return

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'**I Have Banned** {member.mention} :thumbsup:')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms :)')

@client.command()
async def info(ctx):
    await ctx.send(f'This bot is developed by: **Mildaknutten#8669** Its under development so expect bugs :flag_se:')

@client.command()
async def CatPink(ctx):
    await ctx.send(f'**Heres your cat pic :cat: ** https://imgur.com/QSkZOqE')

@client.command()
async def CatWat(ctx):
    await ctx.send(f'**Heres your cat pic :cat: ** https://imgur.com/1BmrGGU')

@client.command()
async def CatCmds(ctx):
    await ctx.send(f'**Heres all the commands for cat pictures** - CatWat - CatSleep - CatPink')

@client.command()
async def CatSleep(ctx):
    await ctx.send(f'**Heres your cat pic :cat: ** https://imgur.com/JUEkRlR')


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Help Command 2',
        description='This displays all Commands',
        colour=discord.Colour.blue()
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/620228893114105886/672515841413218344/Adde.png')
    embed.add_field(name='Adde help', value='This command is displayed right now.', inline=False)
    embed.add_field(name='Adde purge', value='This command is used to purge messages. Example: Adde purge 10', inline=False)
    embed.add_field(name='Adde ban', value='This command is used to ban a member. Example: Adde ban (Mentioned User)', inline=False)
    embed.add_field(name='Adde kick', value='This command is used to kick a member. Example: Adde kick (Mentioned User)', inline=False)
    embed.add_field(name='Adde ping', value='This command is used to display the bots current ping.', inline=False)
    embed.add_field(name='Adde unban', value='This command is used to unban a member. Example: Adde unban Member#0001', inline=False)
    embed.add_field(name='Adde info', value='This command is used to display the bot information.', inline=False)
    embed.add_field(name='Adde mute', value='This command is used to mute a member. Example: Adde mute (Mentioned member): Need to have a Muted role with Permission to send messages disabled.', inline=False)
    embed.add_field(name='Adde unmute', value='This command is used to unmute a member!. Example: Adde unmute (Member mentioned)', inline=False)
    embed.add_field(name=':)', value='help2 For more commands.', inline=False)

    await ctx.send(embed=embed)

@client.command()
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not member:
        await ctx.send("**Please specify a member!** :thumbsdown: ")
        return
    await member.add_roles(role)
    await ctx.send("**Muted!** :thumbsup: ")

@client.command()
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not member:
        await ctx.send("**Please specify a member**! :thumbsdown: ")
        return
    await member.remove_roles(role)
    await ctx.send("**Unmuted!** :thumbsup: ")

@client.command()
async def help2(ctx):
    embed = discord.Embed(
        title='Help2 Command',
        description='This displays all Commands.',
        colour=discord.Colour.blue()
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/620228893114105886/672515841413218344/Adde.png')
    embed.add_field(name='help2', value='Currently displayed.', inline=False)
    embed.add_field(name='Adde CatCmds', value='This command is used to show all Cat Commands.', inline=False)
    embed.add_field(name='Aball', value='This is a Aball its a question randomizer. Example: Adde Aball', inline=False)
    embed.add_field(name=' :cat: ', value='**More Commands Soon**', inline=False)

    await ctx.send(embed=embed)


@client.command()
async def Aball(ctx):
    choices = (
    "No", "Yes", "Yes - definitely", "Don't count on it", "Very doubtful.", "Probably not.", "Cannot predict now", "Why did u even ask that.", "Outlook not so good.", "Ask again later.", "You may rely on it.", "Outlook good.", "Hell yeah!", "Signs point to yes.", "Yazz queen!", "Hell no!")
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

client.run('NjcxNjM4NDYyNzQ2NzIyMzE0.XjFd8w.pKr6t9EApUxkQbxnXEezkJs6RcI')
