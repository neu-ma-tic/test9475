@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name="!help commands | Vote me on top.gg now!"))