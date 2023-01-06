from discord.ext import commands
import discord



class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.User = None,reason=None):
          try:
            embed=discord.Embed(colour=0xC0FF78)
            await ctx.guild.ban(member, reason=reason)
            embed.add_field(name="Banned!",value=f"{member} is banned. Reason: "+str(reason))
            
            await ctx.channel.send(embed=embed)
          except Exception as e:
            pass 
            embed=discord.Embed(description="I don't have permission to ban them :(", colour=discord.Colour.red())
            
            await ctx.send(embed=embed)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.User = None,reason=None):
          try:
            
            await ctx.guild.kick(member, reason=reason)
            embed = discord.Embed(
              description=(f"{member} is kicked. Reason: "+str(reason)),
              colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
          except Exception as e:
            pass 
            embed=discord.Embed(description="I don't have permission to kick them :(", colour=discord.Colour.blue())

    @commands.command()
    async def unban(self, ctx,*, member):
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split("#")

            for banned_entry in banned_users:
                user = banned_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f"{user.mention} has been unbanned.:sunglasses:")
                    return
    @commands.command()
    async def mute(self, ctx, member: discord.Member):
            role = ctx.guild.get_role(784168505498533920)
            guild = ctx.guild
            if role not in guild.roles:
                perms = discord.Permissions(send_messages=False, speak=False)
                await guild.create_role(name="Muted", permissions=perms)
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                await member.add_roles(role)
                embed = discord.Embed(
                    description=(f"{member} was muted."), colour=discord.Colour.red()
                )
                await ctx.send(embed=embed)
            else:
                await member.add_roles(role)
                embed = discord.Embed(
                    description=(f"{member} was muted."), colour=discord.Colour.red()
                )
                await ctx.send(embed=embed)
    @mute.error
    async def mute_error(self, ctx, error):
            if isinstance(error, commands.MissingRole):
              embed=discord.Embed(description=("You don't have permission to do this"),  colour=discord.Colour.blue())
              await ctx.send(embed=embed)
            elif isinstance(error, commands.BadArgument):
                embed=discord.Embed(description=("That is not a valid member"),  colour=discord.Colour.blue())
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member = None, reason=None):
          role = discord.utils.get(ctx.message.guild.roles, name="Muted")
          await member.remove_roles(role)
          embed=discord.Embed(colour=discord.Colour.green(),
          description=("Unmuted! :slight_smile: This user is unmuted!")
          )
          await ctx.send(embed=embed)

 


def setup(client):
  client.add_cog(ModCog(client))