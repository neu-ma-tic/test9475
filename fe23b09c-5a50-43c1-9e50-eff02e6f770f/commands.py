import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from googleapiclient.discovery import build

google_api_key = "AIzaSyBkSn4COE3PsJD86WFnPTQU95sBZcR6SBE"
google_cse_id = "009898924031066437454:r4mgv0d34o2"


class AdminCommands(commands.Cog, name='🛠️ Settings'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="`!google [word]`\n\nGoogle Search the top 10 result of the said word.")
    async def google(self, ctx, *, word):

        await ctx.message.delete()

        search_result = ''

        def google_search(search_term, api_key, cse_id, **kwargs):
            service = build("customsearch", "v1", developerKey=api_key)
            res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
            return res["items"]

        results = google_search(word, google_api_key, google_cse_id, num=10)

        for result in results:
            search_result += f'{result["link"]}\n'

        embed = discord.Embed(
            description=f"Here are your top 10 Google Search results for the word `{word}`:\n\n{search_result}",
            color=0xff0000)
        embed.set_author(name="Google Search Results",
                         icon_url="https://w7.pngwing.com/pngs/882/225/png-transparent-google-logo-google-logo-google-search-icon-google-text-logo-business.png")
        embed.set_footer(text=ctx.message.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(description="`!roleinfo [role mention]`\n\nGets information of said role.")
    async def roleinfo(self, ctx, role: discord.Role):

        await ctx.message.delete()

        perms = role.permissions
        embed = discord.Embed(title="Role Info", description=f"Role Info - {role.name}", color=0xff0000)

        embed.add_field(name="Name", value=f"{role.name}", inline=True)
        embed.add_field(name="Position", value=f"{role.position}", inline=True)
        embed.add_field(name="Modifiable", value=f"{role.managed}", inline=True)
        embed.add_field(name="Permission", value=f"Administrator: {perms.administrator}\n"
                                                 f"Manage Channels: {perms.manage_channels}\n"
                                                 f"Manage Emojis: {perms.manage_emojis}\n"
                                                 f"Manage Server: {perms.manage_guild}\n"
                                                 f"Manage Permissions: {perms.manage_permissions}\n"
                                                 f"Manage Messages: {perms.manage_messages}\n"
                                                 f"Manage Roles: {perms.manage_roles}\n"
                                                 f"Mention Everyone: {perms.mention_everyone}\n"
                                                 f"Ban Members{perms.ban_members}\n"
                                                 f"Kick Members {perms.kick_members}\n"
                                                 f"Add Reactions: {perms.add_reactions}\n"
                                                 f"Send Messages: {perms.send_messages}\n"
                                                 f"Read Messages: {perms.read_messages}\n"
                                                 f"Send TTS Messages: {perms.send_tts_messages}\n")
        embed.add_field(name="Created on", value=role.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
        embed.add_field(name="Colour", value=f"{role.color}")

        await ctx.send(embed=embed)

    @commands.command(description="`!userinfo [mention]`\n\nGets information of said user.")
    async def userinfo(self, ctx, user: discord.Member = None):

        await ctx.message.delete()

        if user:

            embed = discord.Embed(colour=0xff0000, timestamp=ctx.message.created_at)
            roles = [role for role in user.roles]

            embed.set_author(name=f"{user.name}'s Information", icon_url=user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Name", value=f"{user}", inline=True)
            embed.add_field(name="Nickname", value=f"{user.nick}", inline=True)
            embed.add_field(name="ID", value=f"{user.id}", inline=True)
            embed.add_field(name="Avatar", value=f"[{user.name}'s Avatar Link]({user.avatar_url})", inline=True)

            embed.add_field(name="Created on", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                            inline=True)
            embed.add_field(name="Joined on", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)

            embed.add_field(name="Highest Role", value=f"{user.top_role.mention}", inline=True)
            embed.add_field(name=f"Roles ({len(roles)})", value=" ".join({role.mention for role in roles})[0:1000],
                            inline=True)

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(colour=0xff0000, timestamp=ctx.message.created_at)
            roles = [role for role in ctx.message.author.roles]

            embed.set_author(name=f"{ctx.message.author.name}'s Information", icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Name", value=f"{ctx.message.author}", inline=True)
            embed.add_field(name="Nickname", value=f"{ctx.message.author.nick}", inline=True)
            embed.add_field(name="ID", value=f"{ctx.message.author.id}", inline=True)
            embed.add_field(name="Avatar", value=f"[{ctx.message.author.name}'s Avatar Link]({ctx.message.author.avatar_url})", inline=True)

            embed.add_field(name="Created on", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                            inline=True)
            embed.add_field(name="Joined on", value=ctx.message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)

            embed.add_field(name="Highest Role", value=f"{ctx.message.author.top_role.mention}", inline=True)
            embed.add_field(name=f"Roles ({len(roles)})", value=" ".join({role.mention for role in roles})[0:1000],
                            inline=True)

            await ctx.send(embed=embed)


    @commands.command(description="`!serverinfo`\n\nGets information of this server.")
    async def serverinfo(self, ctx):

        await ctx.message.delete()

        server_id = ctx.message.guild.id

        ServerInfoEmbed = discord.Embed(title=f"{ctx.message.guild}'s Server Information", description="",
                                        color=0xff0000, timestamp=ctx.message.created_at)
        ServerInfoEmbed.set_thumbnail(url=ctx.message.guild.icon_url)
        ServerInfoEmbed.set_footer(text=f'Requested by {ctx.author}')
        ServerInfoEmbed.add_field(name='Server Owner:', value=ctx.message.guild.owner, inline=True)
        ServerInfoEmbed.add_field(name='Server ID:', value=server_id, inline=True)
        ServerInfoEmbed.add_field(name="Roles", value=f"{len(ctx.message.guild.roles)}", inline=True)
        ServerInfoEmbed.add_field(name='Region', value=ctx.message.guild.region, inline=True)
        ServerInfoEmbed.add_field(name='Verification Level', value=f"{ctx.message.guild.verification_level}")
        ServerInfoEmbed.add_field(name='Highest role', value=ctx.message.guild.roles[0])
        ServerInfoEmbed.add_field(name='Number of emotes', value=f"{len(ctx.message.guild.emojis)}")
        ServerInfoEmbed.add_field(name='Created on',
                                  value=ctx.message.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        ServerInfoEmbed.add_field(name='Server Boost Level',
                                  value=f"{ctx.message.guild.premium_tier} ({ctx.message.guild.premium_subscription_count} Boosts)")

        bot = 0

        for member in ctx.guild.members:

            if member.bot:
                bot += 1

        ServerInfoEmbed.add_field(name='Member Count',
                                  value=f'Members 👥: {len(ctx.message.guild.members)}\nRobot 🤖: {bot}', inline=False)

        await ctx.send(embed=ServerInfoEmbed)

    @commands.command(description="`!avatar [mention]\n\nGets the avatar information of the said user.")
    async def avatar(self, ctx, avamember: discord.Member = None):

        await ctx.message.delete()

        if avamember:

            userAvatarUrl = avamember.avatar_url
            embed = discord.Embed(color=0xff0000)
            embed.set_footer(text=f"{avamember}", icon_url=userAvatarUrl)
            embed.set_footer(text=ctx.message.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url=userAvatarUrl)
            await ctx.send(embed=embed)
            await ctx.send(f"{avamember}")

        else:

            userAvatarUrl = ctx.message.author.avatar_url
            embed = discord.Embed(color=0xff0000)
            embed.set_footer(text=ctx.message.author, icon_url=userAvatarUrl)
            embed.set_author(name=ctx.message.author, icon_url=userAvatarUrl)
            embed.set_image(url=userAvatarUrl)
            await ctx.send(embed=embed)

    @commands.command(description="`!lockdown`\n\nLocks the channel that this command was posted to.")
    async def lockdown(self, ctx):

        await ctx.message.delete()

        await ctx.message.channel.set_permissions(ctx.message.guild.default_role, send_messages=False)
        embed = discord.Embed(description=f"{ctx.message.channel} channel is now on lock down!")
        await ctx.send(embed=embed)

    @commands.command(description="`!unlock`\n\nUnlocks the channel that this command was posted to.")
    async def unlock(self, ctx):

        await ctx.message.delete()

        await ctx.message.channel.set_permissions(ctx.message.guild.default_role, send_messages=True)
        embed = discord.Embed(description=f"{ctx.message.channel} channel is now out of lock down!")
        await ctx.send(embed=embed)

    @commands.command(
        description="`!clear [amount] [user(optional)]`\n\nPrunes message in a channel. Requires Manage Message Permission.")
    async def clear(self, ctx, amount: int, member: discord.Member = None):

        await ctx.message.delete()

        if 0 < amount < 101:

            if member:

                def user(m):

                    return m.author == member

                deleted = await ctx.channel.purge(limit=100, check=lambda m: m.author.id == 59152242862723072)
                embed = discord.Embed(description=f"Deleted {len(deleted)} messages of " + str(member) + "!",
                                      color=0x4797b1)
                embed.set_footer(text=ctx.message.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

            else:

                deleted = await ctx.channel.purge(limit=amount)
                embed = discord.Embed(description=f'Deleted {len(deleted)} messages!', color=0x4797b1)
                embed.set_footer(text=ctx.message.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:

            embed = discord.Embed(description="Amount has to be an integer between 1 to 100!")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AdminCommands(bot))
