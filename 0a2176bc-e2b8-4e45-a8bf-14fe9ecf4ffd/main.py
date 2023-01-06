# import statements
import os
import discord
import search




#instantiate EcoWikiWeb class from search
Eco_Data_Search = search.EcoDataSearch
#Eco_Wiki_Web = search.EcoWikiWeb()


#variables
my_secret = os.environ['Token']
client = discord.Client()




#discord event to check when the bot is online
@client.event
async def on_ready():
  print(f'{client.user} is now online!')

#no result message
no_result_message = '''Sorry, we can\'t find what you are searching for.'''

#teach the bot to recognize commands
@client.event
async def on_message(message):
  #make sure bot doesn't respond to it's own messages to avoid infinite loop 
  if message.author == client.user:
    return

  #lower case the message
  
  message_content = message.content.lower()
  #message_content = message_string.capitalize()
  #print(message_content)
  #user_message = message_content

  if message.content.startswith(f'$hello'):
    await message.channel.send('''Hello there! I\'m the bot for Eco. 
    Sorry but I really need to go to the bathroom... Please read my manual by typing $help or $commands while I'm away.''')

  if f'search' in message_content:
   
    key_words = Eco_Data_Search.key_words(message_content)
    result_data = Eco_Data_Search.search(key_words)

    await message.channel.send(result_data)
    #links = Eco_Wiki_Web.send_link(result_links, search_words)

    #if len(links) > 0:
      #for link in links:
        #await message.channel.send(no_result_message)

client.run(my_secret)