import discord
import os
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
			return
			
	if message.content.startswith('$hello'):
				await message.channel.send('Hello!')
				
	if message.content.startswith('$penis'):
					await message.channel.send('www.meatspin.com')

@client.event
async def on_voice_state_update(member,before,after):
	friends = [9313]
	channel = after.channel
	if channel and member.id in friends:
		await client.kick()
client.run(os.getenv('TOKEN'))