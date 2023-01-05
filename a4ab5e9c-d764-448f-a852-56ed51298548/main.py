from webserver import keep_alive
import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os
import random
intents = discord.Intents.all()
intents.members = True 
client = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(client, sync_commands=True)
id = [889585104849088552]

@slash.slash(name="test", description="este es un comando de barra en test", guild_ids=id)
async def _test(ctx):
	await ctx.send("Hola! al ejecutar el comando de barra, todo salio bien ❤️")

@slash.slash(
	name="ping",
	description="Latencia del bot",
	guild_ids=id
)
async def _ping(ctx):
	num = ['3','4','5','6']
	await ctx.send(f"Ping: {random.choice(num)}ms")

keep_alive()
my = os.environ["KEY"] 
client.run(my)