import discord
import requests
import json
from googletrans import Translator

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = str(json_data[0]['q'] + " -" + json_data[0]['a'])
    translator = Translator()
    result = translator.translate(quote, src='en', dest='ru')
    return result


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)


client.run(('OTEwOTU0ODQyMjkyMzcxNDY2.YZaWzw.W1lrtUQiJjzFaZ6C3V8vtNG5RFY'))