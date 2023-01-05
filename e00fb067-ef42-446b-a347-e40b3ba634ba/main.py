import discord
import os
import requests
import json
import random
import time
from keep_alive import keep_alive

client = discord.Client()
url = "https://meme-api.herokuapp.com/gimme"

sexuality_list = ['straight', 'lesbian', 'gay', 'pansexual', 'super-straight', 'polysexual', 'asexual', 'autosexual', 'bisexual', 'bicurious', 'aromantic', 'biromantic']

connors_list = ['gay', 'bisexual', 'pansexual']

responses = ['sus', 'interesting', 'hmmmmmmmm']

with open("sus.txt", "r") as f:
  banned_words = f.readlines()

with open("gaycount.txt", "r") as f:
  data = f.readlines()
  gay_count = data[0]

with open("gaycount2.txt", "r") as f:
  data = f.readlines()
  gay_count2 = data[0]

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  global url
  global gay_count
  global gay_count2

  gay_count = int(gay_count)
  gay_count2 = int(gay_count2)

  if message.author == client.user:
    return

  if message.content.startswith("$hi"):
    await message.channel.send("Hello!")

  if message.content.startswith('$dildo'):
    for i in range(0, 100):
      await message.channel.send('pls buy pink phallic object')
      time.sleep(5)

  if message.content.startswith("$sexuality"):
    success = False
    content = message.content
    content = content.split(' ')
    try:
      name = content[1]
      success = True
    except:
      success = False
    a = str(message.author)
    a = a.split('#')
    if str(message.author) == 'WatermanAllureFountainPen#1059':
      sexuality = random.choice(connors_list)
    elif str(message.author) == 'Noah Palmer#4153':
      sexuality = 'gay (for connor)'
    else:
        sexuality = random.choice(sexuality_list)

    if success:
      user = name
    else:
      user = a[0]
      
    await message.channel.send('{} your sexuality is {}'.format(user, sexuality))

  if message.content.startswith("$meme"):
    r = requests.get(url)
    database = json.loads(r.text)
    await message.channel.send(database["title"])
    await message.channel.send(database["url"])

  if message.content.startswith("$simp"):
    success = False
    content = message.content
    content = content.split(' ')
    try:
      name = content[1]
      success = True
    except:
      success = False
    rand = random.randint(0, 100)
    a = str(message.author)
    a = a.split('#')
    if str(message.author) == 'Noah Palmer#4153':
      rand = 1000
    if str(message.author) == 'BigBoyBorris#9818':
      rand = 1000
    if success:
      user = name
    else:
      user = a[0]
    await message.channel.send("{} your simp level is {}%".format(user, rand))
    if rand >= 90:
      await message.channel.send("https://i.redd.it/wa70zfigrsl41.jpg")

  if message.content.startswith("$test"):
    pass

  if "hoya" in message.content.lower():
    amount = random.randrange(1, 40)
    await message.channel.send("HOY{}".format('A' * amount))

  if str(message.author) == "WatermanAllureFountainPen#1059":
    for word in banned_words:
      word = word.rstrip()
      if word.lower() in message.content:
        gay_count += 1
        with open("gaycount.txt", "w") as f:
          f.write(str(gay_count))
        await message.channel.send(random.choice(responses))

  if str(message.author) == "ars0n_fire#1199":
    for word in banned_words:
      word = word.rstrip()
      if word.lower() in message.content:
        gay_count2 += 1
        with open("gaycount2.txt", "w") as f:
          f.write(str(gay_count2))
        await message.channel.send(random.choice(responses))

  if message.content.startswith("$count"):
    await message.channel.send("Connor has said sus words %d times since 22/06/2021" % gay_count)
    await message.channel.send("Reece has said sus words %d times since 23/06/2021" % gay_count2)

keep_alive()
token = os.environ['TOKEN']
client.run(token)