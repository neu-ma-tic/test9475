import discord
import os
import search_runpee # search class we will impelement later

'''
# If you are coding the bot on a local machine, use the python-dotenv pakcage to get variables stored in .env file of your project
from dotenv import load_dotenv
load_dotenv()
'''

# instantiate discord client 
client = discord.Client()

# discord event to check when the bot is online 
@client.event
async def on_ready():
  print(f'{client.user} is now online!')

# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('ODQxMjMyOTg1MjQ3ODQyMzM0.YJjxRQ.Q0KqZf9m8o-QQJ3vggtqdMVlVqE'))