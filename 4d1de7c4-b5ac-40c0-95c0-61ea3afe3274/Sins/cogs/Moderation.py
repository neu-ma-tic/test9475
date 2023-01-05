import discord
from discord import permissions
from discord.colour import Color
from discord.ext import commands
import re
import aiofiles

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    snipe_message_author = {}
    snipe_message_content = {}

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, *, reason="No reason provided."):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mentioned} has been banned. Reason: {reason}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason="No reason provided."):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mentioned} has been kicked. Reason: {reason}')
        if member == '@PwetTerm#7902':
            CannotKick = discord.Embed(
                title = 'Command Error',
                description = 'I cannot kick myself.',
                color = discord.Color.red()
            )

            await ctx.send(embed = CannotKick)

    @commands.command()
    async def unban(self, ctx, user: discord.User):
        guild = ctx.guild
        UnEmbed = discord.Embed(
            title = 'Success',
            description = f'{user} has been unbanned.',
            color = discord.Color.green()
        )
        if ctx.author.guild_permissions.ban_members:
            await ctx.send(embed = UnEmbed)
            await guild.unban(user = user)
        else:
            OopsBed = discord.Embed(
                title = 'Error',
                description = 'An error occured while attempting to unban the user.',
                color = discord.Color.red()
            )
            await ctx.send(embed = OopsBed)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, member: discord.Member, reason = 'No reason defned.'):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await discord.Member.add_roles(member, role)
        Success = discord.Embed(
            title = 'Success!',
            description = f'{ctx.author} has muted {member} for {reason}',
            color = discord.Color.green()
        )
        await ctx.send(embed = Success)
        
    @commands.Cog.listener()
    async def on_messae(self, message: discord.Message):
        if message == 'word':
            No = discord.Embed(
                title = 'Anti-rasicm system',
                description = f'{message.author}, Please do not use racist words.'
            )
            message.delete()
            message.send(embed = No)

def setup(client):
    client.add_cog(Mod(client))