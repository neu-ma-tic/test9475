import discord

TOKEN = "OTM2ODY3OTMwNDY4MTQ3MjUw.YfTcQA.rYRRSBuLSBSrbJy9QnMwU8Yfiy"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
       return

    elif message.content.startswith("tell me a joke") or message.content.startswith("please tell me a joke"):
        await message.channel.send("I'm a bot I can't tell a joke")

client.run(TOKEN)