import requests
import time
import json
import base64
import discord
import random
import os
import proxies
from discord.ext import commands



f = open('premium.txt','r')
premiums = f.read().splitlines()
f.close()


def last_used(user_id):
    f = open('log.txt','r')
    text = f.read().splitlines()
    f.close()
    
    d = {}
    for line in text:
        if ':' in line:
            d[line[0:line.find(':')]] = line[line.find(':')+1:len(line)]

    if str(user_id) in d:
        return d[str(user_id)]
    else:
        return 0

def update_dict(user_id):
    f = open('log.txt','r')
    text = f.read().splitlines()
    d = {}
    for line in text:
        if ':' in line:
            d[line[0:line.find(':')]] = line[line.find(':')+1:len(line)]
    d[str(user_id)] = str(int(time.time()))

    new_text_file = ''
    keys = d.keys()
    for key in keys:
        new_text_file = new_text_file + str(key) + ':' + str(d[key]) + '\n'
    new_text_file = new_text_file[0:len(new_text_file) -1]
    
    f.close()
    f = open('log.txt','w')
    f.write(new_text_file)
    f.close()

def bypass_link(url):
    first_link = 'https://publisher.linkvertise.com/api/v1/redirect/link/static/'

    second_link = 'https://publisher.linkvertise.com/api/v1/redirect/link/insert/linkvertise/path/here/target?serial=base64encodedjson'
    second_link_front = second_link[0:second_link.find('insert/linkvertise')]
    second_link_back = second_link[second_link.find('/target?serial'):second_link.find('base64encodedjson')]

    f = open('proxies.json','r')
    data = json.load(f)
    f.close()
    proxies = data['proxies']

    tries = 0

    while True:

        proxy = random.choice(proxies)

        http_proxy  = "http://" + proxy['proxy']['http']
        https_proxy = "https://" + proxy['proxy']['https']
        ftp_proxy   = "ftp://" + proxy['proxy']['http']

        proxyDict = { 
                    "http"  : http_proxy, 
                    "https" : https_proxy, 
                    "ftp"   : ftp_proxy
                    }

        try:


            #proxy = proxies.Proxies()

            input_link = url
            link = ''
            if '.com/' in input_link:
                if '?o=' in input_link:
                    link = input_link[input_link.find('.com/')+5:input_link.find('?o=')]
                else:
                    link = input_link[input_link.find('.com/')+5:len(input_link)]
            if '.net/' in input_link:
                if '?o=' in input_link:
                    link = input_link[input_link.find('.net/')+5:input_link.find('?o=')]
                else:
                    link = input_link[input_link.find('.net/')+5:len(input_link)]
            

            r = requests.get(first_link + link,proxies=proxyDict,timeout=4)
            #r = proxy.scrape(first_link + link)
            text = r.text
            link_id = text[text.find('"id":')+5:text.find(',"url":')]


            new_json = {"timestamp":int(time.time()), "random":"6548307", "link_id":int(link_id)}

            s = json.dumps(new_json)
            json_converted = base64.b64encode(s.encode('utf-8'))
            json_converted = str(json_converted)
            json_converted = json_converted[2:len(json_converted)-1]

            #r = proxy.scrape(second_link_front + link + second_link_back + json_converted)
            r = requests.get(second_link_front + link + second_link_back + json_converted,proxies=proxyDict,timeout=4)
            converted_json = json.loads(r.text)
            new_link = converted_json['data']['target']
            break
        except:
            sdfasdfa='324'
        
        if tries >= 3:
            return None
        tries = tries + 1

    
    return new_link

def get_data():

    f = open('data.json','r')
    data = json.load(f)
    f.close()

    return data
    
