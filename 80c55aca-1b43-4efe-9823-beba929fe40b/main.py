import discord
from discord.ext import commands
import random, os
import datetime
import time
import json
import requests
from keep_alive import keep_alive
import requests
from bs4 import BeautifulSoup

intents = discord.Intents().all()
client = commands.Bot(command_prefix='', intents=intents)
STUDENTS = {"Nikola Babić": "29.9.", "Frane Baletić": "29. 10.", "Matej Bedenic": "30.5.", "Lovro Gale": "28.1.", "Marti": "21.8.", "Gospodar Univerzuma": "big bang / 22.8.", "Luka": "22.8.", "Bartol Perić": "22.12.", "Toma Petrušić": None, "Robi Markulin": "29.9.", "Jagodario": None, "Renato Krpan": None, "Petar Hržina": None, "Marko Zrilić": None, "Jakov Džijan": None, "Alen Bešić": None, "Joško Lukač": None, "Anja Bilać": "28.11.", "Petra Delić": None, "Andrea Brzica": "5.6.", "Anamarija Mihaljević": None, "Hana Kos": None, "Manjina": None, "Lucija Kantolić/Oš igrat Apex": "2.4.", "Katarina Madunić": None, "Vita Crnjak": "3.12."}

API_KEY = "tx4RoxvmzTNw"
PROJECT_TOKEN = "tY1u4rDigDVx"
RUN_TOKEN = "tG1JJ5gKXsvC"


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Send zoom links'))
    print('Bot is ready!')
    for guild in client.guilds:
        if guild.name == 'DISCORD_GUILD':
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} || (id: {guild.id})\n'
    )

@client.command()
async def deletechannel(ctx, channel: discord.TextChannel):
    embed = discord.Embed(
      title="Succes",
      description = f"Channel: {channel} has been deleted" 
    )

    await ctx.send(embed=embed)
    await channel.delete()


@client.command(aliases=['roll', 'roll_dice', 'dicer'])
async def roll_a_dice(ctx):
    numbers = [1, 2, 3, 4, 5, 6]
    await ctx.send(f'You rolled number {random.choice(numbers)}!')


@client.command(aliases=['ima_li_kustec', 'kustec?'])
async def is_kustec_here(ctx):
    await ctx.send('Nooooo! Yessss!')


@client.command()
async def kustec_vs_puljiz(ctx):
    await ctx.send('Puljiz / Kustec = -inf')


@client.command()
async def covid_cases(ctx, name):
    response = requests.get(f"https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data", params={"api_key": API_KEY})
    data = json.loads(response.text)
    message = ''
  
    if "case" in name.lower(): message = "Total COVID-19 Cases: " + str(data['total'][0]['value'])
    elif "death" in name.lower(): message = "Total COVID-19 Deaths: " + str(data['total'][1]['value'])
    elif "recover" in name.lower(): message = "Total COVID-19 Recovered: " + str(data['total'][2]['value'])
    else: message = "Sorry wrong attribute!"

    await ctx.send(message)


@client.command(aliases=['club'])
async def kartaski_klub_rijeke_zrmanje(ctx):
    await ctx.send('Uđite u najbolji kartaški klub na našim predjelima: https://discord.gg/YHkRCEQv')


@client.command()
async def clear(ctx, amount: int, code):
    if code == "1234":
        await ctx.channel.purge(limit=amount + 1)


@client.command()
async def LiiiigaLegendiii(ctx, path):
    await ctx.send("Opening League of Legends!!!")
    os.startfile(path)


@client.command()
async def Minecraft(ctx, path):
    await ctx.send("Opening Minecraft!!!")
    os.startfile(path)


@client.command()
async def kick(ctx, member: discord.Member):
    await member.kick(reason='beacause')
    await ctx.send(f'{member} has been kicked!')


@client.command(alias=['its friday night'])
async def its_friday_night(ctx):
    now = datetime.datetime.now()
    day = datetime.datetime.weekday(now)
    now = str(now)[12]

    if day == 4:
        if int(now) > 7:
            await ctx.send(f"Its friday night!")
        else:
            await ctx.send('Its almost friday night!')
            await ctx.send('-p friday')
    else:
        await ctx.send('Its not friday night :(')


@client.command()
async def ban(ctx, member: discord.Member, code):
    if code == "123456":
        await member.ban(reason='Because1')
        name = member.mention
        await ctx.send('Someone was banned!')
        await ctx.send(f'{name} has been baned!')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unband {user.name}')

