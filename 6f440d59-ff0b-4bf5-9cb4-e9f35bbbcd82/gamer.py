from discord.ext import commands
import discord
bot = commands.Bot(command_prefix='/')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    await ctx.send('0!t2020fp1')

@bot.command()
async def aaa(ctx):
    await ctx.send(':ez:')

@bot.command()
async def Wee(ctx):
    await ctx.send('Dudududududuudududududududududududududududududuududm')

@bot.command()
async def fop(ctx):
    await ctx.send('oooof')
    
@bot.command()
async def cmds(ctx):
    await ctx.send('/Wee, /fop, /obama, /dmme(the discors user).')
    
@bot.command()
async def obama(ctx):
    await ctx.send('https://youtu.be/FIlug3WYtPk')

@bot.command()
async def si(ctx):
    await ctx.send('https://tenor.com/view/skillissue-skill-issue-gif-22125481')
    
@bot.command()
async def ihm(ctx):
    await ctx.send('https://tenor.com/view/sarcasm-gif-20360578')

@bot.command()
async def jvc(ctx):
    await ctx.send('https://tenor.com/view/join-vc-vc-join-join-voice-chat-voice-gif-19300161')

@bot.command()
async def dmme(ctx):
    await ctx.send("If you want the commands say '/cmds'")

@bot.command()
async def ef(ctx):
    await ctx.send("https://tenor.com/view/epic-embed-fail-ryan-gosling-cereal-embed-failure-laugh-at-this-user-gif-20627924")

@bot.command()
async def efv2(ctx):
    await ctx.send("https://tenor.com/view/nikocado-avocado-epic-embed-fail-epic-embed-gif-23508659")

        
@bot.command()
async def spam(ctx):
    while (1 == 1):
      await ctx.send('@PanzerGrenadier#1883')

@bot.command()
async def test(ctx):
    await ctx.send('_**ur mom**_')
      
@bot.command()
async def alphabet(ctx):
  await ctx.send('a')
  await ctx.send('b')
  await ctx.send('c')
  await ctx.send('d')
  await ctx.send('e')
  await ctx.send('f')
  await ctx.send('g')
  await ctx.send('h')
  await ctx.send('i')
  await ctx.send('j')
  await ctx.send('k')
  await ctx.send('l')
  await ctx.send('m')
  await ctx.send('n')
  await ctx.send('o')
  await ctx.send('p')
  await ctx.send('q')
  await ctx.send('r')
  await ctx.send('s')
  await ctx.send('t')
  await ctx.send('u')
  await ctx.send('v')
  await ctx.send('w')
  await ctx.send('x')
  await ctx.send('y')
  await ctx.send('z')
  
@bot.command()
async def dab(ctx):
  await ctx.send('@here')
  

@bot.command(pass_context=True)
async def baguette(ctx, user:discord.User):
    await user.send('https://gyazo.com/e82a4a9fb06ee5c4bc8d5b621204f376')
    
bot.run ('c73af5b43e07b6fee97674cd68fd0be0f681a7c7582e008ec57c66824bc45343')