def add_message(message,bypass_time):

    data = get_data()

    message_ids = []

    for temp in data['messages']:
        message_ids.append(temp['message_id'])
    
    message_id = message.id
    time_created = message.created_at


    if message_id not in message_ids:
        new_json = {
            "message_id":message.id,
            "channel_id":message.channel.id,
            "channel_name":str(message.channel),
            "author_id": message.author.id,
            "author_username":str(message.author),
            "unix_epoch_time":time_created.timestamp(),
            "year":time_created.year,
            "month":time_created.month,
            "day":time_created.day,
            "hour":time_created.hour,
            "minute":time_created.minute,
            "second":time_created.second,
            "command":"bypass",
            "content":message.content,
            "time_elapsed":bypass_time
        }

        data['messages'].append(new_json)

        f = open('data.json','w')
        json_object = json.dumps(data, indent = 4)
        
        f.write(json_object)
        f.close()
            
def is_admin(user_id):
    f = open('admins.txt','r')
    admins = f.read().splitlines()
    f.close()
    if str(user_id) in admins:
        return True
    return False


# invite https://discord.com/api/oauth2/authorize?client_id=811339635950485546&permissions=8&scope=bot

client = commands.Bot(command_prefix = '.', help_command = None)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name=".help"))
    print('Bot is online.')


@client.command()
async def bypass(ctx, url):

    start_time = time.time()

    if ctx.channel.id != 813841766675513386 and ctx.channel.id != 813841861462589462:
        embed = discord.Embed(
            title = 'Error',
            color = discord.Color.red(),
        )

        embed.add_field(name='Wrong channel', value = 'Please use the #chat channel in https://discord.gg/PvVZ7ZWzVs to bypass links', inline=False)
        await ctx.send(embed = embed)
    else:
        
        try:

            user_id = ctx.message.author.id
            mention = ctx.message.author.mention
            
            #print(ctx.message.channel.id)

            limit = 3 #seconds

            embed = discord.Embed(
                title = 'Linkvertise Bypasser',
                color = discord.Color.green(),
                description = mention+"'s shortlink"
            )
            embed.set_footer(text='Bypassed by SkippyTurtle#0001')


            if str(user_id) in premiums:
                embed.add_field(name='Original Link', value = url, inline=False)
                embed.add_field(name='New link', value = bypass_link(url), inline=False)

            if str(user_id) not in premiums:
                if last_used(user_id) == 0 or int(int(time.time()) - int(last_used(user_id))) >= limit:
                    update_dict(user_id)

                    embed.add_field(name='Old Link', value = url, inline=False)
                    embed.add_field(name='New link', value = bypass_link(url), inline=False)
                    
                else:
                    embed.add_field(name='ERROR', value = 'You next avaliable bypass is in ' + str( limit - (int(time.time()) - int(last_used(user_id))) ) + ' seconds', inline=False)

            if bypass_link(url) == None:
                raise Exception("Link invalid")

            time_elapsed = time.time() - start_time

            add_message(ctx.message,time_elapsed)
            
            await ctx.send(embed = embed)
        except:

            user_id = ctx.message.author.id
            mention = ctx.message.author.mention

            embed = discord.Embed(
                title = 'Linkvertise Bypasser',
                color = discord.Color.red(),
                description = mention+"'s shortlink"
            )

            embed.add_field(name='Error', value = 'After numerous attemps, your link could not be bypassed.\n\nYour link provided was either not a proper Linkvertise link or the link is dead.', inline=False)
            #embed.add_field(name='Error', value = 'The bot is currently being rate limited right now. Please be patient and try again later.', inline=False)

            time_elapsed = time.time() - start_time
            add_message(ctx.message,time_elapsed)

            await ctx.send(embed = embed)

@client.command()
async def logold(ctx):

    if is_admin(ctx.author.id) == False:

        old_messages = []
        data = get_data()
        existing_messages = []
        existing_message_ids = []
        for msg in data['messages']:
            existing_messages.append(msg)
            existing_message_ids.append(msg['message_id'])

        async for msg in ctx.history(limit=1000):
            if '.bypass' in msg.content:
                if msg.id not in existing_message_ids:
                    old_messages.append(msg)
        
        for msg in old_messages:
            add_message(msg,1.635465645613)
        
        await ctx.send('Logged All Old .bypass Commands Successfully')
    else:
        await ctx.send('Sorry, this command is for admins only!')

