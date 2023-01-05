import discord
import random

TOKEN = 'OTMwMjA3MDc4NjYyOTU5MTQ1.Ydyg2Q.Z8Hnaj23JDP33MDSnQX1M5nzHwg'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return

    if message.channel.name == '✔〡bump':
        if user_message.lower() == '!bm':
            await message.channel.send(f'!d bump')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!buying':
        await message.channel.send('**Check The Info Channel Before Doing Anything!**')
        return


client.run(TOKEN)