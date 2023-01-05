from discord.ext import commands

# Because it acts like a password it is best practice to store your API token in an external text file
TOKEN_FILE = open("API.txt", "r")
TOKEN = TOKEN_FILE.read()

# All your commands must start with this prefix for your bot to respond
bot = commands.Bot(command_prefix='>')
#prevents spam
bot.owner_id = 634008988916121610



@commands.is_owner()
@bot.command()
async def ping(ctx):
    await ctx.send('>pong')


@commands.is_owner()
@bot.command()
async def logout(ctx):
    await ctx.bot.logout()


@commands.is_owner()
@bot.command()
async def reverse(ctx, arg):
  rev=""
  for x in range(len(arg)):
    rev=arg[x]+rev
  await ctx.send(rev)

@commands.is_owner()
@bot.command()
async def test(ctx, *args):
  await ctx.send(f"{len(args)} arguments: {', '.join(args)}")

@commands.is_owner()
@bot.command()
async def test1(ctx, *, arg):
    await ctx.send(ctx.message)

@commands.is_owner()
@bot.command()
async def another(ctx, arg):
  await ctx.send(arg)


bot.run(TOKEN)