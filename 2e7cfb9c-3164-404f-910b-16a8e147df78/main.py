import discord
import re
import json
from os import getenv
from ping_self import ping_self


client = discord.Client()


class bot: # functions ordered by dependancies
  def json_to_dict(self, file_name):
    file = open(file_name, 'r')
    raw_object = json.load(file)
    file.close()
    del file
    return dict(raw_object)
  
  def __init__(self):
    settings = self.json_to_dict("settings.json") # reading files every call is wasteful
    self.prefix = str(settings["defaults"]["prefix"])
    self.jokes_saturation = 0
    self.jokes_active = bool(settings["jokes"]["active"])
    self.jokes_cost = int(settings["jokes"]["cost"])
    self.jokes_limit = int(settings["jokes"]["limit"])
    del settings

    self.command = re.compile("^" + self.prefix + "[\w]+") # so is compiling regexes
    self.joke_1 = re.compile("^(I|i)('){0,1}m [\w]+(.){0,1}$")
    self.joke_2 = re.compile("[\w]+er(.){0,1}$")
  
  def reply(self, string, message):
    message.channel.send("```" + string + "```")
  
  async def play_playlist(self, message, playlist): # todo
    pass

  def attempt_command(self, message): # todo
    match = self.command.match(message.content)
    command = match.match[1,-1] # cuts out the /
    del match

    if (command == 'add' or command == 'a'):
      self.reply("I can't do this right now.", message)
      pass
    elif (command == 'create' or command == 'c'):
      self.reply("I can't do this right now.", message)
      pass
    elif (command == 'help' or command == 'h'):
      self.reply("Here's the full list of commands I use:\n+ add <song> to <playlist>\n+ create <playlist>\n+ help\n+ help_advanced\n+ play <playlist> (using <prefix>)\n+ rename <playlist old name> <playlist new name>\n+ settings <setting> <value>\n+ stop\nview <playlist>\n\nMost commands can be abbreviated to 1 or 2 letters\nType /help_advanced for in-depth information on each command.", message)
    elif (command == 'help_advanced' or command == 'ha'):
      self.reply("Here's in-depth information on all of my commands:\n+ add <song> to <playlistlist>\n     Adds a song to a playlist. If the song contains the word 'to', put it in apostrophes or quotation marks.\n+ create <playlist>\n     Creates a new empty playlist called <playlist>. <playlist> can only be 1 word.\n+ help\n     Shows a list of commands.\n+ help_advanced\n     Provides in-depth information on each command.\n+ play <playlist> (using <prefix>)\n     Starts playing the playlist <playlist> in the voicechat of whoever typed the command, using the prefix provided. If no prefix is provided, defaults to '-'. Can be used in multipule places at once.\n+ rename <playlist old name> <playlist new name>\n     Renames the playlist <playlist old name> to <playlist new name>\n+ settings <setting> <value>\n     Sets <setting> to <value>.\n+ stop\n     stops playing all music.\n+ view <playlist>\n   shows all the songs in <playlist>. If no <playlist> is provided, will show a list of playlists. Typing /view settings will show all settings.", message)
    elif (command == 'play' or command == 'p'):
      self.reply("I can't do this right now.", message)
      pass
    elif (command == 'rename' or command == "r"):
      self.reply("I can't do this right now.", message)
      pass
    elif (command == 'settings'):
      self.reply("I can't do this right now.", message)
      pass
    elif (command == 'stop' or command == 's'):
      self.reply("I can't do this right now.", message)
      pass
    elif (command == 'view' or command == 'v'):
      self.reply("I can't do this right now.", message)
      pass
    else:
      self.reply("Sorry, but I don't know the command '" + command + "'. Type /help for a full list of commands, or /help_advanced for an in-depth list.", message)

  def attempt_jokes(self, message):
    if (self.joke_1.match(message.content) != None): # dad joke #1: hi i'm dad
      name = message.content[4:-1]
      if (name.endswith(".")): name = name[0:-2] # cuts out the period
      self.reply("Hi " + name + ", I\'m Dad!", message)
      self.jokes_saturation += self.jokes_cost
      del name
      pass
    match = self.joke_2.match(message.content) # dad joke #2: i hardly know her
    if match != None:
      verb = match.match[0,-3]
      if (match.match.endswith('.')): verb = verb[0,-2]
      self.reply(verb + " er? I hardly know er!", message)
      self.jokes_saturation += self.jokes_cost
      del verb, match
      pass
    del match

  def respond_to_message(self, message):
    if (message.content.startswith(self.prefix)):
      self.attempt_command(message)
    elif (self.jokes_active == True):
      if (self.jokes_saturation <= self.jokes_limit*self.jokes_cost):
        self.attempt_jokes(message)
      else:
        self.jokes_saturation -= 1


gary_jr = bot()


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  gary_jr.respond_to_message(message)

client.run(getenv("TOKEN"))