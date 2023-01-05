import os
import discord
import random
import requests
from replit import db
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import asyncio
from keep_alive import keep_alive


def getAPI():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
  'id':'6264'
  }
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '008b681b-36c1-4d8f-8361-1b5b5dc2a549',
  }

  session = Session()
  session.headers.update(headers)
  
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data['data']['6264']['quote']['USD']['price']
    # print(data)
    return price
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

client = discord.Client()

my_secret = os.environ['TOKEN']

async def ch_pr():
  await client.wait_until_ready()
  while not client.is_closed():
    price = getAPI()
    print('----------------------------------')
    print(price)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$'+str(round(price, 6))))
    await asyncio.sleep(180)
  
client.loop.create_task(ch_pr())

@client.event
async def on_ready():
  keys = db.keys()
  # value = list(db["sleep"])
  print(keys)
  # print("sleep= "+str(value[0]))
  print('We have logged in as {0.user}'.format(client))

keep_alive()
client.run(my_secret)