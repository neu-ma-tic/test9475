import discord
from discord.ext import commands


class CustomHelp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title='Help', description='Use .help <command> for more information', color=ctx.author.color)
        embed.add_field(name='Moderation', value='kick, ban, unban, clear', inline=True)
        embed.add_field(name='Fun', value='8ball, meme, CoinFlip, movie, chooseGame', inline=False)
        embed.add_field(name='Music', value='play, queue, skip, stop, pause, resume, clearQ, disconnect, lyrics', inline=False)
        embed.add_field(name='Formula 1', value='f1drivers, f1constructors', inline=False)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        await ctx.send(embed=embed)

    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(title='kick', description='Kicks user from server', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.kick <member> [reason]', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(title='kick', description='Bans user from server', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.ban <member> [reason]', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def unban(self, ctx):
        embed = discord.Embed(title='unban', description='Unbans user from server', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.unban <member>', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def clear(self, ctx):
        embed = discord.Embed(title='clear', description='Clears messages from channel where command was typed', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.clear [amount]', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def play(self, ctx):
        embed = discord.Embed(title='play', description='Plays song from youtube', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.play/.p <song name or url>', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def queue(self, ctx):
        embed = discord.Embed(title='queue', description='Displays current queue of songs', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.queue/.q', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def skip(self, ctx):
        embed = discord.Embed(title='skip', description='Skips current song and plays next song in the queue', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.skip/.sk', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def lyrics(self, ctx):
        embed = discord.Embed(title='lyrics', description='Displays lyrics of song currently playing', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.lyrics/.l', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def stop(self, ctx):
        embed = discord.Embed(title='stop', description='Stops and ends current song(Cannot be resumed)', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.stop/.st', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def pause(self, ctx):
        embed = discord.Embed(title='pause', description='Pauses current song(can be resumed)', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.pause/.ps', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def resume(self, ctx):
        embed = discord.Embed(title='resume', description='Resumes a paused song', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.resume/.rs', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def clearQ(self, ctx):
        embed = discord.Embed(title='clearQ', description='Removes all songs from queue', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.clearQ/.cq', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def disconnect(self, ctx):
        embed = discord.Embed(title='disconnect', description='Disconnects the bot from voice channel', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.disconnect/.dc', inline=True)
        await ctx.send(embed=embed)

    @help.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        embed = discord.Embed(title='8ball', description='Predicts the future', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.8ball <question>', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(title='meme', description='Sends a funny meme in the channel', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.meme/.me', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def CoinFlip(self, ctx):
        embed = discord.Embed(title='CoinFlip', description='Coin flip between two users', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.CoinFlip/.cf <@User> <@User2>', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def chooseGame(self, ctx):
        embed = discord.Embed(title='chooseGame', description='Picks a game from entered selection', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.chooseGame/.cg <Game1 Game2 Game3 etc.> (no spaces in game name eg. '
                                             'Rocket League= RocketLeague) ', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def f1drivers(self, ctx):
        embed = discord.Embed(title='f1drivers', description='Gives current f1 drivers standings', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.f1drivers/.f1d <year>', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def f1constructors(self, ctx):
        embed = discord.Embed(title='f1constructors', description='Gives current f1 constructor standings', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.f1constructors/.f1con <year>', inline=True)
        await ctx.send(embed=embed)

    @help.command()
    async def movie(self, ctx):
        embed = discord.Embed(title='Movie', description='Gives information about movie or tv show you entered', color=ctx.author.color)
        embed.set_author(name='Camelot Bot')
        embed.set_footer(text='Bot created by Eggnogg')
        embed.add_field(name='Syntax', value='.movie <name>', inline=True)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(CustomHelp(client))
