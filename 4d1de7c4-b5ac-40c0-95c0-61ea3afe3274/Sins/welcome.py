import discord

class WelcomeClient(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user} ({self.user.id}).')

    async def on_member_join(self, member):
        guild = member.guild
        SetChannel = discord.Embed(
            title = f'<:SinsArrow:881323481768288267> New Member!',
           description = f'Hey {member}! Welcome to {guild.name}. We hope you have a great time here!',
           color = discord.Color.blurple()
        )
        

        await guild.system_channel.send(embed = SetChannel)




intents = discord.Intents.default()
intents.members = True

client = WelcomeClient(intents=intents)
client.run('ODc2NTYzMTI3ODI5OTIxODAz.YRl5Bw.QgJtpX34pKzP1MaorSkUPH-mmxs')

