@client.command()
async def stats(ctx):
    embed = discord.Embed(
        title = 'Server Stats',
        color = discord.Color.blue(),
    )

    embed.add_field(
        name = 'Member count', 
        value = '`' + str(ctx.guild.member_count) + '`' + ' members', 
        inline = False
    )

    total_bypasses = len(get_data()['messages'])

    embed.add_field(
        name = 'Bypass Stats', 
        value = '`' + str(total_bypasses) + '`' + ' total bypasses', 
        inline = False
    )


    await ctx.send(embed = embed)


@client.command()
async def ping(ctx):

    await ctx.send(str(int(client.latency*1000)) + ' ms')

@client.command()
async def flipcoin(ctx):
    options = ['heads','tails']
    option = random.choice(options)

    embed = discord.Embed(
        title = 'Flip coin',
        color = discord.Color.blue(),
        description = option
    )

    await ctx.send(embed = embed)

@client.command()
async def rock(ctx):
    options = ['scissors','paper','rock']
    option = random.choice(options)

    embed = None

    if option == 'scissors':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.green(),
            description = 'I chose `Scissors` You Won!'
        )
    
    if option == 'paper':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.red(),
            description = 'I chose `Paper` You Lost!'
        )
    
    if option == 'rock':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.blue(),
            description = 'I chose `Rock` You Tied!'
        )

    await ctx.send(embed = embed)

@client.command()
async def paper(ctx):
    options = ['scissors','paper','rock']
    option = random.choice(options)

    embed = None

    if option == 'rock':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.green(),
            description = 'I chose `Rock` You Won!'
        )
    
    if option == 'paper':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.blue(),
            description = 'I chose `Paper` You Tied!'
        )
    
    if option == 'scissors':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.red(),
            description = 'I chose `Scissors` You Lost!'
        )
    
    await ctx.send(embed = embed)

@client.command()
async def scissors(ctx):
    options = ['scissors','paper','rock']
    option = random.choice(options)

    embed = None

    if option == 'rock':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.red(),
            description = 'I chose `Rock` You Lost!'
        )
    
    if option == 'paper':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.green(),
            description = 'I chose `Paper` You Won!'
        )
    
    if option == 'scissors':
        embed = discord.Embed(
            title = 'Rock, Paper, Scissors',
            color = discord.Color.blue(),
            description = 'I chose `Scissors` You Tied!'
        )
    
    await ctx.send(embed = embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        color = discord.Color.blue(),
        description = 'Command Parameters: <required> {optional}\nOfficial Discord Help Server: https://discord.gg/8uterAf'
    )
    
    embed.add_field(
        name = '.help', 
        value = 'Displays Help', 
        inline = False
    )

    embed.add_field(
        name = '.bypass <link>', 
        value = "Get what's behind the shortlink", 
        inline = False
    )

    embed.add_field(
        name = '.ping', 
        value = 'Gives ping', 
        inline = False
    )
    
    embed.add_field(
        name = '.stats', 
        value = "Displays general server stats", 
        inline = False
    )

    embed.add_field(
        name = '.logold', 
        value = '(Admin only), Logs old commands', 
        inline = False
    )

    embed.add_field(
        name = '.flipcoin', 
        value = 'Flips a coin', 
        inline = False
    )

    embed.add_field(
        name = '.rock', 
        value = 'Plays rock paper scissors', 
        inline = False
    )

    embed.add_field(
        name = '.paper', 
        value = 'Plays rock paper scissors', 
        inline = False
    )

    embed.add_field(
        name = '.scissors', 
        value = 'Plays rock paper scissors', 
        inline = False
    )
    

    await ctx.send(embed = embed)


client.login(process.env.TOKEN)