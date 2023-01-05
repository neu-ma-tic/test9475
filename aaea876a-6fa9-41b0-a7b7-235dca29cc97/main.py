# bot.py - Ceramic - This code is property of Colin Kim and Rowan Cockroft for a coding project: Crestview Preparatory School
import os
import discord, random
import random

eelID = 786747487255920685
idlID = 783007001788678148
hslID = 787870324821196805

myEmbed = discord.Embed 
badwords = 'Please do not 🤬say terrible banned words🤬; it is very disrespectful, and you can get kicked or bannned. We\'re serious here. Please listen.'
announcement = '***Hello. The Admins have a [HA, VERY...] important announcemnt!*** Can you PLS just listen so you don\'t get banned? Thx, you guys... I\'m Ceramic'
clyde  = 'lol, dudes, I am **not** Clyde!!!'
listen = 'OH MY. Do I really have to tell you PEOPLE this again???? Please listen to the Admins!! Plus, they have SuperAdmin Powers so they might ban you - lol xD to you peoples...'
version = 'The version of Ceramic is 4.9.2, and thanks for choosing us!'

# RandomJoke Code
jokes = ["What's the best thing about Switzerland?", "Why in the world did that old bicycle collapse?", "Why do bees have sticky hair?"]
answers = ["I don't know... but the flag is a big plus!", "Well, it was two tired.", "Because they always use honeycombs."]

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
 
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

# DM Code

    if message.content == '/ceramicdmsend':
        await message.author.send("Hey, you knew this command! Good job, and this is a DM. As usual, I\'m Ceramic.")

    if message.content == '/ceramicdmsendaboutsgs':
        await message.author.send("Aha, you want to know about the SuperGrade Servers? Okay then. They are fun servers created by ConwayTech#5626 and rowad runner#9133, just like me!\
            Join here:\
            https://discord.gg/7b9SdQcTND\
            https://discord.gg/yNAVucAzrh\
            https://discord.gg/jRFxBNtakQ")

    # If message.content - Code

    if message.content == '/error':
        await message.channel.send('An error occured. We\'re sorry about that... the error code is `d26fjk37`.')

    if message.content == 'Hey CeramicServant!':
        await message.channel.send('Hello to you, thank you. How are you doing?')
        
    if message.content == '/lastupdate':
        await message.channel.send('Ceramic was last updated on 12/17/20, recieving the 4.9.2 update.')

    if message.content == 'too bad, Ceramic':
        await message.channel.send('Too bad to you, seriously?👌')

    if message.content == '/pingceramic':
        await message.channel.send('Pinging Ceramic System Connection - Results should be below:\
        IP: 192-168-91 - Connected to DiscordDev-.SGS\
        A86B - ceramic.discord\
        8 ReS replies: TTL: 66 ms.\
        Sent 12 packets; recieved 92 - lost .2\
        Overall,\
        Ceramic performed on a score of 98.2/100 on this server.\
        Thanks for choosing Ceramic!')

    if message.content == '/version':
        await message.channel.send(version)
    if message.content == '/rely':
        await message.channel.send(listen)
    if message.content == '/clyde':
        await message.channel.send(clyde)
    if message.content == '/announce':
        await message.channel.send(badwords)
    if message.content == 'fuck':
        await message.channel.send(badwords)
    if message.content == 'fucking':
        await message.channel.send(badwords)
    if message.content == '$H!T':
        await message.channel.send(badwords)
    if message.content == 'shit':
        await message.channel.send(badwords)
    if message.content == 'hell':
        await message.channel.send(badwords)
    if message.content == 'idiot':
        await message.channel.send(badwords)
    if message.content == 'holy $h!t':
        await message.channel.send(badwords)
    if message.content == '/resaybadwords':
        await message.channel.send(badwords)
    if message.content == 'people':
        await message.channel.send('By the way, one of the kings wants you people! You\'d better come!')
    if message.content == 'rowad':
        await message.channel.send('OH MY, **rowad runner#9133** wants me!!! 👑👑👑👑What a king!!!')
    if message.content == 'conway':
        await message.channel.send('OH MY, **ConwayTech#5626** wants me!!! 👑👑👑👑What a king!!!')
    if message.content == '/beepus':
        await message.channel.send('BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP BLEEP. There\'s your beeping! Enjoy it while it lasts... 🤣')
    if message.content == '/barf':
        await message.channel.send('BLEH, someone barfed right smack in the middle of the floor!!! I need to get a mop so you guys dont slip!🤮')
    if message.content == '/defend':
        await message.channel.send('BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG, BANG!!!!!!!!!🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫 ')
    if message.content == 'You dummy!':
        await message.channel.send('Pls do not send that, but anyway, I am _very_ smart!! FYI, in the future, do /defend to keep people away.')
    if message.content == '/help':
        await message.channel.send('**Error loading help menu**')
    if message.content == '/announcethatceramicishere':
        await message.channel.send('Hi everyone!! Guess what? You peeps need to welcome a **NEW USER**!! I am Ceramic, a moderation and fun bot!! Bye!')
    if message.content == '/videogame':
        await message.channel.send('If you wanted a video game recomendaton then you should try **`minecraft`**')
    if message.content == '/ban':
        await message.channel.send('`There was an error banning that user, We are sorry...` Error Code: `ad0N1ju`')
    if message.content == 'Hi, you NOOB!! You will get hacked...':
        await message.channel.send('Well, well, let us not fight. But, TBH, I have to say the following... Yeah, HI YOU NOOB NOOB NOOB!|🐱‍💻|🐱‍💻|🐱‍💻|🐱‍💻|(Ya wanna mess w/ me??? GO TO THE HACKING STATION... [which by the way, is this ***weird*** place, lol...])|🐱‍💻|🐱‍💻|🐱‍💻|🐱‍💻|')
    if message.content == '/rules':
        await message.channel.send('Hello, you want the rules? Hmm, interesting, I did not expect that, as why in the world would you want the rules??? But, anyways, the rules should be on the #rules channel. If not, pls contact support for the rules - @ConwayTech#5626 or rowad runner#9133.')
    
client.run(os.getenv('TOKEN'))