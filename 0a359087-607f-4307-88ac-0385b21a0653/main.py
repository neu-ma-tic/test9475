import discord
import os
my_secret = os.environ['token']


client = discord.Client()

@client.event
async def on_ready():
	print('We have logged on as {0.client}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user :
		print()
	
	if message.content.startswith('!hello'):
		await message.channel.send('Hello there!')


client.run(token)
