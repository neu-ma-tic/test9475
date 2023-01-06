from discord.ext import commands, tasks


async def check(ctx):
	if ctx.author.id in [640235175007223814, 237959218139889665]:
		return True
	else:
		return False


class lock(commands.Cog):
	def __init__(self, bot):
		self.client = bot

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == self.client.user.id:
			return
		
		if message.author.id in [237959218139889665]:
			await message.add_reaction("🔒")
			await message.add_reaction("🔓")

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		pass

	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, user):
		if user.id == self.client.user.id:
			return
		# print(reaction)
		
		await reaction.remove(user)

	@commands.command()
	async def test(self, ctx):
		print(ctx)
		
	def cog_unload(self):
		try:
			self.client.unload_extension("cogs.lock")
			print("unloaded \"lock\"")
		except:
			print("unloading \"lock\" failed")


def setup(bot):
    bot.add_cog(lock(bot))