from discord.ext import commands
from twilio.rest import Client
import time
import os

bot = commands.Bot(command_prefix='$')

@bot.command(name='hello')
async def said_hello(message):

  await message.channel.send("Bye Bitch")
  time.sleep(2)
  await message.author.kick(reason="get outta here")

@bot.command(name='text')
async def txt(ctx, phone_number, text_message):

  await ctx.send('sending...')

  phone_client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_TOKEN'))

  message = phone_client.messages.create(
    messaging_service_sid='MG0013813c6edebb9e57fd430bea749441',
    body=text_message,
    to='+1'+phone_number
)
  
bot.run(os.getenv('TOKEN'))