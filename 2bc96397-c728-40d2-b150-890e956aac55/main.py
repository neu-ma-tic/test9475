import discord
import os
import random
import csv
from keep_awake import keep_awake



client = discord.Client()

profane_words = ["tangina", "tanga", "gago", "bobo", "tang ina", "putangina"]

momma_sermons = ["don't talk like that!",
                "Yo mama didn't teach you that word!",
                 "Shame on you talking like that",
                "You kiss your mama with that mouth?",
                "lessen that type of words child."
                "come on, you're better than that."]


with open ('bible_data_set.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  phrase = [f"{line[4]}\n -{line[1]} {line[2]}:{line[3]}"for line in csv_reader]
    # print(phrase)
  
@client.event
async def on_ready():
  print('I {0.user} is ready to serve.'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg.startswith('$randomphrase'):
    await message.channel.send(random.choice(phrase))
    
  if any(word in msg for word in profane_words):
    await message.channel.send(random.choice(momma_sermons))
    await message.channel.send('\n heres some bible verse for you.')
    await message.channel.send(random.choice(phrase))


keep_awake()
client.run(os.getenv('discordbothash'))
    
  