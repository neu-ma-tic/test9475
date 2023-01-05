import discord
import os 
from discord.ext import commands


TOKEN = 'NzkxMTcxMjY0NzY4MjQ1Nzkw.X-LRqA.xeLTrY8PA3IFY3wiWBvYwayFPyk'

bot = commands.Bot(command_prefix='$')

print('Running........')


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


# commands
commands_embed = discord.Embed(title="Commands", url='', description="**$bitchcount** = shows the amount of bitches the user have.\n\n**$niggercount** = shows you the amount of niggers in the server\n\n**$stfu** = tells the user to shut the fuck up\n\n**$kys** = tells the user to kill himself\n\n**$version** = tells the user the version of the bot\n\n**$hello** = sends a nice hello message :)\n\n**$nuke** = nukes the server\n\n**$ratio** = you will need to find out yourself.\n\n\n**More Commands Coming Soon....**")
commands_embed.set_author(name="Bot Daun", icon_url='')
commands_embed.set_footer(text="Nemo#1819 All rights Reserved ©")


# giveaway
gwgw_embed = discord.Embed(title="Giveaway", url='', description="**Text**")
gwgw_embed.set_author(name="author", icon_url='')
gwgw_embed.set_footer(text="XJOWHUISKJDHNKH9281793NJKHD")


# bitch count
embed2 = discord.Embed(title="Bitch Counter", url='', description="**Bitch Count:**1 (chel's mom)\n")

# stfu
stfu_embed = discord.Embed(title="Man shut yo Bitchass up nigga\n", url='', description="")


# version
version_embed = discord.Embed(title="Bot Daun", url='', description="**Version:** v0.01\n")

# hello
hello_embed = discord.Embed(title="fuck you dumbass nigga\n", url='', description="")

# nibber
nibber_embed = discord.Embed(title="Nigger Counter", url='', description="**2 Niggers found in this server**\n")


# ratio full text
ratio_embed = discord.Embed(title="", url='', description="**L + ratio + wrong + get a job + unfunny + you fell off + never liked you anyway + cope + ur allergic to gluten + don't care + cringe ur a kid + literally shut the fuck up + galileo did it better + your avi was made in MS Excel + ur bf is kinda ugly + i have more subscribers + owned + ur a toddler + reverse double take back + u sleep in a different bedroom from your wife + get rekt + i said it better + u smell + copy + who asked + dead game + seethe + ur a coward + stay mad + you main yuumi + aired + you drive a fiat 500 + the hood watches xqc now + yo mama + ok + currently listening to rizzle kicks without u. plus ur mind numbingly stupid plus ur voice is ronald mcdonald.**")



@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content == '$help':
    await message.channel.send(embed=commands_embed)

  if message.content == '$giveaway':
    await message.channel.send(embed=gwgw_embed)
    
  if message.content == '$hello':
    await message.reply(embed=hello_embed)
    
  if message.content == '$version':
    await message.reply(embed=version_embed)
    
  if message.content == '$bitchcount':
    await message.reply(embed=embed2)
    
  if message.content == '$stfu':
    await message.reply(embed=stfu_embed)

  if message.content == '$ratio':
    await message.reply(embed=ratio_embed)
    
  if message.content == '$kys':
    await message.reply('KyS :)')

  if message.content == '$niggercount':
     await message.reply(embed=nibber_embed)
   
  if message.content == '$nuke':
    i = 0
    while i < 100:
      await message.reply('@everyone')
      i = i + 1
      print("Ping Count: ", i)

  if 'XJOWHUISKJDHNKH9281793NJKHD' in message.content:
    emoji32 = '\N{PARTY POPPER}'
    await message.add_reaction(emoji32)
  
  if 'w/l' in message.content:
    emoji = '\N{THUMBS UP SIGN}'
    emoji2 = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji)
    await message.add_reaction(emoji2)
  elif 'W/l' in message.content:
    emoji = '\N{THUMBS UP SIGN}'
    emoji2 = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji)
    await message.add_reaction(emoji2)
  elif 'W/L' in message.content:
    emoji = '\N{THUMBS UP SIGN}'
    emoji2 = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji)
    await message.add_reaction(emoji2)
  elif 'w/L' in message.content:
    emoji = '\N{THUMBS UP SIGN}'
    emoji2 = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji)
    await message.add_reaction(emoji2)


 

      




bot.run('NzkxMTcxMjY0NzY4MjQ1Nzkw.X-LRqA.xeLTrY8PA3IFY3wiWBvYwayFPyk')
