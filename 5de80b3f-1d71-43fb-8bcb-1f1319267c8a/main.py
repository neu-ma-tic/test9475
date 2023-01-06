import discord
import os
import random
import requests
import json
import time

client = discord.Client()

leList = [
    "https://www.youtube.com/watch?v=pzYepqSPgLY",
    "https://www.youtube.com/watch?v=eQwBAfJXz7Y",
    "https://www.youtube.com/watch?v=kdm-c9ba82c"
]


def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    jsonData = json.loads(response.text)
    quote = jsonData[0]["q"] + " -" + jsonData[0]["a"]
    return quote


def getJoke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    jsonData = json.loads(response.text)
    joke = jsonData[0]["setup"] + jsonData[0]["punchline"]
    return joke


def getAge(name):
    webUrl = "https://api.agify.io?name=" + name
    response = requests.get(webUrl)
    jsonData = json.loads(response.text)
    age = jsonData["age"]
    return age


def getActivity():
    response = requests.get("https://www.boredapi.com/api/activity")
    jsonData = json.loads(response.text)
    activity = jsonData["activity"]
    return activity


def getMeme():
    response = requests.get("https://api.imgflip.com/get_memes")
    jsonData = json.loads(response.text)
    memeNumber = random.randint(0, 100)
    meme = jsonData["data"]["memes"][memeNumber]["url"]
    return meme


def getHoliday(date):
    response = requests.get(
        "https://date.nager.at/api/v2/publicholidays/2020/US")

    jsonData = json.loads(response.text)

    for day in jsonData:
        index = jsonData.index(day)
        if date == jsonData[index]["date"]:
            holiday = jsonData[index]["name"]
            return holiday

    return ("That is not a Holiday :(")


def encrypt(stuff, num):
    newStuff = ""
    for letter in stuff:
        number = ord(letter) + num
        newStuff += chr(number)
    return newStuff


def decrypt(stuff, num):
    newStuff = ""
    for letter in stuff:
        number = ord(letter) - num
        newStuff += chr(number)
    return newStuff

def getMusic(song):
  response = requests.get()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith("!caraVideo"):
        await msg.channel.send("https://www.youtube.com/watch?v=i82528KGDdo")
    elif msg.content.startswith("!caraGif"):
        await msg.channel.send(
            "https://www.verdict.co.uk/wp-content/uploads/2017/09/giphy-downsized-large.gif"
        )
    elif msg.content.startswith("!caraList"):
        await msg.channel.send(random.choice(leList))
    elif msg.content.startswith("!caraInspire"):
        quote = getQuote()
        await msg.channel.send(quote)
    elif msg.content.startswith("!caraJoke"):
        joke = getJoke()
        x = joke.split("?")
        await msg.channel.send(x[0] + "?")
        time.sleep(1)
        await msg.channel.send(x[1])
    elif msg.content.startswith("!caraAGE"):
        message = msg.content
        name = message[10:]
        print(name)
        age = getAge(name)
        await msg.channel.send(age)
    elif msg.content.startswith("!caraBored"):
        activity = getActivity()
        await msg.channel.send(activity)
    elif msg.content.startswith("!caraMeme"):
        meme = getMeme()
        await msg.channel.send(meme)
    elif msg.content.startswith("!caraHoliday"):
        length = len("!caraHoliday")
        date = msg.content[length:]
        stats = getHoliday(date)
        await msg.channel.send(stats)
    elif msg.content.startswith("!caraEncrypt"):
        length = len("!caraEncrypt")
        
        check = msg.content[length + 1:length + 2]
        digit = check.isnumeric()

        if digit == True:
          number = msg.content[length:length + 2]
          word = msg.content[length + 2:]
          check = msg.content[length + 2:length + 3]
          digit = check.isnumeric()
          if digit == True:
            word = msg.content[length + 3:]
            number = msg.content[length:length + 3]
            check = msg.content[length + 3:length + 4]
            digit = check.isnumeric()
            if digit == True:
              word = msg.content[length + 4:]
              number = msg.content[length:length + 4]
        else:
          number = msg.content[length:length + 1]
          word = msg.content[length + 1:]
        
        new = encrypt(word, int(number))
        await msg.channel.send(new)

    elif msg.content.startswith("!caraDecrypt"):
        length = len("!caraDecrypt")

        check = msg.content[length + 1:length + 2]
        digit = check.isnumeric()

        if digit == True:
          word = msg.content[length + 2:]
          number = msg.content[length:length + 2]

          check = msg.content[length + 2:length + 3]
          digit = check.isnumeric()
          if digit == True:
            word = msg.content[length + 3:]
            number = msg.content[length:length + 3]

            check = msg.content[length + 3:length + 4]
            digit = check.isnumeric()
            if digit == True:
              word = msg.content[length + 4:]
              number = msg.content[length:length + 4]
        else:
          number = msg.content[length:length + 1]
          word = msg.content[length + 1:]
        
        new = decrypt(word, int(number))
        await msg.channel.send(new)
    elif msg.content.startswith("!caraMusic"):
        length = len("!caraMusic")
        song = msg.content[length:]
        music = getMusic(song)
        await msg.channel.send(music)
    elif msg.content.startswith("!caraHelp"):
        await msg.channel.send(
            "Commands: !cara, !caraVideo, !caraGif, !caraList, !caraInspire, !caraJoke, !caraAGE[name], !caraBored, !caraMeme, !caraHoliday####-##-##, !caraEncrypt##message, !caraDecrypt##message You don't get to know what any of them do"
        )
    elif msg.content.startswith("!cara"):
        await msg.channel.send("Look my bot works")


client.run(os.getenv('TOKEN'))
