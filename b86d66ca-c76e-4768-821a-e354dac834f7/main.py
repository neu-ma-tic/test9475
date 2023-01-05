import os
import discord
my_secret = os.environ['TOKEN']
import requests
import json
import random


client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing, so sad"]

starter_encouragements = [
    "Cheer up!",
    "Don't kill yourself",
    "Maybe send it, who cares"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)
# get_quote()

@client.event
async def on_ready():
    print('The end is near {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # msg = message.content

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run(my_secret)