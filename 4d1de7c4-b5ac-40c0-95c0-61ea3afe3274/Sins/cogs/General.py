import discord
from discord.colour import Color
from discord.ext import commands
import random
from discordTogether import DiscordTogether
import time
import datetime
from discord import voice_client
from nextcord.ext.commands.core import cooldown

class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rip(self, ctx):
        RIP = discord.Embed(
            title = 'End of discord.py.',
            description = 'Sadly, the main maintainer has now stepped down, no other contributors will step up, this means in April 2022 discord.py will no longer work. People are forking it and attempting to try and save it. If it ends, thousand of bots will end with it, includin Enders and mine. Please read the official statement at the discord.py github (https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1)',
            color = discord.Color.blue()
        )

        await ctx.send(embed = RIP)
    
    @commands.command()
    async def credits(self, ctx):
        CEmbed = discord.Embed(
            color = ctx.author.color
        )
        CEmbed.add_field(name = 'Credits', value = 'Sins#0023 - Bot Owner and Main Dev.\nEnder2K89#9999 - Helping me with some commands and helping with errors.')
        CEmbed.set_footer(text = f'Requested by: {ctx.author}', icon_url = ctx.author.avatar_url)

        await ctx.send(embed = CEmbed)

    @commands.command(aliases=['Update', 'update', 'updates'])
    async def Updates(self, ctx):
        UpdateBed = discord.Embed(color = ctx.author.color)
        UpdateBed.add_field(name = 'Bot updates', value = 'Added a kill command like Dank Memer.')
        UpdateBed.add_field(name = 'Current version', value = '```1.3 Credits')

        await ctx.send(embed = UpdateBed)

    @commands.command()
    async def say(self, ctx,*, arg):
            if '<@' in arg or '@everyone' in arg:
                await ctx.message.delete()

                AboozProtect= discord.Embed(
                    title = 'Abuse protection V1',
                    description = f'{ctx.author}, You cannot ping a member, role or everyone, this is to stop abuse.',
                    color = discord.Color.red()
                )

                await ctx.send(embed = AboozProtect)
            elif arg == 'fuck':

                SwearProtect= discord.Embed(
                    title = 'Swear protection V1',
                    description = f'{ctx.author}, You cannot swear using this bot to prevent rule breaking.',
                    color = discord.Color.red()
                )
                await ctx.message.delete()
                await ctx.send(embed = SwearProtect)
            else:
                await ctx.send(arg)
            
        #ErrorBed = discord.Embed(
            #title = 'Cannot cannot be ran',
            #description = 'Due to people using it to break the "No swearing" rule in many servers, this command will be disabled for now.'
        #)

    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has loaded all cogs and has encountered no errors on startup.')
        print('------------------------------------------------------------------------------')
        print(f'Username: {self.client.user.name}')
        print(f'ID: {self.client.user.id}')
        print('------------------------------------------------------------------------------')

    @commands.command()
    @commands.cooldown(1,200,commands.BucketType.member)
    async def kill(self, ctx, member: discord.Member):
        responses = [
            'Ate too much mcdonalds and died of loss of air.',
            'Died of starvation.',
            'Became a fornite kid.',
            'Fell down 100 staris and broke their neck',
            'Stopped lookng at scp-173 and got there neck snapped.',
            'Didnt duck when Arnold shot the temernator.',
            'Fell down a cliff while watching how to die.',
            'Just had enough and died.',
            'Got orbital striked.',
            'Got greifed by a Oppressor MK 2.',
            'Got caught by El Rubio.'
        ]

        await ctx.send(f'{member.mention} {random.choice(responses)}')

    @commands.command()
    async def invite(self, ctx):
        InvBed = discord.Embed(
            color = ctx.author.color
        )
        InvBed.add_field(name = 'Invite', value = 'To invite the bot to your server, use the following link: https://discord.com/api/oauth2/authorize?client_id=876563127829921803&permissions=8&scope=bot')

        await ctx.send(embed = InvBed)

    @commands.command()
    async def gulag(self, ctx, member : discord.Member = None):
        if member == None:
            NoMenGulag = discord.Embed(
                title = 'Gulag',
                description = f"{ctx.author.mention}, you have been sent to the gulag, you must fight your way out to get back to the battlefield.",
                color = discord.Color.dark_gray()
            )
            await ctx.send(embed = NoMenGulag)
        else:
            MentionedGulag = discord.Embed(
                title = 'Gulag',
                description = f"{member.mention} you have been sent to the gulag, you must fight your way out to get back to the battlefield.",
                color = discord.Color.dark_gray()
            )

def setup(client):
    client.add_cog(Utils(client))