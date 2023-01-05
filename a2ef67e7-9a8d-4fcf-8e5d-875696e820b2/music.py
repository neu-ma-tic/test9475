import asyncio
import youtube_dl
import pafy
import discord
from discord.ext import commands
from keep_alive import keep_alive
from music import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")


class Player(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self.song_queue = {}

    self.setup()

  def setup(self):
    for guild in self.bot.guilds:
      self.song_queue[guild.id] = []

  async def check_queue(self, ctx):
    if len(self.song_queue[ctx.guild.id]) >0:
      ctx.voice_client.stop()
      await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
      self.song_queue[ctx.quild.id].pop(0)

  async def search_song(self, amount, song, get_url=False):
    info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format":"bestaudio","quiet": True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
    if len(info['entries']) == 0: return None

    return [entry["webpage_url"] for entry in info['entries']] if get_url else info

  async def play_song(self, ctx, song):
    url = pafy.new(song).getbestaudio().url
    ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
    ctx.voice_client.source.volume = 0.5




  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
      return await ctx.send("Dołącz do któregoś kanału :D")

    if ctx.voice_client is not None:
      await ctx.voice_client.disconnect()

    await ctx.author.voice.channel.connect()

  @commands.command()
  async def leave(self,ctx):
    if ctx.voice_client is not None:
      return await ctx.voice_client.disconnect()

    await ctx.send("Już nie jestem tu potrzebny :(")

  @commands.command()
  async def play(self, ctx, *, song=None):
    if song is None:
      return await ctx.send("Musisz powiedzieć mi co chciałbyś usłyszeć")

    if ctx.voice_client is None:
      return await ctx.send("Chciałbym puszczać najlepszą muzyczkę, ale muszę być na kanale głosowym ;D ")

    #handler jeżeli nuta nie ma urla
    if not("youtube.com/watch?" in song or "https://youtu.be" in song):
      await ctx.send("Szukam najlepszej wersji dla Ciebie, to zajmie tylko chwilkę...")

      result = await self.search_song(1, song, get_url=True)

      if result is None:
        return await ctx.send("Przepraszam, nie znalazłem tej piosenki, spróbuj użyć mojego wyszukiwania.")

      song = result[0]
    
    if ctx.voice_client.source is not None:
      queue_len = len(self.song_queue[ctx.guild.id])

      if queue_len < 10:
        self.song_queue[ctx.guild.id].append(song)
        return await ctx.send(f"Aktualnie odtwarzam utwór, ta zostanie dodana do kolejki jako:{queue_len+1}.")

      else:
        return await ctx.send("Przepraszam, mam już 10 utworów w kolejce, poczekaj aż skończy się aktualna pozycja.")

    await self.play_song(ctx, song)
    await ctx.send(f"Aktualnie leci:{song}")

  @commands.command()
  async def search(self, ctx, *, song=None):
    if song is None: return await ctx.send("Zapomniałeś podać tytułu :D")
    
    await ctx.send('Szukam wybranego utworu, daj mi chwilę')

    info = await  self.search_song(5, song)

    embed = discord.Embed(title=f"Oto wyniki dla "{song} ":", description="Wybierz z listy dokładnie ten utwór, który chciałeś")

    amount = 0

    for entry in info["entries"]:
      embed.description +=f"[{entry['title']}]({entry['webpage_url']})\n"
      amount += 1
    
    embed.set_footer(text=f"Wyświetlam {amount} pierwszych wyników.")
    await ctx.send(embed=embed)

  
  @commands.command()
  async def queue(self, ctx): #wyświetla id aktualnej piosenki
    if len(self.song_queue[ctx.quild.id]) == 0:
      return await ctx.send("Twoja playlista jest pusta")

    embed = discord.Embed(title="Playlist", description="", colour=discord.Colour.dark_gold())
    i = 1
    for url in self.song_queue[ctx.guild.id]:
      embed.description += f"{i})\n"

      i += 1

    embed.set_footer(text= "Cieszę się, że mnie wybrałeś:D")
    await ctx.send(embed=embed)

  @command.command()
  async def skip(self, ctx):
    if ctx.voice_client is None:
      return await ctx.send("Aktualnie cisza.")

    if ctx.author.voice id None:
      return await ctx.send("Nie jesteś na kanale głosowym")

    if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
      return await ctx.send("Nie wybrałeś żadnego utworu :D")

    
    poll = discord.Embed(title=f"Głosowanie za pominięciem utworu utworzone przez - {ctx.author.name}#{ctx.author.discriminator}", description="**80% uczestników kanału musi zagłosować na tak, aby pominąć utwór.**", colour=discord.Colour.blue())
    poll.add_field(name = "Pomiń", value=":white_check_mark:")
    poll.add_field(name= "Zostaw", value= ":no_entry_sign:")
    poll.set_footer(text="Głosowanie zamknie się za 15 sekund")

    poll_msg = await ctx.send(embed=poll)
    poll_id = poll_msg.id

    await poll_msg.add_reaction(u"\2705") #głosowanie na tak
    await poll_msg.add_reaction(u"\U0001F6AB") #głosowanie na nie

    await asyncio.sleep(15)

    poll_msg = await ctx.channel.fetch_message(poll_id)

    votes = {u"\u2705": 0, u"\U0001F6AB": )=0}
    reacted = []

    for reaction in poll_msg.reactions:
      if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
        async for user in reaction.users():
          if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
            votes[reaction.emoji] += 1

            reacted.append(user.id)

    skip = False

    if votes[u"\u2705"] > 0:
      if votes[u"\U0001F6AB"] == 0 or votes[u"\2705"] / (votes[u"\2705"] + votes[u"\U0001F6AB"]) > 0.79:
        skip = True
        embed = discord.Embed(title="Pomiń zaakceptowane", description="Głosowanie na następny utwór przebiegło pomyślnie, pomijam ten utwór.***", colour=discord.Colour.green())

      if not skip:
            embed = discord.Embed(title="Pomiń odrzucone", description="*Pomijanie odrzucone.*\n\n**Mniej niż 80% uczestników kanału głosowało na tak, odtwarzam dalej**", colour=discord.Colour.red())

        embed.set_footer(text="Głosowanie zakończone.")

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        if skip:
            ctx.voice_client.stop()


    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused():
            return await ctx.send("Czekam na dalsze polecenia.")

        ctx.voice_client.pause()
        await ctx.send("Zatrzymuje odtwarzanie.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("Nie jestem podłączony do kanału głosowego.")

        if not ctx.voice_client.is_paused():
            return await ctx.send("Odtwarzam już utwór.")
        
        ctx.voice_client.resume()
        await ctx.send("Odtwarzam dalej ;D.")

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

bot.loop.create_task(setup())

keep_alive()
bot.loop.create_task(setup())
bot.run(os.getenv('TOKEN'))




