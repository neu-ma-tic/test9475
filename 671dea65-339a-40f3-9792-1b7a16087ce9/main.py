import os
import discord
import asyncio
import random
# import json
# from discord.ext import commands

#Number_emojis = ["\N{KEYCAP DIGIT ONE}"]
#YesNo_emojis = ["\N{THUMBS UP SIGN}"]
YesNo_emojis = ['\U0001F44D', '\U0001F44E'] #'\U0000270C']
one23_emojis = ['1\ufe0f\u20e3', '2\ufe0f\u20e3', '3\ufe0f\u20e3']
Qs_lib = {'Q1': ['As one of the members in the assigned team, what are you supposed to do?',
 {'A1': 'A1: Relo to a building as needed',
  'A2': "A2: Join the team leader's rally asap",
  'A3': "A3: Solo attack some building whenever possible"}, 1],
  'Q2': ['When you are getting zeroed by only one attacker, what are you supposed to do?',
  {'A1': 'A1: Relo away',
   'A2': 'A2: Send away troops',
   'A3': 'A3: Make sure to have enough troops to defend'}, 2]}

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

async def on_message(message):
  if message.author == client.user:
      return
  chan = message.channel 

  if message.content.startswith("$hello"):
    await chan.send('Hello! This is MojiBot!')

  # if message.content.startswith('$start_training'):
  #   await chan.send("This is for RR training. Let's begin!")
  #   num_q = len(Qs_lib)
  #   num_corr = 0
  #   num_inco = 0
  #   await chan.send("Threre will be {} questions before finish the training. Good Luck!".format(num_q))
  #   shuffled_list = random.shuffle(list(range(num_q)))
  #   for num in shuffled_list:
  #     q = 'Q'+str(num)
  #     await chan.send('Question {}:'.format(q[1]))
  #     await chan.send(Qs_lib[q][0])
  #     for key in Qs_lib[q][1]:
  #       await chan.send(Qs_lib[q][1][key])
  #     for emoji in one23_emojis:
  #       await chan.last_message.add_reaction(emoji)
  #     def check(reaction, user):
  #       return user == message.author #and reaction.emoji == YesNo_emojis[Qs_lib['Q1'][2]]
  #     try:
  #       reaction,user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
  #     except asyncio.TimeoutError:
  #       await chan.send('Time Out! You failed the test!')
  #     else:
  #       if reaction.emoji == YesNo_emojis[Qs_lib[q][2]]:
  #         await chan.send('Correct!')
  #         num_corr += 1
  #       else:
  #         correct_ans = 'A'+ str(Qs_lib[q][2]+1)
  #         await chan.send('Incorrect! The answer is: ' + Qs_lib[q][1][correct_ans][4:])
  #         num_inco += 1
  #   await chan.send("That's all! You answered correctly {} times!".format(num_corr))

  if message.content.startswith('$help'):
    await chan.send("The available commands are: $hello, $start_training.")

@client.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    print(reaction.emoji == YesNo_emojis[0])

client.run(os.getenv('TOKEN'))

