#Importing
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
import datetime

#Defining Client
Client = discord.Client()
client = commands.Bot(command_prefix = "/")
chat_filter = []
bypass_list = ["422891607239688202"]

#What to say right as it starts
@client.event
async def on_ready():
    print("Bot is Ready")

#embed
@client.command()
async def embeder():
  embed = discord.Embed(
    title= "Title",
    description = "This is a description",
    colour = discord.Colour.green()
  )

  embed.set_footer(text="This is a footer")
  embed.set_image(url="https://cdn.discordapp.com/avatars/135157153408221184/89de5ae59b12aad67aaa098749292b30.png")
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/135157153408221184/89de5ae59b12aad67aaa098749292b30.png")
  embed.set_author(name="Atomization",icon_url="https://cdn.discordapp.com/avatars/135157153408221184/89de5ae59b12aad67aaa098749292b30.png")
  embed.add_field(name="Field Name", value="Field Value", inline=False)
  embed.add_field(name="Field Name", value="Field Value", inline=True)
  embed.add_field(name="Field Name", value="Field Value", inline=True)

  await client.say(embed=embed)

#What happens when user messages something
@client.event
async def on_message(message):

  
  #Check if message is a command
  await client.process_commands(message)
  #Chat filter
  contents = message.content.split(" ")
  for word in contents:
    if word.upper() in chat_filter:
      for i in bypass_list:
        if not i in (role.id for role in message.author.roles):

          try:
            await client.delete_message(message)
            await client.send_message(message.channel, "**HEY!** You can't say that")
          
          except discord.errors.NotFound:
            return



  #If prefix is !PING return Pong
  if message.content.upper().startswith("!PING"):
    userID = message.author.id
    await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  #If Prefix is !SAY check user ID
  if message.content.upper().startswith("!SAY"):
    try:
      args = message.content.split(" ")
      await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    except discord.errors.HTTPException:
      return

  
    
  #Check if You are Owner
  if message.content.upper().startswith("!ADMIN"):
    if "422891607239688202" in (role.id for role in message.author.roles):
      await client.send_message(message.channel, "You are an Owner")
    
    else:
      await client.send_message(message.channel, "You are not an Owner")

@client.event
async def on_member_join(member):
  joindate = discord.utils.snowflake_time(member.id)
  if joindate == "2018-04-01 05:29:08.377000":
    client.add_roles(member.id, "445073056701087766")
  print(joindate)
  
  
  #role = discord.utils.get(member.server.roles, name="Member")
  #await client.add_roles(member,role)


#Real way of doing commands    
@client.command()
async def test():
  await client.say("Sup")

#Args is considered list
@client.command()
async def echo(*args):
  output = ""
  for i in args:
    output += i
    output += " "
  await client.say(output)

#Purging
@client.command(pass_context=True)

async def clear(ctx, amount=100):
  try:
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
      messages.append(message)
    await client.delete_messages(messages)
    await client.say("Deleted" + amount + "Messages")

  except ClientException:
    await client.say("You can only bulk delete messages that are under 14 days old!")

#embed
@client.command()
async def embeder():
  embed = discord.Embed(
    title= "Title",
    description = "This is a description",
    colour = discord.Colour.green()
  )

  embed.set_footer(text="This is a footer")
  embed.set_image(url=https://cdn.discordapp.com/avatars/135157153408221184/89de5ae59b12aad67aaa098749292b30.png)
  embed.set_thumbnail(url=https://cdn.discordapp.com/avatars/135157153408221184/89de5ae59b12aad67aaa098749292b30.png)
  embed.set_author(name="Atomization",icon_url=https://cdn.discordapp.com/avatars/135157153408221184/89de5ae59b12aad67aaa098749292b30.png)
  embed.add_field(name="Field Name", value="Field Value", inline=False)
  embed.add_field(name="Field Name", value="Field Value", inline=True)
  embed.add_field(name="Field Name", value="Field Value", inline=True)

  await client.say(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
  channel = reaction.message.channel
  await client.send_message(channel, "{} has added {} to the message: {}".format(user.name,reaction.emoji,reaction.message.content))

@client.event
async def on_reaction_remove(reaction,user):
  channel = reaction.message.channel
  await client.send_message(channel, "{} has removed {} from the message: {}".format(user.name,reaction.emoji,reaction.message.content))


    


#Run Bot
client.run("NTQxMTI3NDIwNjIzOTc4NTA2.Dzp-cw.rX0yL0W0pEzMD-gyeTP_FEQaiRc")

