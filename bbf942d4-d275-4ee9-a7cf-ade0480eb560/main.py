import discord
import os
from keepAlive import keepAlive
client = discord.Client() #This is the client of the server

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if (message.author==client.user):  #This is so that the bot doesn't replies to it's own message
		return

	if(message.content.startswith('!CallMeDaddy')):
		await message.channel.send('{} is my daddy'.format(message.author.name))

keepAlive()
client.run(os.getenv('TOKEN'))	