@client.command(aliases=['school_left', "left_dead"])
async def spasenje_za(ctx, school_end="6-16"):
    now = str(datetime.date.today()).split("-")[1:]
    school_end = str(school_end).split("-")
    now = list(map(int, now))
    school_end = list(map(int, school_end))
    months_left = school_end[0] - now[0]
    days_left = 30 * months_left
    if school_end[1] >= now[1]:
      days_left += school_end[1] - now[1]
    else:
      days_left += now[1] - school_end[1]
      months_left -= 1
    await ctx.send(months_left, days_left)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        pass# await ctx.send('Invalid command.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permission for this command.")


@client.command()
async def spam(ctx, member: discord.Member, amn=20):
    for i in range(amn):
        await ctx.send(f'I"m <--(ne da mi se sve stavit u dvostruke navodnike) am spaming {member.mention}!!!!')


@client.command()
async def truefalse(ctx, *, challenge):
  await ctx.send(challenge + " : " + random.choice(["True", "False"]))


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Yes!',
                 'Yes, of course!',
                 'YESSSS',
                 '100%, yes!',
                 "I'm not sure.",
                 'Ask me later.',
                 'Its questionable.',
                 'No!',
                 'Of course, no!',
                 'NOOOOO',
                 'No way!'
                 ]

    if "lovro" not in question.lower() and ("gei" in question.lower() or "gey" in question.lower() or "peder" in question.lower() or "gej" in question.lower()):
        await ctx.send(f'Question: {question}\nAnswer: {responses[random.randint(0, 3)]}')
    else:
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['print'])
async def dprint(ctx, *, msg):
    msg = str(msg)
    await ctx.send(" >>> " + msg)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    ctx.send('Cog loaded!')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    ctx.send('Cog unloaded!')


@client.command(aliases=['izseri', 'poseri'])
async def izvrijeđaj(ctx, *, name):
    if name[-1] == 'a' or name.lower() == 'tomo':
        await ctx.send(f'{name} ti kravo glupa!')
        await ctx.send('Ko te rodio tako glupu!')
        await ctx.send('Glupačo odi u vrapče prognana si!')
    else:
        await ctx.send(f'{name} ti si moron retardirani!')
        await ctx.send('Ko te rodio tako glupog!')
        await ctx.send('Degenu odi u vrapče prognan si!')


@client.command()
async def test_webserver(ctx):
  await ctx.send("[Webserver] Connecting to port 8.8.8.8")
  time.sleep(0.4)
  await ctx.send("[Webserver] Connected to port 8.8.8.8")
  time.sleep(0.4)
  await ctx.send("[Bot] Webserver |setup| = true\n[Bot] Client = true")


@client.command(aliases=['choose'])
async def name_choser(ctx, amn, *, challenge):
    chosen = ''

    amn = int(amn)

    if amn >= 26:
      amn = 26
    
    students = random.sample(STUDENTS.keys(), amn)
    for i, stud in enumerate(students):
      chosen += str(i + 1) + '.) ' + stud + "\n"

    await ctx.send("Students chosen for " + str(challenge) + ":")
    await ctx.send(chosen)


@client.command()
async def get_temperature(ctx, *, place):
    await ctx.send(format_data(place))


def get_data():
    response = requests.get("https://meteo.hr/naslovnica_aktpod.php?tab=aktpod")

    soup = BeautifulSoup(response.text, "html.parser")
    cities = soup.find_all("div", class_="fd-c-marker-auto__name")
    temperatures = soup.find_all("span", class_="fd-c-marker__temp-inline")
    formated_cities = [city.text.replace(" ", "").replace("\n", "") for city in cities]
    return formated_cities, temperatures


def format_data(city_selected):
    formated_cities, temperatures = get_data()

    for n, city in enumerate(formated_cities):
      if city.lower() == city_selected.lower():
        return "In {} temperature is {}".format(city, temperatures[n].text.replace(" ", "").replace("\n", ""))
      elif "list" in city_selected.lower():
        return formated_cities

    return f"Sorry city {city_selected} is not in ou database!"


@client.command()
async def rodendan(ctx, *, name):
    try:
      for stname, date_ in STUDENTS.items():
          if "rio" in name.lower():
              name = "Jagodario"
          elif "sičen" in name.lower():
              name = "SiĆenica"
          elif "bartol" in name.lower():
              name = "daj se nemoj derat!"
              await ctx.send(name + "22.12.")
          if name.lower().strip() in stname.lower():
              await ctx.send(f"Name: {name[0].upper() + name[1:]}, Birthday: {date_}")
    except Exception as e:
      print(str(e))



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



keep_alive()
TOKEN = os.environ.get("TOKEN")
print(TOKEN)
client.run(TOKEN)
