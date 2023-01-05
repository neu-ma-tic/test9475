from os import kill
from re import A
from subprocess import call
import time
import discord
from discord import invite
from discord import client
from discord.colour import Color
from discord.enums import Status
from discord.errors import DiscordServerError
from discord.ext import commands
from platform import python_version
from discord import __version__ as discord_version
import json
import os

version = '1.3 (Beta)'

class Utilites(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, command =  None):
        if command == None:
            HelpBed = discord.Embed(
                title = 'Help',
                color = ctx.author.color
            )
            HelpBed.add_field(name = 'General', value = ' *credits, *Updates, *say, *kill, *invite, *start, *stats')
            HelpBed.add_field(name = 'Utilites', value = ' *ping, *help, *userinfo, *serverinfo ')
            HelpBed.add_field(name = 'Moderation', value = ' *kick, *ban ')
            HelpBed.add_field(name = 'Note', value = 'If you chnaged the bots prefix, then replace * with the prefix you set.', inline = False)
            return await ctx.send(embed=HelpBed)

        if command == 'kick':
            KickBed = discord.Embed(
                title = 'Help - Kick',
                color = ctx.author.color
            )
            KickBed.add_field(name = 'Description', value = ' When command is used, the mentioned user will be kicked. ')
            KickBed.add_field(name = 'Usage', value = ' *kick {mention a user} ')

            return await ctx.send(embed = KickBed)

        if command == 'ban':
            BanBed = discord.Embed(
                title = 'Help - Ban',
                color = ctx.author.color
            )
            BanBed.add_field(name = 'Description', value = ' When used, the mentioned user will be banned. ')
            BanBed.add_field(name = 'Usage', value = ' *ban {mention a user} ')

            return await ctx.send(embed = BanBed)

        if command == 'ping':
            PingBed = discord.Embed(
                title = 'Help - Ping',
                color = ctx.author.color
            )
            PingBed.add_field(name = 'Description', value = ' Shows the delay of the bot to run a command. ')
            PingBed.add_field(name = 'Usage', value = ' *ping ')

            return await ctx.send(embed = PingBed)

        if command == 'credits':
            CreditBed = discord.Embed(
                title = 'Help - Credits',
                color = ctx.author.color
            )
            CreditBed.add_field(name = 'Description', value = ' Shows who made/contributed in the making of the bot. ')
            CreditBed.add_field(name = 'Usage', value = ' *credits ')

            await ctx.send(embed = CreditBed)

        if command == 'start':
            StartEmbed = discord.Embed(
                title = 'Help - Start',
                color = ctx.author.color
            )
            StartEmbed.add_field(name = 'Description', value = ' When ran, provides a link that engages a Youtube Together app. You can wach youtube with your friends ')
            StartEmbed.add_field(name = 'Usage', value = ' *start ')

            await ctx.send(embed = StartEmbed)

        if command == 'kill':
            KillBed = discord.Embed(
                title = 'Help - Kill',
                color = ctx.author.color
            )
            KillBed.add_field(name = 'Description', value = ' When ran, it will display a dank memer like death message. ')
            KillBed.add_field(name = 'Usage', value = ' *kill {mention a member} ')

            await ctx.send(embed = KillBed)

        if command == 'serverinfo':
            SIEmbed = discord.Embed(
                title = 'Help - Server Information',
                color = ctx.author.color
            )
            SIEmbed.add_field(
                name = 'Description',
                value = 'This command displays information about the server the command was used in. '
            )
            SIEmbed.add_field(
                name = 'Usage',
                value = '*severinfo'
            )

            await ctx.send(embed = SIEmbed)

        if command == 'unban':
            Unban = discord.Embed(
                title = 'Help - Unban',
                color = ctx.author.color
            )
            Unban.add_field(
                name = 'Description',
                value = 'Unbans a user from the server.'
            )



    @commands.command()
    async def ping(self, ctx):
        PingBed = discord.Embed(
            color = ctx.author.color
        )
        PingBed.add_field(name = 'Client Latency: ', value = f'{round(self.client.latency * 1000)} ms. ')

        await ctx.send(embed = PingBed)

    @commands.command(aliases = ['ui'])
    async def userinfo(self, ctx, member: discord.Member):

        roles = [role for role in member.roles]
        status = str(member.status)
        discr = str(member.discriminator)
        status = str(member.status)

        UIEmbed = discord.Embed(color = member.color, timestamp = ctx.message.created_at)
        UIEmbed.set_author(name=f'User info - {member}')
        UIEmbed.set_thumbnail(url = member.avatar_url)
        UIEmbed.set_footer(text = f'Requested by: {ctx.author}', icon_url = ctx.author.avatar_url)

        UIEmbed.add_field(name = 'ID', value = f' {member.id} ')
        UIEmbed.add_field(name = 'Name', value = f' {member.display_name} ')
        UIEmbed.add_field(name = 'Created at', value = f' {member.created_at.strftime("%a, %d, %B, %Y, %I, %I:%M %p BST")} ', inline = False)
        UIEmbed.add_field(name = 'Joined server at', value = f' {member.joined_at.strftime("%a, %d, %B, %Y, %I, %I:%M %p BST")} ')
        UIEmbed.add_field(name = f'Roles ({len(roles)})', value = ''.join([role.mention for role in roles]))
        UIEmbed.add_field(name = 'Bot?', value = f' {member.bot} ')
        UIEmbed.add_field(name = 'User status', value = status.title())
        UIEmbed.add_field(name = 'Discriminator', value = discr)

        await ctx.send(embed = UIEmbed)


    @commands.command(pass_context = True, aliases = ['si'])
    async def serverinfo(self, ctx):
        SIEmbed = discord.Embed(
            title ='Sever/Guild Information',
            color = ctx.author.color
        )
        name = str(ctx.guild.name)
        icon = str(ctx.guild.icon_url)
        Mcount = str(ctx.guild.member_count)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region).title()
        owner = str(ctx.guild.owner)
        create = str(ctx.guild.created_at.strftime("%a, %d, %B, %Y, %I:%M %p BST"))
        roles = len(ctx.guild.roles)

        SIEmbed.add_field(
            name = 'Guild name:',
            value = name
        )
        SIEmbed.add_field(
            name = 'ID:',
            value = id
        )
        SIEmbed.add_field(
            name = 'Owner:',
            value = owner
        )
        SIEmbed.add_field(
            name = 'Region:',
            value = region
        )
        SIEmbed.add_field(
            name = 'Member count:',
            value = Mcount
        )
        SIEmbed.add_field(
            name = 'Created at:',
            value = create
        )
        SIEmbed.add_field(
            name = 'Role Count:',
            value = roles
        )
        SIEmbed.add_field(
            name = 'Emojis',
            value = len(ctx.author.guild.emojis)
        )

        await ctx.send(embed = SIEmbed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:

            link = ctx.author.avatar_url

            NoMemAva = discord.Embed(
                title = f'Avatar - {ctx.author}',
                color = ctx.author.color
            )
            NoMemAva.add_field(
                name = 'Username:',
                value = ctx.author.mention
            )
            NoMemAva.add_field(
                name = 'Avatar link:',
                value = f'[Click here]({ctx.author.avatar_url})'
            )

            await ctx.send(embed = NoMemAva)
        else:
            link2 = member.avatar_url

            MemAva = discord.Embed(
                title = f'Avatar - {member}',
                color = member.color
            )
            MemAva.add_field(
                name = 'Username:',
                value = member.mention
            )
            MemAva.add_field(
                name = 'Avatar link:',
                value = f'[Click here]({member.avatar_url})'
            )

            await ctx.send(embed = MemAva)

    @commands.command()
    async def stats(self, ctx):
        Status = discord.Embed(
            title = 'Bot stats',
            color = ctx.author.color,
            thumbnail = self.client.user.avatar_url
        )
        Status.add_field(
            name = 'Python Version:',
            value = python_version()
        )
        Status.add_field(
            name = 'Bot version:',
            value = version
        )
        Status.add_field(
            name = 'Discord.py Version:',
            value = discord_version
        )
        Status.add_field(
            name = 'Ping:',
            value = f'{round(self.client.latency * 1000)} ms'
        )
        Status.add_field(
            name = 'Cogs:',
            value = len(self.client.cogs)
        )

        await ctx.send(embed = Status)

    @commands.command()
    @commands.is_owner()
    async def client_logout(self, ctx):
        lougout = discord.Embed(
            title = 'Lougout started.',
            description = 'Shutting down...',
            color = discord.Color.red()
        )
        
        await ctx.send(embed = lougout)
        await self.client.logout()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        Error = discord.Embed(
            title = 'Command error.',
            description = f'An error occured while attempting to run then command. Error: {error}.',
            color = ctx.author.color
        )
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(embed = Error)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.reply(f'Hmm, the command you tried to run was not found, please run ``*help`` to check the commands that are usable.')
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.reply(embed = Error)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.delete()
            await ctx.reply(embed = Error)

def setup(client):
    client.add_cog(Utilites(client))