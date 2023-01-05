import discord
from discord.ext import commands


class Help(commands.Cog, name="Help"):

    def __init__(self, bot):
        self.bot = bot
        print("help.py extension has loaded!")

    commands.command(
        name='help',
        description='The help command!',
        aliases=['commands', 'command'],
        usage='cog')

    @commands.command()
    async def help(self, ctx):

        # The third parameter comes into play when
        # only one word argument has to be passed by the user

        # Get a list of all cogs

        cogs = [c for c in self.bot.cogs.keys()]

        # If cog is specified by the user, we list the specific cog and commands with it

        global embed
        hidden_cogs = ['Help', 'Logs']

        embed = discord.Embed(title="Ghost-chan's Help Menu",
                              description=f"`!myprefix` for this server's prefix and `!setprefix` to change this server's prefix.\n\n`!about` for more information about Ghost-chan! \n\nGhost Ping Alert is by default active in every channel Ghost-chan has access to.\n",
                              color=0x69babe)
        embed.set_thumbnail(url="https://i.imgur.com/3Lgs39V.png")
        embed.set_footer(
            text=f"Requested by {ctx.message.author.name} :: Your server's prefix currently is !",
            icon_url=self.bot.user.avatar_url)

        for cog in cogs:

            if cog not in hidden_cogs:

                cog_commands = self.bot.get_cog(cog).get_commands()
                commands_list = ''

                for comm in cog_commands:
                    commands_list += f'`{comm}` '

                embed.add_field(name=cog, value=commands_list, inline=True)

        msg = await ctx.send(embed=embed)

        await msg.add_reaction('🛠')

        def check(reaction, user):

            return str(reaction.emoji) in ['🛠'] and user == ctx.message.author

        async def handle_reaction(reaction, msg, check):

            if str(reaction.emoji) == '🛠':

                help_embed = discord.Embed(title='🛠 Settings Help')
                help_embed.set_footer(
                    text=f"Requested by {ctx.message.author.name} :: Your server's prefix currently is !",
                    icon_url=self.bot.user.avatar_url)

                cog_commands = self.bot.get_cog('🛠️ Settings').get_commands()
                commands_list = ''

                for comm in cog_commands:
                    commands_list += f'**{comm.name}** - {comm.description}\n'

                    help_embed.add_field(name=comm, value=comm.description, inline=True)

                await msg.edit(embed=help_embed)

            else:

                return

            reaction, user = await self.bot.wait_for('reaction_remove', check=check, timeout=30)
            await handle_reaction(reaction, msg, check)

        reaction, user = await self.bot.wait_for('reaction_remove', check=check, timeout=30)
        await handle_reaction(reaction, msg, check)


def setup(bot):
    bot.add_cog(Help(bot))
