import discord

TOKEN = 'OTExMTYzNDMwMDU1MDYzNTUy.YZdZEg.e2en0VhkQ2qwMYB77LkdGTxyA8A'

client = discord.Client()

temp = 0

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.author == client.user:

      if message.content.startswith('Desired'):

        return

      else:

        await message.add_reaction('☑️')
        await message.add_reaction('🔄')
        await message.add_reaction('1️⃣')
        await message.add_reaction('5️⃣')
        await message.add_reaction('🔟')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#TODO
#decide on what to print after user has either confirmed or denied the desired amount,
#sol#1: "Enter desired amount: "
#...

@client.event
async def on_raw_reaction_add(payload):

  global temp

  x = client.get_channel(payload.channel_id)

  if payload.user_id == 911163430055063552:

    return

  else:

    if (payload.emoji.name == '☑️'):

      print_statement = 'Desired amount: '+ str(temp) + '?'

      y = await x.send(print_statement)

      await y.add_reaction('✅')

      await y.add_reaction('❌')

    elif (payload.emoji.name == '🔄'):

      temp = 0

    elif (payload.emoji.name == '1️⃣'):

      temp += 1

    elif (payload.emoji.name == '5️⃣'):

      temp += 5

    elif (payload.emoji.name == '🔟'):

      temp += 10

    elif (payload.emoji.name == '✅'):
      
      y = await x.send(f'{payload.member.name} has supplied X garage with {temp * 1000} BMats.')

      temp = 0

    elif (payload.emoji.name == '❌'):

      temp = 0

    else:

      return



@client.event
async def on_raw_reaction_remove(payload):
  global temp

  x = client.get_channel(payload.channel_id)

  if payload.user_id == 911163430055063552:

    return

  else:

    if (payload.emoji.name == '☑️'):

      print_statement = 'Desired amount: '+ str(temp) + '?'

      await x.send(print_statement)

      # await x.add_reaction('✅')
      # await x.add_reaction('❌')

    elif (payload.emoji.name == '🔄'):

      temp = 0

    elif (payload.emoji.name == '1️⃣'):

      temp += 1

    elif (payload.emoji.name == '5️⃣'):

      temp += 5

    elif (payload.emoji.name == '🔟'):

      temp += 10

    else:

      return


client.run(TOKEN)