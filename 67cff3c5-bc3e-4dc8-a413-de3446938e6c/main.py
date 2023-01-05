#import the main libraries
import discord
import os
import time

#declare what the client is (the bot is the client)
client = discord.Client()


@client.event
#when the bot has loaded all the functions and has updated etc then this will start
async def on_ready():
    print("I'm in")
    #prints the bots
    print(client.user)


@client.event
#this finds when any message is sent within the server
async def on_message(message):

    #makes sure the person that the bot is replying to is not itself
    if message.author != client.user:
        messageBody = (message.content).lower()

        if messageBody == "!exercise cardio":
            userAtt = message.author.mention
            await message.channel.send(
                userAtt +
                "\nJumprope (3 min)\nCooldown (30 sec)\nBurpees (3 min)\nCooldown (30 sec)\nJumping-jacks (3 min)\nCooldown (30 sec)\nPlankhold (3 min)\nCooldown (1 min)\nJog (5 min 30sec)\nTimer: "
            )

        if messageBody.startswith("!calories male"):
            userAtt = message.author.mention
            mass = float(messageBody[15:17])
            height = float(messageBody[18:21])
            age = float(messageBody[22:])
            totalCals = (13.75 * mass) + (5.003 * height) - (
                6.755 * age) + 66.47
            await message.channel.send(
                userAtt +
                "** Assuming you put your gender, then mass (kg), then height (cm), then age, your maintenance intake is: {:.2f}"
                .format(totalCals) + " cals**")

        if messageBody.startswith("!calories female"):
            userAtt = message.author.mention
            mass = float(messageBody[17:19])
            height = float(messageBody[20:23])
            age = float(messageBody[24:])
            totalCals = (9.563 * mass) + (1.85 * height) - (
                4.676 * age) + 655.1
            await message.channel.send(
                userAtt +
                "** Assuming you put your gender, then mass (kg), then height (cm), then age, your maintenance intake is: {:.2f}"
                .format(totalCals) + " cals**")


#get the private token from the .env file
token = os.environ.get("DISCORD_BOT_SECRET")
#run the stuff on the private token location or somthing????(0<0)NIcE
client.run('OTE1NTMxNTg4MjExNzMyNTAx.Yac9PA.ruujPyK1jeBsaxkqhWwWp0mB5yM')
