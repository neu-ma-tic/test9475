import discord
import random
import datetime

TOKEN = 'ODcxNTc4OTUxNjMyNDQ1NDgw.YQdXJw.9wVV8W6f8nWD-Nv1v01Yxniv8T0'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,       activity=discord.Game("Reading your messages 👀"))
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Hey :wave:",
        description=f'Welcome to **{member.guild}**, {member.name} !',
        colour=discord.Colour.pink()
    )

    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member}', icon_url='https://pbs.twimg.com/media/EbtdoOoWkAEQbQN.jpg')
    embed.add_field(name=f'Total Members:', value=f'{len(list(member.guild.members))}', inline=False)
    embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
    embed.timestamp = datetime.datetime.utcnow()

    print("User joined " + str(member))
    guild = client.get_guild(871579547315896350)
    channel = guild.get_channel(872163485147091006)
    rules_channel = guild.get_channel(872164830499467345)
    await channel.send(embed=embed)
    await member.send(f'''
Hey **{member}**, welcome to {guild} !
Before you get to chatting, **make sure to read** {rules_channel} :scroll: !
Have fun!''')
    return


@client.event
async def on_member_remove(member):
    print('User left server ' + str(member))
    embed = discord.Embed(
        title="Bye :wave:",
        description=f'Sad to see you go, **{member.name}**!',
        colour=discord.Colour.dark_grey()
    )

    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member}', icon_url='https://pbs.twimg.com/media/EbtdoOoWkAEQbQN.jpg')
    embed.add_field(name=f'Total Members:', value=f'{len(list(member.guild.members))}', inline=False)
    embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
    embed.timestamp = datetime.datetime.utcnow()

    guild = client.get_guild(871579547315896350)
    channel = guild.get_channel(872516571602501663)
    await channel.send(embed=embed)
    return


@client.event
async def on_message(message):
    guild = client.get_guild(871579547315896350)
    username = str(message.author.name)
    message_sent = str(message.content)
    general = guild.get_channel(871579547315896353)
    commands = guild.get_channel(872313893551226931)
    if message.channel == general:
        # All messages in General will be read from here
        if message_sent.lower() == "hello":
            await message.channel.send(f'Hello there {username}!')
            return

    # Here on is all messages in commands channel
    elif message.channel == commands:
        if message_sent == "-members":
            embed = discord.Embed(
                title='Command: -members',
                colour=discord.Colour.dark_grey()
            )

            embed.set_thumbnail(url='https://pbs.twimg.com/media/EbtdoOoWkAEQbQN.jpg')
            embed.add_field(name=f'Total Members:', value=f'{len(list(guild.members))}', inline=False)
            embed.set_footer(text=f'{guild}', icon_url=f'{guild.icon_url}')
            embed.timestamp = datetime.datetime.utcnow()

            await commands.send(embed=embed)
            return
        elif message_sent == "-random":
            embed = discord.Embed(
                title='Command: -random',
                colour=discord.Colour.dark_grey()
            )

            embed.add_field(name=f'Your number:', value=str(random.randint(0, 1001)), inline=False)
            embed.set_footer(text=f'{guild}', icon_url=f'{guild.icon_url}')
            embed.timestamp = datetime.datetime.utcnow()

            await commands.send(embed=embed)
            return

        elif message_sent == "-serverinfo":
            embed = discord.Embed(
                title='Command: -serverinfo',
                colour=discord.Colour.dark_grey()
            )

            embed.add_field(name=f'Members:', value=len(list(guild.members)), inline=False)
            embed.add_field(name=f'')
            embed.set_footer(text=f'{guild}', icon_url=f'{guild.icon_url}')
            embed.timestamp = datetime.datetime.utcnow()

            await commands.send(embed=embed)
            return
        

client.run(TOKEN)
