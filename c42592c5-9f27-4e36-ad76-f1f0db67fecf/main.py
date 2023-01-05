import discord
from discord.ext import commands
import asyncio
import random
anna = 0
client = commands.Bot(command_prefix = 'u ')
client.remove_command('help')

@client.command()
async def msg(ctx, word, *, message):
    word = int(word)

    channel = client.get_channel(word)

    await channel.send(message)

@client.event
async def on_ready():
  print('-client online')

@client.command()
async def ping(ctx):
    await ctx.send(f'**PONG!** *{round(client.latency * 1000)} ms*')




@client.event
async def on_message(message):
  if message.author == client.user:
    return
  emoji = ['😀','😁','👽','🤬','👌','👅','🥰','🥵','👋🏻','⚡️','🍆','🔪','✏️',
  '🍌','💔','❤️']

  await message.add_reaction(random.choice(emoji))
 


  if message.content.startswith('hi'):
    if message.author.id == 685459390840832001:
      
      print('anna is cool')
      list = [f'{message.author.mention} your awesome', 'Hiii <3', '<3']

      await message.channel.send(random.choice(list))
    else:

      

      list = ['you suck', 'Everything is bad', 'nobody likes you go to sleep😎',
      'Youre a great person. JK GO DIE😎','Your have nothing to offer 🤗', 'you probably have no money and want to die 🤑', 'youre a shit 💩', 'hi go kill yourself😴']

      await message.channel.send(random.choice(list))
  if message.author.id == 155120915665911808:
    if isinstance(message.channel, discord.DMChannel):
    
      message = message.content
      channel = client.get_channel(689168506306297934)

      await channel.send(message)

  



async def text():
  while True:
    stuff = input('> ')
    channel = client.get_channel(689168506306297934)

    await channel.send(stuff)




async def chg_pr():
    await client.wait_until_ready()

    statuses =['with things a long pink thing', 'with toys ;)', 'with your mom', 'around', 'with young girls', 'sexy girls :)']

    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(status))

        await asyncio.sleep(25)



client.loop.create_task(chg_pr())
client.run('NTg3MzcwOTI1NzQ2NDIxNzYx.XtgBwg.NBiLlXW70filE5XfkMWZ_3TnFXA')