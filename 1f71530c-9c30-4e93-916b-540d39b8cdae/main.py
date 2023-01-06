# bot.py
import os

import discord
from discord.ext import tasks
#from dotenv import load_dotenv'
#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
import datetime
import calendar

GENERAL = 675577165906968601
VOICETEXT = 692844663639638036
MSG_CHANNEL = GENERAL
WEEKDAY_TO_SEND_MESSAGE = 0  # Monday

client = discord.Client(intents=discord.Intents.default())


def get_last_fridays(year):
  last_fridays = []
  for month in range(1, 13):
    last_friday_day_number = max(
      week[calendar.FRIDAY] for week in (calendar.monthcalendar(year, month)))
    last_friday = datetime.date(year, month, last_friday_day_number)
    last_fridays.append(last_friday)
  return last_fridays


def get_next_friday(from_date):
  weekday = from_date.weekday()
  # Add a number of days as needed
  days_to_add = 4 - weekday
  # If the current day is Saturday or Sunday then this will be a
  # negative number. We need to wrap around
  days_to_add %= 7
  return from_date + datetime.timedelta(days=days_to_add)


def is_time_for_msg():
  today = datetime.datetime.today()
  print("The current day is", today)
  print("And the weekday is", today.weekday())
  # Find out if the next Friday is the last Friday of the month
  next_friday = get_next_friday(today)
  last_fridays = get_last_fridays(today.year)
  if next_friday.date() in last_fridays:
    # If so, we should call it out if it's the right day of the week
    if today.weekday() == WEEKDAY_TO_SEND_MESSAGE:
      return True
  else:
    print("The next Friday is", next_friday)
    print("The list of last Fridays is", last_fridays)
  return False


@client.event
async def on_ready():
  guild = discord.utils.get(client.guilds, name=GUILD)
  print(f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')
  send_message.start()


@tasks.loop(hours=24)
async def send_message():
  channel = client.get_channel(MSG_CHANNEL)
  if is_time_for_msg():
    msg = "ℹ️ This Friday is the last Friday of the month."
    await channel.send(msg)
    print("Sent message")
  else:
    print("Did not send a message, it's not the right time.")


client.run(TOKEN)
