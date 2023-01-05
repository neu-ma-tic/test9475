import discord
import os


intents = discord.Intents.default() 
intents.members = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_raw_reaction_add(payload):
  ourMessageID = 911413055672451073

  if ourMessageID == payload.message_id:
    member = payload.member
    guild = member.guild

    emoji = payload.emoji.name
    print (emoji)
    if emoji == 'acmDev':
      role = discord.utils.get(member.guild.roles, id=901637431437189161)
      #dev
      await member.add_roles(role)
    elif emoji == 'acmAlgo':
      role = discord.utils.get(member.guild.roles, id =901637335542792263)
      #algo
      await member.add_roles(role)
    elif emoji == 'acmCreate':
      role = discord.utils.get(member.guild.roles, id =901637294245683201)
      #create
      await member.add_roles(role)
    else :
      channel = client.get_channel(901636979144413214)
      await channel.send("Please use an emoji corresponding to a proper ACM role")


      
client.run(os.getenv('acmBot'))
#Alejandro Ramos email: alejandroramosh27@csu.fullerton.edu

#Sreevidya Sreekantham  email: srvidya@csu.fullerton.edu

#Himani Tawade (himani.tawade@csu.fullerton.edu)
#AkshayaK
#AkshayaR@csu.fullerton.edu

#Ricardo Granados (ricardog2002@csu.fullerton.edu)

#Joel Anil John (joel.aniljohn@csu.fullerton.edu)

#Mohamed Habarneh (MohamedHabarneh@csu.fullerton.edu)