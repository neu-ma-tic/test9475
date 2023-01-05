import os
from difflib import SequenceMatcher

import discord

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()
history = []
def similar(a,b):
	return SequenceMatcher(None, a, b).ratio()
@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	#sequence matching
	ok = 1
	for x in history:
		if similar(x, message.content) > 0.8:
			await message.channel.send("High probability of copied message in "+ message.channel.name + "which was" + x)
			ok = 0;
	if ok:
		history.append(message.content)
		await message.channel.send("Good!")
		
	# await message.channel.purge(limit=10000)

client.run(TOKEN)
