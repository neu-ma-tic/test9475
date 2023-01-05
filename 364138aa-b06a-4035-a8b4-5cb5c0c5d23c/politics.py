import discord
from discord.ext import commands
from discord.utils import get
from replit import db

class Voting(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.has_role("BotDev")
  @commands.command(name='vote', help='See your job title')
  async def poll(self, ctx, question:str, *options:str):
    print('ran')
    print(question)
    print('Ran')

    print(len(options))
    if len(options) <= 1:
        await ctx.send("Error! A poll must have more than one option.")
        return
    if len(options) > 2:
        await ctx.send("Error! Poll can have no more than two options.")
        return

    if len(options) == 2 and options[0] == "yes" and options[1] == "no":
        reactions = ['👍', '👎']
    else:
        reactions = ['👍', '👎']

    description = []
    for x, option in enumerate(options):
        description += '\n\n {} {}'.format(reactions[x], option)

    embed = discord.Embed(title = question, color = 3553599, description = ''.join(description))

    react_message = await ctx.send(embed = embed)

    for reaction in reactions[:len(options)]:
        await self.bot.add_reaction(react_message, reaction)

    embed.set_footer(text='Poll ID: {}'.format(react_message.id))

    await ctx.send(react_message, embed=embed)