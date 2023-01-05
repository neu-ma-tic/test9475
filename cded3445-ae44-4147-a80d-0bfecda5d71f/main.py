import discord

client = discord.Client()
bot = commands.Bot(command_prefix="e!", description="WIP bot.")

@client.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_prescence(game=discord.Game(name='e!help'))

@bot.command()
async def ping(ctx): 
  await bot.send('help')

client = MyClient()
client.run('NzE3NDQzNTk2MzQ0NjIzMTQ2.XtaZsA.aDSepfBwU4PIwVhwBCU1XPYc4FM')