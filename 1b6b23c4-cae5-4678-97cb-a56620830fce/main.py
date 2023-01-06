from discord.ext import commands
from random import randrange

TOKEN = 'OTMwODQ4MDc2Mjg4MTE0NzE5.Yd710w.kYQtG12MrKQLFMBnt4WXlF4WsPo'

client = commands.Bot(command_prefix='.')
insultos=["muerto hambre","duchate puerco","comprate un amigo"]


@client.event
async def on_ready():
    print(f'todo listo nene')
    print(insultos)

@client.command(pass_context=True)
async def vete(ctx):
    if (ctx.voice_client):
      await ctx.guild.voice_client.disconnect()
    else:
      await ctx.send('menudo tontaco')

@client.command(pass_context=True)
async def add(ctx,*,insulto):
  print(insulto)
  insultos.append(insulto)

@client.event
async def on_message(message):
    #username = str(message.author).split('#')[0]
    user_message = str(message.content)
    #channel = str(message.channel.name)
    userid=message.author.id


    #andres 347510526307205125
    #yo 271676691879821312
    #ojedih 336867240978939905

    if(user_message[0]!='.'):
      if(userid==833723510462873621):
        print(insultos)
        await message.channel.send(insultos[randrange(len(insultos))])

client.run(TOKEN)
