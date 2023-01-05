import discord, datetime
from youtube_dl import YoutubeDL
from enum import Enum, auto


class VoiceStatus(Enum):
    DISCONNECTED = auto()
    IN_CHANNEL = auto()
    WRONG_CHANNEL = auto()


class music_bot():
    def __init__(self, client):
        self.client = client

        # youtube_dl options
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options':
            '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        # key: guild id, value: boolean
        # stores if currently playing music on connected servers
        self.is_playing = {}

        # key: guild id, value: datetime
        # stores when the bot last played music on connected servers
        self.last_played = {}

        # key: guild id, value: voice_channel
        # stores a voice client for each server it is currently connected to
        self.voice_channel = {}

        # key: guild id, value: list of songs
        # a song has a 'source' and a 'title' key
        self.music_queue = {}

    # searches the item on youtube
    # returns an audio file and it's title
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item,
                                        download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    # this function called first when someone uses the play command
    async def play(self, item, message):
        guild_id = message.guild.id
        if not await self.joins(guild_id, message):
            return

        song = self.search_yt(item)
        self.music_queue[guild_id].append(song)

        if self.is_playing[guild_id]:
            await message.channel.send(
                f"Added to queue `({len(self.music_queue[guild_id])})`: **{song['title']}**"
            )
        else:
            await self.play_music(guild_id, message)

    # infinite loop checking
    async def play_music(self, guild_id, message):
        if len(self.music_queue[guild_id]) > 0:
            self.is_playing[guild_id] = True

            song = self.music_queue[guild_id][0]
            m_url = song['source']
            self.music_queue[guild_id].pop(0)

            self.voice_channel[guild_id].play(
                discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS),
                after=lambda e: self.play_next(guild_id))

    def play_next(self, guild_id):
        if guild_id not in self.voice_channel:
            return

        if len(self.music_queue[guild_id]) > 0:
            self.is_playing[guild_id] = True

            song = self.music_queue[guild_id][0]
            m_url = song['source']
            self.music_queue[guild_id].pop(0)

            self.voice_channel[guild_id].play(
                discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS),
                after=lambda e: self.play_next(guild_id))
        else:
            self.is_playing[guild_id] = False
            self.last_played[guild_id] = datetime.datetime.now()

    # connects the client to a voice_channel if it wasn't already
    # returns True if the client is connected to tha same channel as the user
    async def joins(self, guild_id, message) -> bool:
        if message.author.voice == None:
            await message.channel.send(
                "You have to be in a voice channel to use this command.")
            return False

        voice_status = self.voice_status(message)
        if voice_status == VoiceStatus.DISCONNECTED:
            vc = await message.author.voice.channel.connect()
            self.voice_channel[guild_id] = vc
            self.is_playing[guild_id] = False
            self.last_played[guild_id] = datetime.datetime.now()
            self.music_queue[guild_id] = []
            return True
        elif voice_status == VoiceStatus.WRONG_CHANNEL:
            await message.channel.send(
                "Sorry, I'm busy playing music in another voice channel.")
            return False
        elif voice_status == VoiceStatus.IN_CHANNEL:
            return True

    # returns a string based on the client's and user's voice_channel
    def voice_status(self, message) -> VoiceStatus:
        channel_id = None
        for voice in self.client.voice_clients:
            if voice.guild.id == message.author.voice.channel.guild.id:
                channel_id = voice.channel.id
        if channel_id == None:
            return VoiceStatus.DISCONNECTED
        elif channel_id == message.author.voice.channel.id:
            return VoiceStatus.IN_CHANNEL
        elif channel_id != message.author.voice.channel.id:
            return VoiceStatus.WRONG_CHANNEL

    # returns True if the user and the bot is in the same channel
    # otherwise it returns False and gives feedback on why did the command fail
    async def in_right_channel(self, message) -> bool:
        if message.author.voice == None:
            await message.channel.send(
                "You have to be in a voice channel to use this command.")
            return False

        voice_status = self.voice_status(message)
        if voice_status == VoiceStatus.DISCONNECTED:
            await message.channel.send("I'm not connected you silly.")
            return False
        elif voice_status == VoiceStatus.WRONG_CHANNEL:
            await message.channel.send("GET OVER HERE!")
            return False
        elif voice_status == VoiceStatus.IN_CHANNEL:
            return True

    async def queue(self, message) -> None:
        if not await self.in_right_channel(message):
            return

        guild_id = message.guild.id
        if len(self.music_queue[guild_id]) > 0:
            msg = "Queue:\n"
            step = 1
            for song in self.music_queue[guild_id]:
                msg += f"\t`{step}` - **{song['title']}**\n"
                step += 1
            await message.channel.send(msg)
        else:
            await message.channel.send("The queue is empty.")

    async def skip(self, message) -> None:
        if not await self.in_right_channel(message):
            return

        guild_id = message.guild.id
        if self.is_playing[guild_id]:
            self.voice_channel[guild_id].stop()
        else:
            await message.channel.send("There is nothing to skip you silly.")

    async def leave(self, message) -> None:
        if not await self.in_right_channel(message):
            return

        guild_id = message.guild.id
        bot = self.voice_channel[guild_id]
        if self.is_playing[guild_id]:
            self.voice_channel[guild_id].stop()
        await bot.move_to(None)
        if guild_id in self.music_queue:
            del self.music_queue[guild_id]
        if guild_id in self.is_playing:
            del self.is_playing[guild_id]
        if guild_id in self.last_played:
            del self.last_played[guild_id]
        if guild_id in self.voice_channel:
            del self.voice_channel[guild_id]

    async def leave_check(self) -> None:
        now = datetime.datetime.now()

        for voice in self.client.voice_clients:
            guild_id = voice.guild.id
            last_played_delta = (now - self.last_played[guild_id]).seconds / 60
            if not self.is_playing[guild_id] and last_played_delta > 10:
                bot = self.voice_channel[guild_id]
                await bot.move_to(None)
                if guild_id in self.music_queue:
                    del self.music_queue[guild_id]
                if guild_id in self.is_playing:
                    del self.is_playing[guild_id]
                if guild_id in self.last_played:
                    del self.last_played[guild_id]
                if guild_id in self.voice_channel:
                    del self.voice_channel[guild_id]

    async def datas(self, message) -> None:
        queue = {}
        played = {}
        voice = {}
        for key in self.music_queue:
            queue[key] = ""
            for item in self.music_queue[key]:
                queue[key] += f"{item['title']}\n||{item['source']}||\n"
            if queue[key] == "":
                queue[key] = "empty"
        for key in self.last_played:
            played[key] = self.last_played[key].strftime("%H:%M:%S.%f")
        for key in self.voice_channel:
            voice[key] = self.voice_channel[key].channel.name
        await message.channel.send(f"music_queue:\n{queue}")
        await message.channel.send(f"is_playing:\n{self.is_playing}")
        await message.channel.send(f"last_played:\n{played}")
        await message.channel.send(f"voice_channel:\n{voice}")
