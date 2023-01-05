import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('you suck'):
        await message.channel.send('no u')


client.run('ODkxOTQxNTIwMDQ1OTI4NDk4.YVFrRQ.6Q3XLfjrTZMEL3bOkno3qqxWbSA')