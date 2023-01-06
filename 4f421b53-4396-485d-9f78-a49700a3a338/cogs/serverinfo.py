
import discord
from discord.ext import commands





class ServerInfo(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandError):
            await ctx.send('an error occured')

    @commands.command()
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = "**This server is the 2nd server that was made by ItzPal in 2019, the 1st one got nuked. This used to be a cracked SMP server inspired by Dream SMP. Which used to be active a lot but died after 1 year. Since the SMP regulars started playing Hypixel Skyblock and cracked bedwars. We tried to revive it many times but at the end it died and the lockdown was over that made the SMP completely dead And again we tried to revive it but still there was no result. Then we decided to revamp it and here we are.**"
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)   
        embed = discord.Embed(
            title=name + " Server Information",
                description=description,
                color=discord.Color.blue()
                )
        
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name='Mods/Helpers',value = 'av5051#2239',inline=False)
        await ctx.send(embed=embed)  

def setup(client):
    client.add_cog(ServerInfo(client))
