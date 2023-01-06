import discord
import os

client = discord.Client()

def spam():
  while True:
    pyautogui.typewrite("fuck you")
    pyautogui.press("enter")

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'
        .format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if(message.content.startswith("s hello")):
    await message.channel.send("Hello dickhead.")
  if(message.content.startswith("s ayon")):
    await message.channel.send("gay nigga ayon likes to suck dicks in the shower.")
  if(message.content.startswith("s shattiq")):
    await message.channel.send("Sexiest Man of The Year.")
  if(message.content.startswith("s amir")):
    await message.channel.send("Would you sit on the cake and eat the dick or sit on the dick and eat the cake? Amir would sit on the dick and eat another dick.")
  if(message.content.startswith("s spam")):
    while True:
      pyautogui.typewrite("fuck you")
      pyautogui.press("enter")

if(message.content.startswith("s ayon")):
    await message.channel.send("gay nigga ayon likes to suck dicks in the shower.")
client.run(os.getenv('token'))