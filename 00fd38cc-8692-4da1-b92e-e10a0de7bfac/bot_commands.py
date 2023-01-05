import discord
import youtube_dl
import os
import asyncio
import urllib.parse, urllib.request, re
from discord.ext import commands
from discord import FFmpegPCMAudio
import time

counter = 0
music_queue = []
queue_titles = []

#--------------------------------------------------------------------
# Command: !hello
# returns: "Hello, I'm Bleep Bloop! What can i do for you?"
#--------------------------------------------------------------------
async def hello(ctx):
  await ctx.send("Hello, I'm Bleep Bloop! What can i do for you?")


#--------------------------------------------------------------------
# Command: !commands
# returns: list of commands
#--------------------------------------------------------------------
async def commands(ctx):
  await ctx.send("List of commands:\n!hello")


#--------------------------------------------------------------------
# - Whenever a user joins the voice channel, the bot greets that user
#
# - Whenever the voice channel gets empty, the bot eliminates all the 
#   messages that he has sent and the commands sent by the user
#--------------------------------------------------------------------
async def on_voice_state_update(member, before, after, client):

  global counter
  global music_queue
  global queue_titles
  
  text_channel = client.get_channel(348584941568917505)

  if not before.channel and after.channel:
    counter += 1
    
    if member.display_name != "Bleep Bloop": 
      await text_channel.send('Welcome Back {}! To show the list of commands type !commands' .format(member.display_name))
      return
  
  elif not after.channel:
    print(counter)

    voice_channel = client.get_channel(348584941568917506)

    counter -=1

    members = voice_channel.members #finds members connected to the channel

    for member in members:
      if member.name == "Bleep Bloop":
        if counter == 1:
          music_queue = []
          queue_titles = []
          await member.move_to(None)
        
    if counter == 0:
      await text_channel.send('All users have left the voice channel.')

      async for message in text_channel.history(limit=200):
        if message.author.id == client.user.id or message.content.startswith("!"):
           await message.delete()


#--------------------------------------------------------------------
# Command: !join
# returns: the bot joins the voice channel, that the user that has 
#          called him is in
#--------------------------------------------------------------------
async def join(ctx, client):

  voice_state = ctx.author.voice
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  if voice_state != None: # Só faz join se o user estiver connectado a um                             voice channel
    if voice == None:
      voice_channel = ctx.author.voice.channel
      print(voice_channel)
      await voice_channel.connect()
  
  else:
    await ctx.send("You need to be in a voice channel to use this command")


#--------------------------------------------------------------------
# Command: !leave
# returns: the bot leaves the voice channel
#--------------------------------------------------------------------
async def leave(ctx, client):
  global music_queue
  global queue_titles
  voice_state = ctx.author.voice
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

  if voice_state != None:  # Só faz leave se o user estiver connectado a um                            voice channel
    if voice != None:
      music_queue = []
      queue_titles = []
      await ctx.voice_client.disconnect()
  else:
    await ctx.send("You need to be in a voice channel to use this command.")


#--------------------------------------------------------------------
# Command: !play
# returns: If the bot is not currently playing anything, he will play the music #          that the user has requested. 
#          Else he queues the music.
#--------------------------------------------------------------------
async def play(ctx, name, client):
    global msucic_queue
    global queue_titles
    
    voice_state = ctx.author.voice

    if voice_state == None: # Só faz join se o user estiver connectado a um                             voice channel
      await ctx.send("You need to be in a voice channel to use this command.")
      return
    
    voice_channel = ctx.author.voice.channel
    voice = ctx.guild.voice_client
    
    if voice == None:
      await voice_channel.connect()

    voice = ctx.guild.voice_client

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    YDL_OPTIONS = {'format': "bestaudio"}

    query_string = urllib.parse.urlencode({'search_query': name})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' +                                         query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
 
    ydl = youtube_dl.YoutubeDL(YDL_OPTIONS)
    info = ydl.extract_info(search_results[0], download=False)
    
    for key, value in info.items() :
      if key == 'title':
        queue_titles.append(value)
        break


  
    url2 = info['formats'][0]['url']
    source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

    if not voice.is_playing():
      player = voice.play(source, after=lambda x=None: check_queue(ctx, client))
      title = queue_titles.pop(0)
      await ctx.send("Currently playing: **{}**" .format(title))

    else:
      music_queue.append(source)
      await ctx.send("Added to queue **{}**" .format(value))

def check_queue(ctx, client):
  global music_queue

  if music_queue != []:
    voice = ctx.guild.voice_client
    channel = client.get_channel(348584941568917505)
    
    source = music_queue.pop(0)
    title = queue_titles.pop(0)
    client.loop.create_task(channel.send("Currently playing: **{}**" .format(title)))
    player = voice.play(source, after=lambda x=None: check_queue(ctx, client))


#--------------------------------------------------------------------
# Command: !pause
# returns: the bot pauses the music that was playing
#--------------------------------------------------------------------
async def pause(ctx, client):

  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  voice.pause()
  await ctx.send("Paused")

#--------------------------------------------------------------------
# Command: !queue
# returns: the bot shows the musics in the queue
#--------------------------------------------------------------------
async def queue(ctx):
  global queue_titles
  i = 1
  text = "Current queue:\n"

  if queue_titles == []:
    await ctx.send("There are no songs in queue")
    return

  for song in queue_titles:
    text = text + ("{} - **{}**\n"  .format(i, song))
    i += 1
  await ctx.send(text)


#--------------------------------------------------------------------
# Command: !stop
# returns: the bot stops the current song and clears the queue
#--------------------------------------------------------------------
async def stop(ctx):
  global music_queue
  global queue_titles

  music_queue = []
  queue_titles = []

  if ctx.guild.voice_client.is_playing(): 
    ctx.voice_client.stop()


#--------------------------------------------------------------------
# Command: !skip
# returns: the bot skips the current song and plays the next in queue
#--------------------------------------------------------------------
async def skip(ctx, client):
  global music_queue
  global queue_titles

  if music_queue != []:

    voice = ctx.guild.voice_client

    voice.pause()

    channel = client.get_channel(348584941568917505)
    
    source = music_queue.pop(0)
    title = queue_titles.pop(0)
    client.loop.create_task(channel.send("Currently playing: **{}**" .format(title)))
    player = voice.play(source, after=lambda x=None: check_queue(ctx, client))
  
  else:
    ctx.voice_client.stop()