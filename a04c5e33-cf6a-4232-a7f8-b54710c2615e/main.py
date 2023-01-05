import os
import discord
from webserver import keep_alive
from discord.ext import commands, tasks
import requests
import json
import random
import youtube_dl
import DiscordUtils
from operator import pos
from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands import cooldown
import os
from asyncio import sleep
from discord.ext.commands.cooldowns import BucketType
from datetime import datetime, timedelta, date, time
from datetime import *
import random
import asyncpraw
import pytz 
from pytz import timezone
import asyncio
import math 
import sympy
from sympy import *
from discord.ext import commands
from discord.ext import tasks



bot = commands.Bot(command_prefix='.')
client = discord.Client()
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="Nara's Mom"))
  print("The bot is ready")

#Date time week

english_weekday = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
now_utc = datetime.now(timezone('UTC'))
now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
todays = now_Jakarta.now()
weekdays = now_Jakarta.weekday()
weekdays = int(weekdays)
today = english_weekday[weekdays]


@bot.command()
async def day(ctx):
  english_weekday = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  today = english_weekday[weekdays]
  await ctx.send(f'Today is {today}') 

@bot.command()
async def date(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = str(now_utc.astimezone(timezone('Asia/Jakarta')))
  split = (now_Jakarta.split())
  result = split[0].split(".")
  await ctx.send(result[0]) 

@bot.command(name = "time")
async def timenow(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = str(now_utc.astimezone(timezone('Asia/Jakarta')))
  split = (now_Jakarta.split())
  result = split[1].split(".")
  await ctx.send(f"It is {result[0]}")
  
#Time for

@bot.command()
async def timefor(ctx,location):
  now_utc = datetime.now(timezone('UTC'))
  if location.lower() == "useast":
    now_useast = str(now_utc.astimezone(timezone('US/Eastern')))
    result = (now_useast.split("."))
    await ctx.send(result[0])
  elif location.lower() == "uswest":
    now_uswest = str(now_utc.astimezone(timezone('US/Pacific')))
    result = (now_uswest.split("."))
    await ctx.send(result[0])
  elif location.lower() == "eueast":
    now_eueast = str(now_utc.astimezone(timezone('Europe/Moscow')))
    result = (now_eueast.split("."))
    await ctx.send(result[0])
  elif location.lower() == "euwest":
    now_euwest = str(now_utc.astimezone(timezone('Europe/Paris')))
    result = (now_euwest.split("."))
    await ctx.send(result[0])
  elif location.lower() == "africa":
    now_africa = str(now_utc.astimezone(timezone('Africa/Johannesburg')))
    result = (now_africa.split("."))
    await ctx.send(result[0])
  elif location.lower() == "dubai":
    now_dubai = str(now_utc.astimezone(timezone('Asia/Dubai')))
    result = (now_dubai.split("."))
    await ctx.send(result[0])
  else:
    await ctx.send("Unsupported timezone")


#Time in 

@bot.command()
async def timein(ctx,timeneeded,timetype):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  timeneeded = int(timeneeded)
  if timetype.lower() == "s":
    calculated_time = str(now_Jakarta + timedelta(seconds = timeneeded))
    split = (calculated_time.split())
    result = split[1].split(".")
    await ctx.send(result[0])
  elif timetype.lower() == "m":
    calculated_time = str(now_Jakarta + timedelta(minutes = timeneeded))
    split = (calculated_time.split())
    result = split[1].split(".")
    await ctx.send(result[0])
  elif timetype.lower() == "h":
    days = 0
    while timeneeded >= 24:
        days += 1
        timeneeded -= 24
    calculated_time = str(now_Jakarta + timedelta(hours = timeneeded))
    split = (calculated_time.split())
    result = split[1].split(".")
    if days == 0:
      await ctx.send(result[0])
    else:
      await ctx.send(f'{result[0]} +{days}d')
  elif timetype.lower() == "d":
    calculated_time = str(now_Jakarta + timedelta(days = timeneeded))
    split = (calculated_time.split())
    result = split[0].split(".")
    await ctx.send(result[0])
  else: 
    await ctx.send("Invalid input only accept (d = Days, h = Hours, m = Minutes, s = Seconds)")

#Timedif

@bot.command()
async def timedif(ctx,hours,minutes):
  hours = int(hours)
  minutes = int(minutes)
  total = hours * 60 + minutes
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  totalnow = now_Jakarta.hour * 60 + now_Jakarta.minute
  difference = total - totalnow
  h = 0
  if difference == 0:
    await ctx.send(f"It is currently {hours}:{minutes}")
  elif difference < 0:
    difference = (total + 1440) - totalnow
    while difference >= 60:
      h += 1
      difference -= 60
    if difference == 0:
      await ctx.send(f"It is {h}  away from {hours}:{minutes}")
    elif h == 0:
      await ctx.send(f"It is {difference} minutes away from {hours}:{minutes}")
    else:
      await ctx.send(f"It is {h} hours and {difference} minutes away from {hours}:{minutes}")
  else:
    while difference >= 60:
      h += 1
      difference -= 60
    if difference == 0:
      await ctx.send(f"It is {h}  away from {hours}:{minutes}")
    elif h == 0:
      await ctx.send(f"It is {difference} minutes away from {hours}:{minutes}")
    else:
      await ctx.send(f"It is {h} hours and {difference} minutes away from {hours}:{minutes}")
  
#Convertjkt

@bot.command()
async def convertjkt(ctx,hour,minute,location):
  hour = int(hour)
  minute = int(minute)
  h = 0
  if location.lower() == "dubai":
    hour -= 3
    while hour < 0:
      h += 1
      hour += 1 
    if h != 0:
      await ctx.send(f"Its {h}:{minute} in Dubai")
    else:
      await ctx.send(f"Its {hour}:{minute} in Dubai")
  elif location.lower() == "useast":
    hour -= 12
    while hour < 0:
      h += 1
      hour += 1 
    if h != 0:
      await ctx.send(f"Its {h}:{minute} in US East")
    else:
      await ctx.send(f"Its {hour}:{minute} in US East")
  elif location.lower() == "aueast":
    hour += 3
    while hour > 24:
      h += 1
      hour -= 1
    if h != 0:
      await ctx.send(f"Its {h}:{minute} in Au East")
    else:
      await ctx.send(f"Its {hour}:{minute} in Au East")
  else:
    await ctx.send("Unsupported time zone")

#Holidays

@bot.command()
async def christmas(ctx):
  difference =  359 - int(datetime.now().timetuple().tm_yday)
  if difference == 0:
    await ctx.send("It is Christmas! :D")
  elif difference < 0: 
    ago = str(difference).replace("-", "")
    difference = 724 - int(datetime.now().timetuple().tm_yday)
    await ctx.send(f"Christmas was {ago} days ago, the next one will be in {difference} days! :D")
  else:
    await ctx.send(f"It is {difference} days till christmas! :D")
  

@bot.command()
async def halloween(ctx):
  difference =  304 - int(datetime.now().timetuple().tm_yday)
  if difference == 0:
    await ctx.send("It is Halloween! :D")
  elif difference < 0: 
    ago = str(difference).replace("-", "")
    difference = 669 - int(datetime.now().timetuple().tm_yday)
    await ctx.send(f"Halloween was {ago} days ago, the next one will be in {difference} days! :D")
  else:
    await ctx.send(f"It is {difference} days till Halloween! :D")
     

@bot.command()
async def newyears(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  difference =  365 - int(datetime.now().timetuple().tm_yday)
  if difference == 0:
    await ctx.send(f"It is New Year's Eve of {now_Jakarta.year + 1}! :D")
  else:
    await ctx.send(f"It is {difference} days till New Year's Eve of {now_Jakarta.year + 1}! :D")

#Reminder

@bot.command()
async def remindin(ctx,timeneeded,timetype,*,message = None):
  timeneeded = int(timeneeded)
  if timetype.lower() == "m":
    await asyncio.sleep(timeneeded*60)
    user = ctx.author
    await user.send(f'Reminder: {message}')
  elif timetype.lower() == "h":
    await asyncio.sleep(timeneeded*3600)
    user = ctx.author
    await user.send(f'Reminder: {message}')
  elif timetype.lower() == "s":
    await asyncio.sleep(timeneeded)
    user = ctx.author
    await user.send(f'Reminder: {message}')
  elif timetype.lower() == "d":
    await asyncio.sleep(timeneeded*86400)
    user = ctx.author
    await user.send(f'Reminder: {message}')
  else: 
    await ctx.send("Invalid input only accept (D = Days, H = Hours, M = Minutes, S = Seconds)")

@bot.command()
async def remindat(ctx,hours,minutes,*,message = None):
  hours = int(hours)
  minutes = int(minutes)
  total = hours * 60 + minutes
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  totalnow = now_Jakarta.hour * 60 + now_Jakarta.minute
  timeneeded = (total - totalnow) * 60
  user = ctx.author
  if timeneeded == 0:
    await ctx.send(f"It is currently {hours}:{minutes}")
  elif timeneeded < 0:
    await ctx.send("Time specified has already elapsed!")
  else:
    await asyncio.sleep(timeneeded)
    await user.send(f"Reminder: {message}")

#Currency

@bot.command()
async def idr(ctx, amount, currency):
  amount = float(amount)
  if currency.lower() == "aed":
    amount *= 3900
    await ctx.send(f"That is Rp. {amount}")
  elif currency.lower() == "usd":
    amount *= 14300
    await ctx.send(f"That is Rp. {amount}")
  else:
    await ctx.send("Unsupported currency")


#Math 

@bot.command()
async def log(ctx,argument,base):
  argument = float(argument)
  base = float(base)
  result = math.log(argument,base)
  await ctx.send(result)

@bot.command()
async def expandbi(ctx,co1,co2,power):
  x, y = sympy.symbols("x y")
  co1 = int(co1)
  co2 = int(co2)
  power = int(power)
  formula = (co1*x + co2*y) ** power
  result = str(formula.expand()).replace("**", "^")
  await ctx.send(result)

@bot.command()
async def factorquad(ctx,a,b,c):
  x, y = sympy.symbols("x y")
  a = int(a)
  b = int(b)
  c = int(c)
  formula = (a*x**2 + b*x + c)
  result = str(formula.factor()).replace("**", "^")
  await ctx.send(result)

@bot.command()
async def expandquad(ctx,co1,a,co2,b):
  x = sympy.symbols("x")
  co1 = int(co1)
  a = int(a)
  co2 = int(co2)
  b = int(b)
  formula = (co1*x+a)*(co2*x+b)
  result = str(formula.expand()).replace("**", "^")
  await ctx.send(result)

@bot.command()
async def convertangle(ctx,value,unit):
  value = int(value)
  if unit.lower() == "rad":
    await ctx.send(f"That is {value * 57.2958} deg")
  elif unit.lower() == "deg":
    await ctx.send(f"That is {value / 57.2958} rad")
  else:
    await ctx.send("Invalid unit: deg or rad")

@bot.command()
async def trig(ctx,ratio,value):
  value = int(value)
  if ratio.lower() == "sin":
    await ctx.send(f"{math.sin(value)} rad")
  elif ratio.lower() == "cos":
    await ctx.send(f"{math.cos(value)} rad")
  elif ratio.lower() == "tan":
    await ctx.send(f"{math.tan(value)} rad")
  else:
    await ctx.send("Invalid ratio: sin or cos or tan")


#Gr.10 Timetable

Monday_10a = '7:30 Prep, 7:40 ENG, 9:10 BI/CHINESE, 10:40 INS, 12:50 Math'
Tuesday_10a = '7:30 Prep, 7:40 ENG, 9:10 SSS, 10:40 PHE/Design/Art, 12:50 Science, 14:15 PP'
Wednesday_10a = '7:40 assembly, 9:10 BI, 10:40 Math, 12:50 INS'
Thursday_10a = '7:30 Prep, 7:40 Religion, 9:10 ENG, 10:40 PPKN, 12:50 Advisory'
Friday_10a = '7:40 Maths, 9:10 Sience, 10:40 PHE/Design/Art'


Monday_10e = '7:30 Prep, 7:40 INS, 9:10 BI, 10:40 ENG, 12:50 PP'
Tuesday_10e = '7:30 Prep, 7:40 INS, 9:10 SSS, 10:40 Science, 12:50 Math, 14:15 ENG'
Wednesday_10e = '7:40 Assembly, 9:10 BI, 10:40 PHE/Design/Art, 12:50 Math'
Thursday_10e = '7:30 Prep, 7:40 Religion, 9:10 ENG, 10:40 PPKN, 12:50 Advisory'
Friday_10e = '7:40 PHE/Design/Art, 9:10 Math, 10:40 Science'


Monday_10c = ['7:30 Prep', '7:40 ENG', '9:10 INS', '10:40 BI', '12:50 Math']
Tuesday_10c = ['7:30 Prep', '7:40 ENG', '9:10 SSS', '10:40 Design/PHE/Art', '12:50 Science', '14:15 BI']
Wednesday_10c = ['7:40 School Assembly', '8:00 Assembly', '9:10 ENG', '10:40 Math', '12:50 PP']
Thursday_10c = ['7:30 Prep', '7:40 Religion', '9:10 INS', '10:40 PPKN', '12:50 Advisory']
Friday_10c = ['7:40 Math', '9:10 Science', '10:40 Design/PHE']


Monday_10b = '7:30 Prep, 7:40 ENG, 9:10 PP, 10:40 BI, 12:50 INS, 13:10 I&S'
Tuesday_10b = '7:30 Prep, 7:40 ENG, 9:10 SSS, 10:40 Science, 12:50 Math, 14:15 BI/Chinese'
Wednesday_10b= '7:40 Asssembly, 9:10 I&S, 10:40 PHE/Design/Art, 12:50 Math'
Thursday_10b = '7:30 Prep, 7:40 Religion, 9:10 ENG, 10:40 PPKN, 12:50 Advisory'
Friday_10b = '7:40 PHE/Design/Art, 9:10 Math, 10:40 Science'


Monday_10d = '7:30 Prep, 8:00 Math, 9:10 BI, 10:40 ENG, 12:50 INS'
Tuesday_10d = '7:30 Prep, 8:00 Science, 9:10 SSS, 10:40 ENG, 12:50 Math, 14:15 INS'
Wednesday_10d = '7:40 Assembly, 9:10 BI, 10:40 PHE/Design/Art, 12:50 Science'
Thursday_10d = '7:30 Prep, 7:40 Religion, 9:10 Math, 10:40 PPKN, 12:50 Advisory'
Friday_10d = '7:40 PHE/Design/Art, 9:10 ENG, 10:40 Math'


@bot.command()
async def timetable10a(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  if weekdays == 0:
    await ctx.send(Monday_10a)
  elif weekdays == 1:
    await ctx.send(Tuesday_10a)
  elif weekdays == 2:
    await ctx.send(Wednesday_10a)
  elif weekdays == 3:
    await ctx.send(Thursday_10a)
  elif weekdays == 4:
    await ctx.send(Friday_10a)
  else:
    await ctx.send("No school today")

@bot.command()
async def timetable10b(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  if weekdays == 0:
    await ctx.send(Monday_10b)
  elif weekdays == 1:
    await ctx.send(Tuesday_10b)
  elif weekdays == 2:
    await ctx.send(Wednesday_10b)
  elif weekdays == 3:
    await ctx.send(Thursday_10b)
  elif weekdays == 4:
    await ctx.send(Friday_10b)
  else:
    await ctx.send("No school today")

@bot.command()
async def timetable10c(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  if weekdays == 0:
    await ctx.send(' '.join(Monday_10c))
  elif weekdays == 1:
    await ctx.send(' '.join(Tuesday_10c))
  elif weekdays == 2:
    await ctx.send(' '.join(Wednesday_10c))
  elif weekdays == 3:
    await ctx.send(' '.join(Thursday_10c))
  elif weekdays == 4:
    await ctx.send(' '.join(Friday_10c))
  else:
    await ctx.send("No school today")

@bot.command()
async def tmrw10c(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  weekdays += weekdays
  if weekdays == 0:
    await ctx.send(' '.join(Monday_10c))
  elif weekdays == 1:
    await ctx.send(' '.join(Tuesday_10c))
  elif weekdays == 2:
    await ctx.send(' '.join(Wednesday_10c))
  elif weekdays == 3:
    await ctx.send(' '.join(Thursday_10c))
  elif weekdays == 4:
    await ctx.send(' '.join(Friday_10c))
  else:
    await ctx.send("No school today")

@bot.command(name = "10c")
async def tenc(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  if weekdays == 0:
    await ctx.send(Monday_10c)
  elif weekdays == 1:
    await ctx.send(Tuesday_10c)
  elif weekdays == 2:
    await ctx.send(Wednesday_10c)
  elif weekdays == 3:
    await ctx.send(Thursday_10c)
  elif weekdays == 4:
    await ctx.send(Friday_10c)
  else:
    await ctx.send("No school today")

@bot.command()
async def timetable10d(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  if weekdays == 0:
    await ctx.send(Monday_10d)
  elif weekdays == 1:
    await ctx.send(Tuesday_10d)
  elif weekdays == 2:
    await ctx.send(Wednesday_10d)
  elif weekdays == 3:
    await ctx.send(Thursday_10d)
  elif weekdays == 4:
    await ctx.send(Friday_10d)
  else:
    await ctx.send("No school today")

@bot.command()
async def timetable10e(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = (now_utc.astimezone(timezone('Asia/Jakarta')))
  weekdays = now_Jakarta.weekday()
  weekdays = int(weekdays)
  if weekdays == 0:
    await ctx.send(Monday_10e)
  elif weekdays == 1:
    await ctx.send(Tuesday_10e)
  elif weekdays == 2:
    await ctx.send(Wednesday_10e)
  elif weekdays == 3:
    await ctx.send(Thursday_10e)
  elif weekdays == 4:
    await ctx.send(Friday_10e)
  else:
    await ctx.send("No school today")


@bot.command()
async def lunchtime(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = now_utc.astimezone(timezone('Asia/Jakarta'))
  weekday = now_Jakarta.weekday()
  if weekday >= 5:
    await ctx.send("No school today")
  elif weekday == 4:
    await ctx.send("No lunch time on Fridays")
  else:
    total = now_Jakarta.hour * 60 + now_Jakarta.minute
    difference = 720 - total
    h = 0
    while difference >= 60:
      h += 1
      difference -= 60
    if 720 <= total < 770:
      await ctx.send("It is lunch time (12:00 - 12:50)")
    elif total >= 770:
      await ctx.send("Lunch time has passed")
    elif difference == 0:
      await ctx.send(f"It is {h} hours away from lunch time")
    elif h == 0:
      await ctx.send(f"It is {difference} minutes away from lunch time")
    else:
      await ctx.send(f"It is {h} hours and {difference} minutes away from lunch time")

@bot.command()
async def dismissal(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = now_utc.astimezone(timezone('Asia/Jakarta'))
  weekday = now_Jakarta.weekday()
  total = now_Jakarta.hour * 60 + now_Jakarta.minute
  if weekday >= 5:
    schoolend = -1
  elif weekday == 1:
    schoolend = 935
  elif weekday == 4:
    schoolend = 690
  else:
    schoolend = 850
  if schoolend == -1:
    await ctx.send("No school today")
  else:
    difference = schoolend - total
    h = 0
    while difference >= 60:
      h += 1
      difference -= 60
    if total >= schoolend:
      await ctx.send("School has ended")
    elif difference == 0:
      await ctx.send(f"It is {h} hours away from dismissal")
    elif h == 0:
      await ctx.send(f"It is {difference} minutes away from dismissal")
    else:
      await ctx.send(f"It is {h} hours and {difference} minutes away from dismissal")

@bot.command()
async def session10c(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = now_utc.astimezone(timezone('Asia/Jakarta'))
  weekday = now_Jakarta.weekday()
  total = now_Jakarta.hour * 60 + now_Jakarta.minute
  if weekday == 0:
    if 460 <= total <= 540:
      await ctx.send(Monday_10c[1])
    elif 550 <= total <= 630:
      await ctx.send(Monday_10c[2])
    elif 640 <= total <= 710:
      await ctx.send(Monday_10c[3])
    elif 770 <= total <= 850:
      await ctx.send(Monday_10c[4])
    else:
      await ctx.send('No class currently')
  elif weekday == 1:
    if 460 <= total <= 540:
      await ctx.send(Tuesday_10c[1])
    elif 550 <= total <= 630:
      await ctx.send(Tuesday_10c[2])
    elif 640 <= total <= 710:
      await ctx.send(Tuesday_10c[3])
    elif 770 <= total <= 850:
      await ctx.send(Tuesday_10c[4])
    elif 855 <= total <= 935:
      await ctx.send(Tuesday_10c[5])
    else:
      await ctx.send('No class currently')
  elif weekday == 2:
    if 460 <= total <= 540:
      await ctx.send(Wednesday_10c[0])
    elif 550 <= total <= 630:
      await ctx.send(Wednesday_10c[2])
    elif 640 <= total <= 710:
      await ctx.send(Wednesday_10c[3])
    elif 770 <= total <= 850:
      await ctx.send(Wednesday_10c[4])
    else:
      await ctx.send('No class currently')
  elif weekday == 3:
    if 460 <= total <= 540:
      await ctx.send(Thursday_10c[1])
    elif 550 <= total <= 630:
      await ctx.send(Thursday_10c[2])
    elif 640 <= total <= 710:
      await ctx.send(Thursday_10c[3])
    elif 770 <= total <= 850:
      await ctx.send(Thursday_10c[4])
    else:
      await ctx.send('No class currently')
  elif weekday == 4:
    if 460 <= total <= 530:
      await ctx.send(Friday_10c[0])
    elif 540 <= total <= 610:
      await ctx.send(Friday_10c[1])
    elif 620 <= total <= 720:
      await ctx.send(Friday_10c[2])
    else:
      await ctx.send('No class currently')
  else:
    await ctx.send('No school today')

@bot.command()
async def nextsession10c(ctx):
  now_utc = datetime.now(timezone('UTC'))
  now_Jakarta = now_utc.astimezone(timezone('Asia/Jakarta'))
  weekday = now_Jakarta.weekday()
  total = now_Jakarta.hour * 60 + now_Jakarta.minute
  if weekday == 0: 
    if total < 460:
      await ctx.send(f'First is {Monday_10c[1]}')
    elif total < 550:
      await ctx.send(f'Next is {Monday_10c[2]}') 
    elif total < 640:
      await ctx.send(f'Next is {Monday_10c[3]}') 
    elif total < 770:
      await ctx.send(f'Next is {Monday_10c[4]}') 
    elif total < 855:
      await ctx.send(f'Last is {Monday_10c[4]}') 
    else:
      await ctx.send('No classes left')
  elif weekday == 1:
    if total < 460:
      await ctx.send(f'First is {Tuesday_10c[1]}')
    elif total < 550:
      await ctx.send(f'Next is {Tuesday_10c[2]}') 
    elif total < 640:
      await ctx.send(f'Next is {Tuesday_10c[3]}') 
    elif total < 770:
      await ctx.send(f'Next is {Tuesday_10c[4]}') 
    elif total < 855:
      await ctx.send(f'Next is {Tuesday_10c[5]}') 
    elif total < 935:
      await ctx.send(f'Last is {Tuesday_10c[5]}')
    else:
      await ctx.send('No classes left')
  elif weekday == 2: 
    if total < 460:
      await ctx.send(f'First is {Wednesday_10c[0]}')
    elif total < 550:
      await ctx.send(f'Next is {Wednesday_10c[2]}') 
    elif total < 640:
      await ctx.send(f'Next is {Wednesday_10c[3]}') 
    elif total < 770:
      await ctx.send(f'Next is {Wednesday_10c[4]}') 
    elif total < 855:
      await ctx.send(f'Last is {Wednesday_10c[4]}') 
    else:
      await ctx.send('No classes left')
  elif weekday == 3: 
    if total < 460:
      await ctx.send(f'First is {Thursday_10c[1]}')
    elif total < 550:
      await ctx.send(f'Next is {Thursday_10c[2]}') 
    elif total < 640:
      await ctx.send(f'Next is {Thursday_10c[3]}') 
    elif total < 770:
      await ctx.send(f'Next is {Thursday_10c[4]}') 
    elif total < 855:
      await ctx.send(f'Last is {Thursday_10c[4]}') 
    else:
      await ctx.send('No classes left')
  elif weekday == 4:
    if total < 460:
      await ctx.send(f'First is {Friday_10c[0]}')
    if total < 540:
      await ctx.send(f'Next is {Friday_10c[1]}')
    elif total < 620:
      await ctx.send(f'Next is {Friday_10c[2]}')
    elif total < 720:
      await ctx.send(f'Last is {Friday_10c[2]}')
    else:
      await ctx.send('No classes left')
  else:
    await ctx.send('No school today')




#Misc

greetings = ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy"]

  
positive = ["Its ok to be sad","Dont be sad, I am a bot","Just hang in there","Be the change you want to see in the world"]

#Music

music = DiscordUtils.Music()

@bot.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, bettersearch=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, bettersearch=True)
        await ctx.send(f"Queued {song.name}")

@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()
  
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)

@bot.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")
  
@bot.command()
async def remove(ctx,index):
  player = music.get_player(guild_id = ctx.guild.id)
  song = await player.remove_from_queue(int(index))
  await ctx.send(f'Removed {song.name} from queue')

@bot.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@bot.command()
async def loop(ctx):
  player = music.get_player(guild_id = ctx.guild.id)
  song = await player.toggle_song_loop()
  if song.is_looping:
    return await ctx.send("Song is looping")


#Reddit 

secret = os.environ["secret"]



reddit = asyncpraw.Reddit(client_id = "-3y279VMw_4TilYj41sFow",
client_secret = secret,
user_agent = "python_reddit"
)


@bot.command()
async def liminal(ctx):
    subreddit = await reddit.subreddit("Liminalspace")
    submission = await subreddit.random()
    await ctx.send(submission.url)

    
@bot.command()
async def meme(ctx):
    subreddit = await reddit.subreddit("memes")
    submission = await subreddit.random()
    await ctx.send(submission.url)


@bot.command()
async def iwannacry(ctx):
    subreddit = await reddit.subreddit("TwoSentenceSadness")
    submission = await subreddit.random()
    await ctx.send(submission.title)
    await ctx.send(submission.selftext)

@bot.command()
async def backrooms(ctx):
    subreddit = await reddit.subreddit("Backrooms")
    submission = await subreddit.random()
    await ctx.send(submission.url)

@bot.command()
async def scary(ctx):
    subreddit = await reddit.subreddit("TwoSentenceHorror")
    submission = await subreddit.random()
    await ctx.send(submission.title)
    await ctx.send(submission.selftext)

@bot.command()
async def food(ctx):
    subreddit = await reddit.subreddit("food")
    submission = await subreddit.random()
    await ctx.send(submission.url)

@bot.command()
async def funfact(ctx):
    subreddit = await reddit.subreddit("todayilearned")
    submission = await subreddit.random()
    await ctx.send(submission.title)
    await ctx.send(submission.selftext)
    await ctx.send(submission.url)
    

def get_cat():
  response_cat = requests.get("https://api.thecatapi.com/v1/images/search")
  cats = response_cat.json()
  cat1 = cats[0]["url"]
  return cat1

#api
#def get_quote():
  #response1 = requests.get#("https://zenquotes.io/api/random")
  #quotes = response1.json()
  #quote = quotes[0]["q"]
  #return quote

def get_fox():
  responses = requests.get ("https://randomfox.ca/floof/")
  foxes = responses.json()
  fox1 = foxes["image"]   
  return fox1


def get_dog():
  response_dog = requests.get("https://dog.ceo/api/breeds/image/random")
  dogs = response_dog.json()
  dog1 = dogs["message"]
  return dog1


def get_joke():
  response_joke = requests.get ("https://official-joke-api.appspot.com/random_joke")
  jokes = response_joke.json()
  return jokes["setup"] ,jokes["punchline"] 


response = requests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/Jakarta")
dateandtime = response.json()

@bot.command()
async def users(ctx):
  id = bot.get_guild(706877473694023740)
  await ctx.send(f'There are currently {id.member_count} members')


@bot.command()
async def grape(ctx):
  await ctx.send("https://ichef.bbci.co.uk/images/ic/704xn/p06svql1.jpg")


@bot.command()
async def ping(ctx):
  await ctx.reply(str(round(bot.latency*1000))+"ms")



imsad = ["At least you can unmute", "At least you didn't get banned by a bot","At least you arent a bot","At least your not bald"]


@bot.command(name = "/")
async def divide(ctx, num1:int ,num2:int):
  await ctx.reply(round(num1/num2))
  

@bot.command()
async def canyouunmute(ctx):
  for i in range(3):
    await ctx.send("I CANT UNMUTE")
    i += 1

@bot.command(name = "*")
async def multiply(ctx, num1:int ,num2:int):
  await ctx.reply(round(num1*num2))



@bot.command(name = "-")
async def minus(ctx, num1:int ,num2:int):
  await ctx.reply(round(num1-num2))

@bot.command()
async def goodnight(ctx):
  if dateandtime["hour"]  > 0 :
    await ctx.reply(f'Its Early, Goodluck sleeping at {dateandtime["time"]} <3')
  else:
    await ctx.reply(f'Goodnight, sweet dreams <3')


@bot.command(name = "bye")
async def bye(ctx):
  await ctx.reply("bye bye handsome", tts=True)

@bot.command()
async def hello(ctx):
  x = random.randint(0,100)
  if x == 1:
    await ctx.reply(f'Hello Bossman {ctx.author.name}')
  else:
    await ctx.reply(f'{random.choice(greetings)} {ctx.author.name}')

#quotes
#@bot.command()
#async def quote(ctx):
  #quotes = get_quote()
  #await ctx.reply(quotes)






#Command_Who

@bot.command()
async def warn(ctx,user:discord.Member,*,message ="Im gonna take over the world one day and you arent invited :)"):
  if user.id == 438676735257608197:
    await user.send(f'{ctx.author} warned you at  {dateandtime["date"]} {dateandtime["time"]}')
    await ctx.send(f'You cannot warn the creator, He has been notified')
  else:
    await user.send(message)
    await ctx.send(f'{user.name} has been warned')


@bot.command()
async def ban(ctx, user:discord.Member,*, reason=None):
  role = discord.utils.get(ctx.guild.roles, name="bot manager")
  if role in ctx.author.roles:
    await user.ban(reason = reason)
    await ctx.reply (f'{user.name} has been banned')
  else:
    await ctx.reply (f'Role is Invalid')


@bot.command(name='unban')
async def unban(ctx, id: int):
  role = discord.utils.get(ctx.guild.roles, name="bot manager")
  if role in ctx.author.roles:
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.reply(f'User{user.name} has been unbanned')
  else:
    await ctx.reply(f'Role is Invalid')





@bot.command()
async def kick(ctx, user:discord.Member,*,reason=None):
  role = discord.utils.get(ctx.guild.roles, name="bot manager")
  if role in ctx.author.roles:
    await user.kick(reason=reason)
    await ctx.reply (f'{user.name} has been kicked')
  else:
    await ctx.reply (f'Role error (Invalid)')



  

@bot.command()
async def test(ctx):
  if ctx.author.id == 438676735257608197:
    await ctx.reply(f'Hello Owner')
  else:
    await ctx.reply("You do not have permission")




@bot.command()
async def who(ctx):
  await ctx.reply(f'My name is Nara, I am going to take over the world one day')
  

@bot.command()
async def add(ctx,num1:int, num2:int):
    await ctx.reply(num1+num2)

@bot.command()
async def sad(ctx):
  await ctx.reply(random.choice(imsad))


@bot.command()
async def fox(ctx):
  foxes = get_fox()
  await ctx.reply(foxes)

@bot.command()
async def dog(ctx):
  dogies = get_dog()
  await ctx.reply(dogies)

@bot.command()
async def cat(ctx):
  caties = get_cat()
  await ctx.reply(caties)


@bot.command()
async def joke(ctx):
  jokies = get_joke()
  await ctx.reply(jokies)



@bot.command()
async def depressed(ctx):
  x = random.randint(0,100)
  if x == 1 or x == 2 or x == 3:
    await ctx.reply("Dont be sad, when I take over the world there will be no more happiness for everyone :)")
  else:
    await ctx.reply(random.choice(positive))

#2/september
    
#4/sep economy bot



    
@bot.command()
async def send(ctx, member:discord.Member,amount,):
    amount = int(amount)
    await open_account(member)
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    if users[str(user.id)]["wallet"] <= 0:
        await ctx.send(f'Transaction has been cancelled due to insufficient funds')
        return

    await ctx.send(f"Are you sure you want to continute with this transaction? (yes/no)")
    msg = await bot.wait_for("message",check = lambda message: message.author == ctx.author\
    and message.channel == ctx.channel)
    if msg.content.lower() ==  "yes":
        users[str(member.id)]["wallet"] += amount
        users[str(user.id)]["wallet"] -= amount
        await ctx.send(f"{user.name} has sent {amount} to {member.name}")

        with open("bank.json", "w") as f:
            users = json.dump(users, f)



@bot.command()
async def bal(ctx, member:discord.Member = None):
    if not member:
        member = ctx.author
    await open_account(member)


    user = member
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{member.name}'s balance",color=discord.Color.dark_red())
    em.add_field(name="Wallet Balance", value=f'{wallet_amt}')
    em.add_field(name="Bank Balance", value=f'{bank_amt}')
    await ctx.send(embed = em)

@bot.command()
@cooldown(1,600,BucketType.user)
async def beg(ctx):
    x = random.randrange(1,200)
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    if x == 100:
        earnings = random.randrange(250,1000)
        await ctx.send(f'{user.name.upper()} JUST GOT A RARE COIN 🥳🥳🥳')
    else:
        earnings = random.randrange(130)

    await ctx.send(f'Someone gave you {earnings} coins')
    await ctx.send(f'{user.name} is now on a 10 minute cooldown')


    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", "w") as f:
        users = json.dump(users, f)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        users = json.dump(users, f)
    return True

async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users











@bot.command()
async def flip(ctx,amount):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    amount = int(amount)
    x = random.randint(1,3)
    if users[str(user.id)]["wallet"] < amount:
        await ctx.send(f"You dont have enough money to flip ${amount}")
        return
    if int(amount) < 0:
        await ctx.send(f"You dont have enough money to flip ${amount}")
        return
    if users[str(user.id)]["wallet"] < 0:
        await ctx.send("You dont have enough money in your balance")
        return
    if x == 1:
        users[str(user.id)]["wallet"] += amount
        await ctx.send(f"{user.name} has won the coin flip and made ${amount}")
    else:
        await ctx.send(f"{user.name} has lost the coin flip and lost ${amount}")
        users[str(user.id)]["wallet"] -= amount
    with open("bank.json", "w") as f:
        users = json.dump(users, f)



@bot.command()
@cooldown(1,60*5,BucketType.user)
async def rob(ctx,member:discord.Member):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    choices = ["success","fail"]
    x = random.choice(choices)
    robbed_amount = random.randrange(150)
    if member.name == user.name:
        await ctx.send(f'You cannot rob yourself, you just gave yourself a  5 mins cooldown :D')
        return
    if users[str(user.id)]["wallet"] <= 0:
        await ctx.send("You dont have enough money")
        return
    

    
    
    if users[str(member.id)]["wallet"] <= 0:
        await ctx.send(f"You cannot rob {member.name} he doesnt have anything :(")
    else:
        if x == "success":
            users[str(member.id)]["wallet"] -= robbed_amount
            users[str(user.id)]["wallet"] += robbed_amount
            
            await ctx.send(f'{member.name} got robbed by {ctx.author.name} for {robbed_amount}$ ')
        else:
            users[str(user.id)]["wallet"] -= robbed_amount
            users[str(member.id)]["wallet"] += robbed_amount
            await ctx.send(f'{ctx.author.name} was caught robbing by {member.name} and lost {robbed_amount}$ ')
        
    await ctx.send(f"{user.name} is now on a 5 minute cooldown")
    with open("bank.json", "w") as f:
        users = json.dump(users, f)




keep_alive()
TOKEN = os.environ['TOKEN']

bot.run(TOKEN)


