import discord
from discord.ui import Button, View
from discord.ext import commands

SallysIntents = discord.Intents.all()
Doing = discord.Game(name = "Halo Infinite")
Sally = commands.Bot(command_prefix = '*',
                     intents = SallysIntents,
                     activity = Doing,
                     status = discord.Status.online
                    )

@Sally.event
async def on_ready():
    from users import TOFU 
    Tofu = discord.utils.find(lambda Tofu: Tofu.id == TOFU, Sally.guilds[0].members)
    await Tofu.send('Awating orders master')

# from Cogs.DebugCog import DebugCog
# Sally.add_cog(DebugCog(Sally))

from Cogs.ReactionRolesCog import ReactRolesCog
Sally.add_cog(ReactRolesCog(Sally))

# from Cogs.MemVerCog import MemverCog
# Sally.add_cog(MemverCog(Sally))

# from Cogs.RequestCog import RequestCog
# Sally.add_cog(RequestCog(Sally))

@Sally.command()
async def ping(ctx):
    button1 = Button(label = 'SUCK', style=discord.ButtonStyle.green)
    button2 = Button(label = 'MY'  , style=discord.ButtonStyle.blurple)
    button3 = Button(style = discord.ButtonStyle.red, emoji = '🍆')
    view = View(button1, button2, button3)

    await ctx.send('.', view = view)

with open('token.txt') as File:
    Sally.run(File.read())