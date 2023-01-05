#Imports
import discord
import os
from discord.ext import commands



Bot = commands.Bot(command_prefix=('$'), intents = discord.Intents.all(), help_command = None)

#Bot = commands.Bot(activity=Bot_activity, allowed_mentions=allowed_mentions, command_prefix=get_prefix, description=Bot_description, emojis=list_emojis, help_command=none, intents=intents, owner_ids=list_owners, )

#References
Cstatus = 'Status: PreAlpha '
Cversion = 'Version 0.0.1'

#Bot is ready 
@Bot.event
async def on_ready():
  print('Bot is ready, ' + 'We have logged in as {0.user}'.format(Bot))
  print('Curent version of Continental Bot is: ' + Cstatus + Cversion)
  print('Curent version of Discord.py is: ' + discord.__version__)
  
  


#Member join 
@Bot.event 
async def on_member_join(member):  
  channel =  member.guild.voice_channels[0]
  await channel.edit(name = f"Total members: {member.guild.member_count}")
  #приветственое сообщение 
  #создание пользовотеля в базе данных 
  
@Bot.event 
async def on_member_remove(member):  
  channel =  member.guild.voice_channels[0]
  await channel.edit(name = "Total members: " + str(member.guild.member_count))  
  #прощальное сообщение
  #изменения статуса пользовотеля в БД 


#system messages 
@Bot.event 
async def on_message(message):
  await Bot.process_commands(message)

@Bot.command()
async def Help(ctx, *arg):
      page1 = discord.Embed(title='Page 1/3',
                              description='Description',
                              colour=discord.Colour.dark_gold())
      page2 = discord.Embed(title='Page 2/3',
                              description='Description',
                              colour=discord.Colour.dark_gold())
      page3 = discord.Embed(title='Page 3/3',
                              description='Description',
                              colour=discord.Colour.dark_gold())

      pages = [page1, page2, page3]

      message = await ctx.send(embed=page1)
      await message.add_reaction('⏮')
      await message.add_reaction('◀')
      await message.add_reaction('▶')
      await message.add_reaction('⏭')

      def check(reaction, user):
          return user == ctx.author

      i = 0
      reaction = None

      while True:
          if str(reaction) == '⏮':
              i = 0
              await message.edit(embed=pages[i])
          elif str(reaction) == '◀':
              if i > 0:
                  i -= 1
                  await message.edit(embed=pages[i])
          elif str(reaction) == '▶':
              if i < 2:
                  i += 1
                  await message.edit(embed=pages[i])
          elif str(reaction) == '⏭':
              i = 2
              await message.edit(embed=pages[i])

          try:
              reaction, user = await Bot.wait_for('reaction_add',
                                                  timeout=30.0,
                                                  check=check)
              await message.remove_reaction(reaction, user)
          except:
              break

      await message.clear_reactions()

Bot.run('ODIwMjIzMTQzMTg0MzAyMDgx.YEyCVA.8pwbbtZGPvCrAQPq79O2xSWetKk')