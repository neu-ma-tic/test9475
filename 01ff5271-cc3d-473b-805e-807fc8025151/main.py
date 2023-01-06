import os
import random
from replit import db
import io
import aiohttp
from PIL import Image
import numpy as np
from datetime import datetime, timezone
import discord

I = np.asarray(Image.open('my.png'))
intents = discord.Intents().all()
client = discord.Client(intents=intents)

f = open("PaimonURL.txt", "r")
paimonURLs = f.read().split(", ")

last_callout = datetime.now(timezone.utc)


def get_color(name):
    if name == "black":
        return [0, 0, 0]
    elif name == "white":
        return [255, 255, 255]
    elif name == "red":
        return [255, 0, 0]
    elif name == "green":
        return [0, 255, 0]
    elif name == "blue":
        return [0, 0, 255]
    elif name == "darkblue":
        return [0, 0, 139]
    elif name == "darkred":
        return [139, 0, 0]
    elif name == "darkgreen":
        return [0, 100, 0]
    elif name == "grey":
        return [128, 128, 128]
    else:
        return None


def change_square(x, y, color):
    I[(x * 8) - 4:(x * 8) + 4, (y * 8) - 4:(y * 8) + 4] = color
    img = Image.fromarray(I, 'RGB')
    img.save('my.png')


def preview_change(x, y, color):
    a = np.asarray(Image.open('my.png'))
    a[(x * 8) - 4:(x * 8) + 4, (y * 8) - 4:(y * 8) + 4] = color
    img = Image.fromarray(a, 'RGB')
    img.save('preview.png')


def get_used_words():
    values = db["words_used"]
    sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
    return sorted_values


def add_used_words(message):
    words = db["words_used"]
    for word in message.split():
        if word in list(words.keys()):
            words[word] += 1
        else:
            words[word] = 1
    db["words_used"] = words


def help_page():
    embedVar = discord.Embed(
        title="Commands Prefix = $",
        description="These are all the smoll pp comands for this bot",
        color=0x00ff00)

    embedVar.add_field(
        name="pp",
        value=
        "Uses advanced sensory techniques to tell you your current penis size.",
        inline=False)
    embedVar.add_field(
        name="paimon",
        value=
        "Gives you a paimon from a limited supply. Warning may make you hard",
        inline=False)
    embedVar.add_field(
        name="words",
        value="Prints out the 10 most frequently used words on the server",
        inline=False)
    embedVar.add_field(
        name="show",
        value=
        "Shows you the very good looking art that everyone on this server has made",
        inline=False)
    embedVar.add_field(
        name="place",
        value=
        "Takes in [X coord, Y coord, color] And places a pixel on that location. Note Y is inverted, top is 0 bot is 128. Canvas is 128X128",
        inline=False)
    embedVar.add_field(
        name="preview",
        value=
        "Same as the place command but doesn't actually add the pixel to the real canvas. Use this to find your where you want to draw.",
        inline=False)
    return embedVar


def check_game():
    guild = client.get_guild(777749282236792862)
    longest_time = 0
    biggest_loser = ""
    activity = ""
    loser_member = 0
    memberList = guild.members
    for member in memberList:
        if member.activities:
            if type(member.activities[0]) != discord.activity.CustomActivity:
                now_utc = datetime.now(timezone.utc)
                if type(member.activities[0].start) == datetime:
                    if (now_utc - member.activities[0].start
                        ).total_seconds() > longest_time:
                        longest_time = (
                            now_utc -
                            member.activities[0].start).total_seconds()
                        biggest_loser = member.name
                        activity = member.activities[0].name
                        loser_member = member
    if longest_time > 7200:
        return biggest_loser, longest_time, activity, loser_member
    else:
        return "nobody", 0, "nothing", 0


#def create_profile(author_id):
#db[str(author_id)] = {"money" : 0,
#"slot1" : "",
#"slot2" : "",
#"slot3" : "",
#"slot4" : "",
#"slot5" : "",
#"storage" : []
#}
@client.event
async def on_ready():
    print("we have logged in as{0.user}".format(client))


@client.event
async def on_message(message):
    global last_callout
    if message.author == client.user:
        return

    add_used_words(message.content)

    if (datetime.now(timezone.utc) - last_callout).total_seconds() > 1800:
        L, T, A, M = check_game()

        if L != "nobody":
            last_callout = datetime.now(timezone.utc)
            await message.channel.send(
                f"{L} is a fucking loser. They have been playing {A} for {int(T//3600)} hours {int((T%3600)//60)} minutes and {int((T%60))} seconds"
            )

        if T > 18000:
            await message.channel.send(
                M.mention +
                "seriously this is not ok, please get off and touch some grass"
            )

    #if db[str(message.author.id)] not in db.keys():
    #create_profile(str(message.author.id))

    if message.content.startswith("$pp"):
        if "ricric" in str(message.content) or "@Sagiricric_gaming" in str(
                message.content):
            await message.channel.send("69 inches")
        else:
            await message.channel.send(str(random.randint(0, 10)) + " inches")

    if message.content.startswith("$words"):
        to_print = get_used_words()
        word_amount = len(to_print)
        embedVar = discord.Embed(
            title="Top 10 Most common words",
            description="These are the top 10 most typed words in this server",
            color=0x00ff00)
        for num in range(min(word_amount, 10)):
            embedVar.add_field(
                name=f"No. {num+1}",
                value=
                f"\"{to_print[num][0]}\" has been said {to_print[num][1]} times",
                inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith("$paimon"):
        async with aiohttp.ClientSession() as session:
            async with session.get(paimonURLs[random.randint(
                    0,
                    len(paimonURLs) - 1)]) as resp:
                if resp.status != 200:
                    return await message.channel.send(
                        'Could not download file...')
                data = io.BytesIO(await resp.read())
                await message.channel.send(
                    file=discord.File(data, 'cool_image.png'))

    if message.content.startswith("$help"):
        await message.channel.send(embed=help_page())
    if message.content.startswith("$show"):
        await message.channel.send(file=discord.File('my.png'))
    if message.content.startswith("$preview"):
        params = (message.content).split()
        color_RGB = get_color(params[3])
        if color_RGB == None:
            await message.channel.send(
                "Not a valid color.  Valid colors: black, white, red, darkred, green, darkgreen, blue, darkblue"
            )
        elif int(params[2]) > 128 or int(params[2]) <= 0:
            await message.channel.send(
                "not valid x coordinate must be between 0 and 128")
        elif int(params[1]) > 128 or int(params[1]) <= 0:
            await message.channel.send(
                "not valid y coordinate must be between 0 and 128")
        else:
            preview_change(int(params[2]), int(params[1]), color_RGB)
            await message.channel.send(file=discord.File('preview.png'))
    if message.content.startswith("$place"):
        params = (message.content).split()
        color_RGB = get_color(params[3])
        if color_RGB == None:
            await message.channel.send(
                "Not a valid color.  Valid colors: black, white, red, darkred, green, darkgreen, blue, darkblue"
            )
        elif int(params[2]) > 128 or int(params[2]) <= 0:
            await message.channel.send(
                "not valid x coordinate must be between 0 and 128")
        elif int(params[1]) > 128 or int(params[1]) <= 0:
            await message.channel.send(
                "not valid y coordinate must be between 0 and 128")
        else:
            change_square(int(params[2]), int(params[1]), color_RGB)
            await message.channel.send(file=discord.File('my.png'))


#keep_alive()
client.run(os.getenv("TOKEN"))
