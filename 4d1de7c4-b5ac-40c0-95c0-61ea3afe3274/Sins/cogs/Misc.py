from nextcord import embeds
from Main import get_prefix
import discord
from discord import permissions
from discord.colour import Color
from discord.ext import commands
from discord import user
import discord
import random
from discord import message
from discord import Client
from discord import client
import json


class Misc(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	def get_prefix(client, message):
		with open ('prefixes.json', 'r') as f:
			prefixes = json.load(f)

		return prefixes[str(message.guild.id)]

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = self.client.get_channel(id)
		WelcomeEmbed = discord.Embed(
			title = 'Welcome!',
			description = f'Welcome {member.mention} to {member.guild.name}!',
			color = discord.Color.random()
		)

		await channel.send(embed = WelcomeEmbed)
	
	@commands.Cog.listener()
	async def on_message(self, message):
		pings = [f'<@<{self.client.user.id}>', f'<@!{self.client.user.id}>']
		if message.content in pings:
			await message.reply(f"Hey, my prefix is: {get_prefix(client, message)}. To get a list of commands, run {get_prefix(client, message)}help.")

	@commands.command()
	@commands.is_owner()
	async def rules(self, ctx):
		RuleEmbed = discord.Embed(
			title = f'Server Rules - {ctx.guild.name}',
			description = 'Please follow these rules to make sure you dont get kicked/banned.',
			color = ctx.author.color
		)
		RuleEmbed.add_field(
			name = '- Rule 1 -',
			value = 'Please make sure to follow the discord terms of service. (can be fund at https://discord.com/tos)',
			inline = False
		)
		RuleEmbed.add_field(
			name = '- Rule 2 -',
			value = 'Please try to keep swearing to a mininal.',
			inline = False
		)
		RuleEmbed.add_field(
			name = '- Rule 3 -',
			value = 'Do not attempt to abuse the bot or any of the commands at any point.',
			inline = False
		)
		RuleEmbed.add_field(
			name = '- Rule 4 -',
			value = 'Do not use any racist slurs such as the n-word or any word that if offensive to 1 or more race.',
			inline = False
		)
		RuleEmbed.add_field(
			name = '- Rule 5 -',
			value = 'Do not talk to teens in a sexual way.',
			inline = False
		)
		RuleEmbed.add_field(
			name = '- Rule 6 -',
			value = 'Do not argue back to staff or try to avoide a ban/punishment.',
			inline = False
		)


		await ctx.send(embed = RuleEmbed)

	@commands.command()
	@commands.is_owner()
	async def toggle(self, ctx, *, command):
		command = self.client.get_command(command)

		if command is None:
			await ctx.send(f'Error, {command} was not found.')

		elif ctx.command == command:
			await ctx.send('This command cannot be disabled.')
		else:
			command.enabled = not command.enabled
			ternary = 'enabled' if command.enabled else 'disabled'
			await ctx.send(f'I have {ternary} {command.qualified_name}.')

def setup(client):
	client.add_cog(Misc(client))