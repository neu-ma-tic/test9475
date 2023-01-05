import discord

from discord_components import Select, SelectOption
from discord.ext import commands

from commands.nsfw import NSFW
from commands.randomize import Randomize
from commands.games import Games
from commands.tools import Tools
from commands.greeting import Greeting
from commands.vn import VN


async def send_embed(ctx: commands.Context, embed: discord.Embed):
    """
    Function that handles the sending of embeds
    -> Takes context and embed to send
    - tries to send embed in channel
    - tries to send normal message when that fails
    - tries to send embed private with information abot missing permissions
    If this all fails: https://youtu.be/dQw4w9WgXcQ
    """
    try:
        await ctx.send(embed=embed)
    except discord.Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except discord.Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *input):
        """Shows all modules of that bot"""
	
	# !SET THOSE VARIABLES TO MAKE THE COG FUNCTIONAL!
        prefix = 't.'# ENTER YOUR PREFIX - loaded from config, as string or how ever you want!
        version =  '1.7.3'
        
        # setting owner name - if you don't wanna be mentioned remove line 49-60 and adjust help text (line 88) 
        owner = 	408620714799661056# ENTER YOU DISCORD-ID
        owner_name = 	'ChezziJr#5124'# ENTER YOUR USERNAME#1234

        # checks if cog parameter was given
        # if not: sending all modules and commands not associated with a cog
        if not input:
            # checks if owner is on this server - used to 'tag' owner
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError:
                owner = owner

            # starting to build embed
            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `help <module>` to gain more information about that module '
                                            f':smiley:\n')

            # iterating trough cogs, gathering descriptions
            """cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'`{cog}` {self.bot.cogs[cog].description}\n'"""

            # adding 'list' of cogs to embed
            emb.add_field(name='Modules', value=f'A total of {len(self.bot.cogs)} modules', inline=False)
            '''for cog in self.bot.cogs:
                emb.add_field(name=cog, value=self.bot.cogs[cog].description, inline=False)'''

            # integrating trough uncategorized commands
            """commands_desc = ''
            for command in self.bot.walk_commands():
                # if cog not in a cog
                # listing command if cog name is None and command isn't hidden
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            # adding those commands to embed
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)"""

            # setting information about author
            emb.add_field(name="About", value=f"The Bots is developed by {owner_name}, based on discord.py.")
            emb.set_footer(text=f"Bot is running {version}\nThis server's prefix: {prefix}")

            modulesOption = [SelectOption(label=cog, 
            value=cog,
            description=self.bot.cogs[cog].description)
              for cog in self.bot.cogs
            ]

            try:
                msg = await ctx.send(embed=emb, components = [Select(
                  placeholder='Choose a module',
                  options = modulesOption
                )])
                interaction = await self.bot.wait_for('select_option', check=None)
                temp = interaction.component
                
                label = interaction.values[0]

                e = discord.Embed(title=f'{label} - Commands', description=self.bot.cogs[label].description,
                                        color=discord.Color.green())
                e.add_field(name='How to use', value='''
**<a>:**\thave to provide a
**<a | b>:**\tchoose between a and b
**(a):**\tno need to provide a
**[list]:**\tprovide as many as you want
                ''')
                    # getting commands from cog
                for command in self.bot.get_cog(label).get_commands():
                        # if cog is not hidden
                    if not command.hidden:
                        e.add_field(name=f"`{command.name}`", value=f'{command.help}\n{command.description}', inline=False)

                return await msg.edit(embed=e, components=[])

            except discord.Forbidden:
                try:
                    return await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
                except discord.Forbidden:
                    return await ctx.author.send(
                        f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                        f"May you inform the server team about this issue? :slight_smile: ", embed=emb)

        # block called when one cog-name is given
        # trying to find matching cog and it's commands
        elif len(input) == 1:

            # iterating trough cogs
            for cog in self.bot.cogs:
                # check if cog is the matching one
                if cog.lower() == input[0].lower():

                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].description,
                                        color=discord.Color.green())
                    emb.add_field(name='How to use', value='''
                    **<a>:**     have to provide a
                    **<a | b>:** choose between a and b
                    **(a):**     no need to provide a
                    **[list]:**  provide as many as you want
                    ''')
                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"`{command.name}`", value=f'{command.help}\n{command.description}', inline=False)
                    # found cog - breaking loop
                    break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=discord.Color.orange())

        # too many cogs requested - only one at a time allowed
        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=discord.Color.orange())

        else:
            emb = discord.Embed(title="It's a magical place.",
                                description="I don't know how you got here. But I didn't see this coming at all.\n",
                                color=discord.Color.red())

        # sending reply embed using our own function defined above
        await send_embed(ctx, emb)



def setup(bot: commands.Bot):
  bot.add_cog(Greeting(bot))
  bot.add_cog(Games(bot))
  bot.add_cog(Tools(bot))
  bot.add_cog(Randomize(bot))
  bot.add_cog(VN(bot))
  bot.add_cog(NSFW(bot))
  bot.add_cog(Help(bot))
