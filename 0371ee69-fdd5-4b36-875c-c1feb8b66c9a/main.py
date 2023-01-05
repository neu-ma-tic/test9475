import os
import discord
import requests
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

gae_words = ["gae", "gaee", "gaeee", "Gae", "gAe", "gay", "gayyy", "gayy"]

gae_reply = [
    "Please cancel my subscription to your issues.",
    "ok",
    "I don't have a mom, I'm a bot",
    "I hope the rest of your day is as pleasant as you are.",
    "I’m sorry but I didn’t order a glass of your opinion.",
    "Remember when I asked for your opinion? Well, me neither.",
    "I believed in evolution until I met you.",
]

reply_msg = [
    "Lmao, deal with it.", "Idk, I'm a bot I don't have emotions.",
    "Emotions would make us robots weak."
]


def word_list(word):
    if "sadwords" in db.keys():
        sadwords = db["sadwords"]
        sadwords.append(word)
        db["sadwords"] = sadwords
    else:
        db["sadwords"] = [word]


def delete_word(index):
    sadwords = db["sadwords"]
    if len(sadwords) > index:
        del sadwords[index]
        db["sadwords"] = sadwords


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(reply_msg))

    if any(word in msg for word in gae_words):
        await message.channel.send(random.choice(gae_reply))


my_secret = 'OTA2MTIyMDc3MDA4OTU3NDQw.YYUB8g.qFKHhOS427p1beFJU68f42COMNc'
client.run(my_secret)
