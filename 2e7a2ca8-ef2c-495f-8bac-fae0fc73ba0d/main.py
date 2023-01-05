import discord
from discord.ext import commands
import random
import os
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} Has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member}Has left the server')

#  Start of the response commands

@client.command(aliases=['Commands'])
async def com(ctx):
  await ctx.send("Here are the list of commands you can use to utilize me to my full potential\n Please keep in mind that you must use my command prefix '.' before the command to summon me and my all mighty never ending wisdom.\n 1. 8ball follwed by a question of your choice, this will summon the magic 8ball **user experience may vary**\n father -aliases Father, husband, Husban\n Hello Dadbot - Please make sure to say Hello to DadBot, he works nonstop to make sure he is availble to service this server \n whoami - This will allow you to identify yourself, you know, just incase you are having one of those days and you can\'t remember who you are \n Math subject - typing out a math subject as a command will summon a list of websites that will help you with the subject of math that you are having issues with. " )


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['Father', 'Husband', 'husband'])
async def father(ctx, *, question):
    responses = ["Yeah, how about NO.",
                 "I can not foresee this happening",
                 "That's cute",
                 "Maybe when you bring home straight A's",
                 "Outside sure is beautiful today",
                 "Shh... Shhhhhhhh... Shhhhhhhhhhhh",
                 "I bet she did",
                 "That's what she said",
                 "bUt I AlReADy DId ThE DiSHeS",
                 "You know what they say",
                 "That's what she said!"]
    await ctx.send(f"Qustion: {question}\nAnswer: {random.choice(responses)}")


@client.command(aliases=['Hello DadBot'])
async def Hello(ctx):
    await ctx.send(f"Hello {ctx.message.author.name}")


@client.command(name="whoami")
async def whoami(ctx):
    await ctx.send(f"You are {ctx.message.author.name}")


@client.command(aliases=['geometry'])
async def Geometry(ctx):
    await ctx.send(f"Here is a list of websites I found to help you with your Geometry Homework.\n"
                   "https://www.khanacademy.org/math/geometry")

#  End of response commands.


@client.command()
async def clear(ctx, amount=10):  # This is used to clear chat from the server.
    # The default amount is set to 10 if no other amount is specified 10 messaged will be deleted.
    await ctx.channel.purge(limit=amount)


#  Start of kick/ban features, ending with the unban feature.


@client.command()
# Kick feature. Reason can be added after the username while kicking any user in discord.
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)  # EG: !kick @user#1234 Obsene Language.


@client.command()
# Same as the kick feature from above. Reason can be added.
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)                                 #
    await ctx.send(f'Banned {member.mention}')                      #


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    # Starts at @client.command and ends at return. This is the feature that is used to unban users.
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#  End of the kick/ban features.

# testing auto-reply feature with no command prompt


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'test':
        await message.channel.send('Testing Uno, Dos, Tres!')

    await client.process_commands(message)
    

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'I hate School':
        await message.channel.send('You\' hate life alot more than you hate school if you don\'t stick with it!')

    await client.process_commands(message)


# Start of the Cogs feature

@client.command()                                       #
async def load(ctx, extension):                         #
    client.load_extension(f'cogs.{extension}')


@client.command()                                       #
async def reload(ctx, extension):                       #
    client.reload_extension(f'cogs.{extension}')        #
    # Loads and unloads cogs


@client.command()                                       #
async def unload(ctx, extension):                       #
    client.unload_extension(f'cogs.{extension}')        #


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.loadextension(f'cogs.{filename[:-3]}')






#cogs to transfer to new file

"""

import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is online.')

            @commands.command()
            async def ping(self, ctx):
                await ctx.send('Pong!')


def setup(client):
    client.add_cog(Example(client))

"""