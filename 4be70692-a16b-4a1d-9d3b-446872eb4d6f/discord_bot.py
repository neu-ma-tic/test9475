import discord
import random
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from googletrans import Translator


token = 'Your-bot-token-here'
client = commands.Bot(command_prefix='Gary ')


@client.command()
async def info(ctx):
    embed = discord.Embed(title="Gary Goodspeed", description='Very annoying according to some Reddit users', color=0xeee657)
    embed.add_field(name='Ólafur Víðir', value='olividir')
    embed.add_field(name='Invite', value='[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=675796941992493066&permissions=0&scope=bot)')

    await ctx.send(embed=embed)

client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Gary Goodspeed", description='Very annoying according to some Reddit users\n Lists of commadns are:', color=0xeee657)
    embed.add_field(name='Gary info', value='Gives information about bot and creator', inline=False)
    embed.add_field(name='Gary nine', value='Quotes form Brooklyn 99', inline=False)
    embed.add_field(name='Gary final', value='Quotes from Gary in Final Space', inline=False)
    embed.add_field(name='Gary google <input>', value='Searches Google for the input given', inline=False)
    embed.add_field(name='Gary hacker', value='Gives name and link of articles with over 100 votes on HackerNews', inline=False)
    embed.add_field(name='Gary trans <lang prefix> <desired text>', value='Translates into any given language given before text.\n Example "Gary trans es Good morning" translates Good morning to Spanish')
    embed.add_field(name='Gary lang', value='Gives dictionary of all the languages supported and prefix of it')

    await ctx.send(embed=embed)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild:
            break
        print(f'{client.user} has connected to Discord!')
        print(f'{guild.name} (id: {guild.id})')


user = discord.Message.author

@client.command()
async def nine(ctx):
    brooklin_99_quotes = [
        'Cool. Cool, cool, cool, cool, cool, cool',
        'Night buddies are back in town',
        'Jake and Boil are on the case',
        'Me and Amy are having a bet on who catches the most perps',
        'Noice'
            ]
    response = random.choice(brooklin_99_quotes)
    await ctx.send(response)


@client.command()
async def final(ctx):
    garys_quotes = [
        'I didn\'t expect this hurt-coin deposit in my sadness savings',
        'Tough titty wompus',
        'Oh my crap',
        'Oh my double crap',
        'Lil Cato, take the mouth wheel',
        'You\'re a good guy Gary',
        'I HATE YOU KVN',
        'Get off my cheeks H.U.E',
        'The nice thing would have been to fake amnesia, Quin. I would have faked amnesia!'
    ]
    response1 = random.choice(garys_quotes)
    await ctx.send(response1)


@client.command()
async def bye(ctx):
    log_out = ['Man am I tired, I think I need to get some shuteye',
               'CAN\'T SEE, NEED TO CLOSE EYES',
               'I think I\'ll just lay down for a minute ',
               'Short of breath, vision fading..... leave me here to DIIIE'
               ]

    if ctx.author.id == 652236894968610871:
        response3 = random.choice(log_out)
        await ctx.send(response3)
        await client.logout()
    else:
        annoyed = [
            'Your\'re not the boss of me!!',
            'You dare to defy ME????',
            'Yeah, you bugger off!!',
            'You\'r words mean nothing to me!!!'
        ]
        pain = random.choice(annoyed)
        await ctx.send(pain)



@client.command()
async def trans(ctx, *args):
    hallo = list(args)
    bello = ' '.join(str(x) for x in hallo)
    if bello[2] == '-':
        b = bello[:5]
        c = bello[5:]
    elif bello[2] == 'a-z':
        b = bello[:3]
        c = bello[3:]
    else:
        b = bello[0:2]
        c = bello[2:]

    translator = Translator()
    translated = translator.translate(c, dest=b).text
    await ctx.send(f'{translated}')

@client.command()
async def lang(ctx):
    languages = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
        'fil': 'Filipino',
        'he': 'Hebrew'
    }
    await ctx.send(dict(map(reversed, languages.items())))


@client.command()
async def google(ctx, *args):
    complain1 = [
        'Why am I doing your job???',
        'Don\'t you know how to use the web??? ',
        'My fingers hurt from all the typing',
        'Do you know how easy it is to get lost on the WEB???',
        'These high-speed travels make my tummy hurt!!'
    ]
    complain2 = [
        'I hope you are happy for spending my time!!',
        'This is time I am never getting back!',
        'Oh my lord, the pain of doing physical work',
        'I will never EVER forgive you for this!!!',
        'Next time just open up a browser, I am too busy'
    ]
    anser1 = random.choice(complain1)
    await ctx.send(anser1)
    user_search = str(args)
    for output_message in search(user_search, tld='com', num=5, stop=3, pause=2):
        answer2 = random.choice(complain2)
        await ctx.send(output_message)
        await ctx.send(answer2)


@client.command(pass_context=True)
async def hacker(ctx):
    compain1 = [
        'Get of my cheeks!!',
        'This is a lot of stuff to go through',
        'This is a bit much to take in',
        'Oh my, it\'s up to my cheeks'
    ]
    complain2 = [
        'Now there is load of my chest',
        'I honestly got nothing for this',
        'Why do I always need to do stuff for others?',
        'I believe in you, next time.... you can do it!!'
    ]

    nr1 = random.choice(compain1)
    nr2 = random.choice(complain2)

    resp = requests.get('https://news.ycombinator.com/')
    resp2 = requests.get('https://news.ycombinator.com/news?p=2')
    soup = BeautifulSoup(resp.text, 'html.parser')
    soup2 = BeautifulSoup(resp2.text, 'html.parser')

    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    links2 = soup2.select('.storylink')
    subtext2 = soup2.select('.subtext')

    mega_links = links + links2
    mega_subtext = subtext + subtext2
    await ctx.send(nr1)

    for idx, item in enumerate(links):
        title = mega_links[idx].getText()
        href = mega_links[idx].get('href', None)
        vote = mega_subtext[idx].select('.score')
        if len(vote):
            vote = int(vote[0].getText().replace('points', ''))
            if vote > 99:
                await ctx.send(f'{title} {href} {vote} votes')

    await ctx.send(nr2)


client.run("OTE3ODE1NjQ5MzQ5Mjc5Nzc0.Ya-Mbg.w9BCsbwBgF2DM9dgzRYrwKw7NwY")


