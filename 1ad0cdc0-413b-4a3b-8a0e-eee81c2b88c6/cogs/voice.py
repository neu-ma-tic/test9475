import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import requests
from botocore.exceptions import ClientError
import re
from bs4 import BeautifulSoup as bs
import aiohttp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from replit import db

sp_api = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id='1ed7357f1f684c31831c15c7411bafce', client_secret='31fec88630a844d6bf567b02f2166666'))


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.is_playing = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylists': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1',
                               'options': '-vn'}

        self.vc = ""
        self.current_song=''
        self.url_regex = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        

        self.session = aiohttp.ClientSession(headers={'User-Agent': 'python-requests/2.20.0'})

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            self.current_song = self.music_queue[0][0]['title']
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            self.current_song = self.music_queue[0][0]['title']
            song_url = self.music_queue[0][0]['source']

            try:
              if self.vc == "" or self.vc.is_connected() != True or self.vc == None:
                  self.vc = await self.music_queue[0][1].connect()
              elif self.vc == self.music_queue[0][1]:
                pass
              elif self.vc != self.music_queue[0][1] and self.vc != "":
                await self.vc.move_to(self.music_queue[0][1])
              else:
                  pass
            except:
              pass

            print(self.music_queue)
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(song_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="play", help="Plays a selected song from youtube", aliases=['p'])
    async def play(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel

        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            with YoutubeDL(self.YDL_OPTIONS) as ydl:
              try:
                requests.get(query)
              except:
                info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]

                song={'source': info['formats'][0]['url'], 'title': info['title'], 'thumbnail': info['thumbnail']}
                self.music_queue.append([song, voice_channel])   
                
              else:
                if ('playlist?list=') in query:
                  info = ydl.extract_info(query, download=False)
                  for entry in info['entries']:
                    link = link = "https://www.youtube.com/watch?v={}".format(entry['id'])
                    song =  ydl.extract_info(link, download=False)
                    r = {'source': song['formats'][0]['url'], 'title': song['title'], 'thumbnail': song['thumbnail']}
                    self.music_queue.append([r, voice_channel])
                    

                elif "https://open.spotify.com/track" in query:
                  if re.search(self.url_regex, query):
                    result = self.url_regex.search(query)
                    url = result.group(0)
                  async with self.session.get(url) as response:

                    page = await response.text()
                    s = bs(page, 'html.parser')

                    title = s.find('title')
                    title = title.string
                    title = title.replace('Spotify – ', '')
                    title = title.replace(' | Spotify,','')

                    info = ydl.extract_info(f"ytsearch:{title}", download=False)['entries'][0]
                    song={'source': info['formats'][0]['url'], 'title': info['title'], 'thumbnail': info['thumbnail']}
                    self.music_queue.append([song, voice_channel])

                elif "open.spotify.com/playlist" in query:

                  code = query.split('/')[4].split('?')[0]
                  try:
                    results = sp_api.playlist_items(code)
                    tracks = results['items']
                    while results['next']:
                        results = sp_api.next(results)
                        tracks.extend(results['items'])

                    links = []

                    for track in tracks:
                        try:
                            links.append(
                                track['track']['external_urls']['spotify'])
                        except:
                            pass

                    for link in links:
                        if re.search(self.url_regex, link):
                          result = self.url_regex.search(link)
                          url = result.group(0)
                        async with self.session.get(url) as response:

                          page = await response.text()
                          s = bs(page, 'html.parser')

                          title = s.find('title')
                          title = title.string
                          title = title.replace('Spotify – ', '')
                          title = title.replace(' | Spotify,','')

                          info = ydl.extract_info(f"ytsearch:{title}", download=False)['entries'][0]
                          song={'source': info['formats'][0]['url'], 'title': info['title'], 'thumbnail': info['thumbnail']}

                          self.music_queue.append([song, voice_channel])         
                  except:
                    pass
                else:
                  info = ydl.extract_info(query, download=False)
                  song = {'source': info['formats'][0]['url'], 'title': info['title'], 'thumbnail': info['thumbnail']}
                  self.music_queue.append([song, voice_channel])

            print(self.music_queue)
            if len(self.music_queue) == 0:
                await ctx.send("No songs were found")
            else:

                em = discord.Embed(title='Music Channel', color=discord.Color.blue())

                channel = discord.utils.get(ctx.guild.text_channels, name='music-commands')
                msg_id =  db[str(ctx.guild.id)]
                message = await channel.fetch_message(msg_id)

                em.add_field(name='What does this channel do', value='Type song name or paste song url in channel to play it or add it to queue. React to control the music',inline=False)

                songs=""
                if len(self.music_queue) <= 10:
                  for i in range(0, len(self.music_queue)):
                    songs += self.music_queue[i][0]['title']+'\n'
                  em.add_field(name='Queued Songs: ', value=songs,inline=False)
                else:
                  for i in range(0, 10):
                    songs += self.music_queue[i][0]['title']+'\n'
                  em.add_field(name='Queued Songs: ', value=f"{songs} ...{len(self.music_queue) - 10} more",inline=False)
                  
                    
                em.add_field(name='Pause:', value='React with ⏸ to pause song',inline=False)
                em.add_field(name='Resume:', value='React with ⏯ to resume song',inline=False)
                em.add_field(name='Skip:', value='React with ⏭ to skip song',inline=False)
                em.add_field(name='Stop:', value='React with ⏹️ to stop song', inline=False)
                em.add_field(name='Shuffle:', value='React with 🔀 to shuffle songs in he current queue', inline=False)
                em.set_footer(text='Bot created by Eggnogg')

                await message.edit(embed=em)

                try:
                  if self.is_playing == False:
                    await self.play_music()
                except ClientError:
                  pass

    @commands.command(name="queue", help="Displays the current songs in queue", aliases=['q'])
    async def q(self, ctx):
      if len(self.music_queue)>0: 
        em = discord.Embed(title='Song Queue:', color=discord.Color.red())
        count = 0
        for i in range(0, len(self.music_queue)):
          count += 1
              
          em.add_field(name=f'Song {i+1}:',value = self.music_queue[i][0]['title'] , inline=False)
        await ctx.send(embed=em)
      else:
        await ctx.send('Nothing in queue')


    @commands.command(name="skip", help="Skips the current song being played", aliases=['sk'])
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            await self.play_music()

    @commands.command(aliases=['ps'], help="Skips the current song being played")
    async def pause(self, ctx):
        ctx.voice_client.pause()
        # await ctx.send('Paused ')

    @commands.command(aliases=['st'], help="Stops playing song")
    async def stop(self, ctx):
        ctx.voice_client.stop()
        # await ctx.send('Music stopped ')
        await self.disconnect(ctx)

    @commands.command(aliases=['rs'], help="Resumes playing of the song")
    async def resume(self, ctx):
        ctx.voice_client.resume()
        # await ctx.send('Playing again...')

    @commands.command(aliases=['dc'], help="Disconnects bot from the voice channel")
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        # await ctx.send('Cheers vir eers')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music cog loaded')

    @commands.command(aliases=['cq'], help="Removes all songs from te queue")
    async def clearQ(self, ctx):
        self.music_queue.clear()
        # await ctx.send('Queue cleared.')
    
    @commands.command(aliases=['l'])
    async def lyrics(self, ctx):
      url = f'https://some-random-api.ml/lyrics?title=' + self.current_song

      async with ctx.typing():
        async with aiohttp.request("GET",url,headers={}) as r:
          if not 200 <= r.status <= 299:
            await ctx.send(f'No Lyrics Found for {self.current_song}')

          data = await r.json()
          print(data)

          if len(data["lyrics"]) > 2000:
            return await ctx.send(f"<{data['links']['genius']}>")

          embed = discord.Embed(title=data["title"],description=data["lyrics"],colour=ctx.author.colour)
          embed.set_thumbnail(url=data["thumbnail"]["genius"])
          embed.set_author(name=data["author"])
          await ctx.send(embed=embed)   
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        message = msg.content
        embeds = msg.embeds
        ctx = await self.client.get_context(msg)
        channel = discord.utils.get(ctx.guild.channels, name='music-commands')
        if embeds==[]:
          try:
            
            channel_id = channel.id
            if msg.channel.id == channel_id:
              await msg.delete()
              await self.play(ctx, message)
          except:
            pass
        else:
          try:
            channel_id = channel.id
            if msg.channel.id == channel_id:
              await msg.delete()
              await self.play(ctx, message)
          except:
            pass

    @commands.command(aliases=['sh'])
    async def shuffle(self, ctx):
        random.shuffle(self.music_queue)
        # await ctx.send('Queue Shuffled -> New Queue:')
        # await self.q(ctx)  

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
      channel = self.client.get_channel(payload.channel_id)
      message = await channel.fetch_message(payload.message_id)
      user = self.client.get_user(payload.user_id)
      ctx = await self.client.get_context(message)

      msg_id =  db[str(ctx.guild.id)]
      
      if msg_id == payload.message_id and payload.user_id != '888334067450388491':
        emoji = payload.emoji.name
        if emoji=='⏸':
          await message.remove_reaction(emoji, user)
          await self.pause(ctx)
          
        elif emoji=='⏯':
          await message.remove_reaction(emoji, user)
          await self.resume(ctx)

        elif emoji=='⏭':
          await message.remove_reaction(emoji, user)
          await self.skip(ctx)
          em = discord.Embed(title='Music Channel', color=discord.Color.blue())
          em.add_field(name='What does this channel do', value='Type song name or paste song url in channel to play it or add it to queue. React to control the music',inline=False)
          songs=""
          if len(self.music_queue) <= 10 and len(self.music_queue) != 0:
            for i in range(0, len(self.music_queue)):
              songs += self.music_queue[i][0]['title']+'\n'
            em.add_field(name='Queued Songs: ', value=songs,inline=False)
          elif len(self.music_queue) == 0:
            pass
          else:
            for i in range(0, 10):
              songs += self.music_queue[i][0]['title']+'\n'
            em.add_field(name='Queued Songs: ', value=f"{songs} ...{len(self.music_queue) - 10} more",inline=False)
            
              
          em.add_field(name='Pause:', value='React with ⏸ to pause song',inline=False)
          em.add_field(name='Resume:', value='React with ⏯ to resume song',inline=False)
          em.add_field(name='Skip:', value='React with ⏭ to skip song',inline=False)
          em.add_field(name='Stop:', value='React with ⏹️ to stop song', inline=False)
          em.add_field(name='Shuffle:', value='React with 🔀 to shuffle songs in he current queue', inline=False)
          em.set_footer(text='Bot created by Eggnogg')

          await message.edit(embed=em)          
          
        elif emoji=='⏹️':
          await message.remove_reaction(emoji, user)
          await self.clearQ(ctx)
          await self.stop(ctx)
          await message.remove_reaction(emoji, user)
          em = discord.Embed(title='Music Channel', color=discord.Color.blue())
          em.add_field(name='What does this channel do', value='Type song name or paste song url in channel to play it or add it to queue. React to control the music',inline=False)
          em.add_field(name='Pause:', value='React with ⏸ to pause song',inline=False)
          em.add_field(name='Resume:', value='React with ⏯ to resume song',inline=False)
          em.add_field(name='Skip:', value='React with ⏭ to skip song',inline=False)
          em.add_field(name='Stop:', value='React with ⏹️ to stop song', inline=False)
          em.add_field(name='Shuffle:', value='React with 🔀 to shuffle songs in he current queue', inline=False)
          em.set_footer(text='Bot created by Eggnogg')

          await message.edit(embed=em)
        elif emoji=='🔀':
          await message.remove_reaction(emoji, user)
          await self.shuffle(ctx)
          em = discord.Embed(title='Music Channel', color=discord.Color.blue())
          em.add_field(name='What does this channel do', value='Type song name or paste song url in channel to play it or add it to queue. React to control the music',inline=False)
          songs=""

          if len(self.music_queue) <= 10 and len(self.music_queue) != 0:
            for i in range(0, len(self.music_queue)):
              songs += self.music_queue[i][0]['title']+'\n'
            em.add_field(name='Queued Songs: ', value=songs,inline=False)
          elif len(self.music_queue) == 0:
            pass
          else:
            for i in range(0, 10):
              songs += self.music_queue[i][0]['title']+'\n'
            em.add_field(name='Queued Songs: ', value=f"{songs} ...{len(self.music_queue) - 10} more",inline=False)
              
          em.add_field(name='Pause:', value='React with ⏸ to pause song',inline=False)
          em.add_field(name='Resume:', value='React with ⏯ to resume song',inline=False)
          em.add_field(name='Skip:', value='React with ⏭ to skip song',inline=False)
          em.add_field(name='Stop:', value='React with ⏹️ to stop song', inline=False)
          em.add_field(name='Shuffle:', value='React with 🔀 to shuffle songs in he current queue', inline=False)
          em.set_footer(text='Bot created by Eggnogg')

          await message.edit(embed=em) 
        else:
          pass
        
        
def setup(client):
    client.add_cog(Voice(client))
