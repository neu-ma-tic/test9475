import discord

client = discord.Client()

prefix = '$'

@client.event

async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
    
    global prefix

    if message.author == client.user:
        return

    if message.content == prefix + 'hello':
        await message.channel.send('hello!')

    if message.content == prefix + 'prefix':
        prefix.replace(' ', '')
        prefix = message.content[len(prefix) + 6:]
        await message.channel.send('prefix set to ' + prefix)


client.run('ODE0NzMxODc0MjExNTk0Mjkw.YDiILw.9ZRBkKF5oMcuykJxZ4VM4AHgNF8')