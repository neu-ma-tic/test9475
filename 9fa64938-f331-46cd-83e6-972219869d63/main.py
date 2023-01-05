import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Zalogowano jako {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

if message.channel.name == 'general':
    if user_message.lower() == 'hello':
        await message.channel.send('Hello {username}')
      return

    elif user_message.lower() == "bye":
        await message.channel.send(f'see you later{username}')
        return
    elif user_message.lower() == "!random":
        response = f'This is your random number: {random.randrange(1000000)}'
        await message.channel.send(response)
        return


client.run(os.getenv('TOKEN'))
