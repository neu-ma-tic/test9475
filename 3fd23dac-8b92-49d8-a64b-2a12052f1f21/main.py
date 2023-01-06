import discord
import asyncio

client = discord.Client()


async def mitoBackgroundCheck():
    await client.wait_until_ready()
    guild = client.get_guild(889840393150165012)
    user = guild.get_member(358874504694333452)
    if user.voice.self_deaf and user.voice.channel is not None:
        await asyncio.sleep(3600)
        if user.voice.self_deaf and user.voice.channel is not None:
            channel = client.get_channel(id=914299360819441694)
            await channel.send('<@358874504694333452> You coming back?')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello')


@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(id=914299360819441694)
    print(member, before.self_deaf, after.deaf)
    if member.id == 358874504694333452:  # Mito
        if after.self_deaf and not before.self_deaf:
            await channel.send('BYE MITO\nWE\'LL BE WAITING FOR YOUR RETURN :)')
            await mitoBackgroundCheck()
        if before.self_deaf and not after.self_deaf:
            await channel.send('BANGER MITO BACK')
    elif member.id == 283489590994665473:  # Lloyd
        if not before.self_deaf and after.self_deaf:
            await channel.send('smh smh\nWe shall be waiting expectantly for your return')
        elif before.channel is None:
            await channel.send('Oh FFS it\'s the gremlin')
        elif after.channel is None:
            await channel.send('Bye little gremlin')
          
    elif member.id == 723977673520709690:  # Lod
        if after.channel is not None and before.channel is None:
            await channel.send('oMg ItS aN aLt FfS')
    elif member.id == 609064362912514069:  # Lauren/Kat
        if after.channel is None or after.self_deaf:
            await channel.send('I guess the grass got mowed')
        if after.channel is not None and not after.self_deaf:
            await channel.send('Welcome back dear')
    else:
        genericJoin = 'Welcome to the VC <@' + str(member.id) + '>!!!'
        genericDeafen = 'Oh no bestie ' + member.display_name + ' can\' hear us'
        genericLeave = 'Bye Bye <@' + str(member.id) + '>'
        greetings = {
            # Jessie
            403198095933964301: [
                ':coffee:',
                genericDeafen,
                'No more :coffee:'
            ],
            # Ciel
            742401840653533235: [
                'Anime has joined the chat',
                genericDeafen,
                'No more squeals'
            ],
            # Edouard
            928611243231707137: [
                'FFS the French',
                genericDeafen,
                'Aha we have won the 100 year war'
            ],
            # Faith
            689869795750838323: [
                'Have Faith',
                genericDeafen,
                'We have lost Faith'
            ],
            # Issy
            649375029221654553: [
                'Fckin short people',
                genericDeafen,
                'Short Person Leave'
            ],
            # Jordan
            881934938180554813: [
                'Who\'s there, I can\'t see anyone',
                genericDeafen,
                'Short Person Leave'
            ],
            # Mars
            599772429992067074: [
                'OMG SCOOTISH MILF',
                genericDeafen,
                'no more scotish milf :broken_heart:'
            ],
            # Mel
            381897281860796427: [
                'Hide ur piss, Mel is here',
                genericDeafen,
                'Piss safe :sunglasses:'
            ],
            # Elysia
            181345207768449024: [
                'Omg a cat',
                genericDeafen,
                'Cat Go Bye-Bye Nya!'
            ],
            # Nicole
            851605001246867477: [
                'Heyyy Nicoleeeeeee, Time to be gay in ' + client.get_channel(id=889840393150165016).mention,
                genericDeafen,
                'Oh Dear, nicole gone'
            ],
            # Cecil
            752467858625134632: [
                'What is this a cavetown line?',
                genericDeafen,
                'Bye Cecil'
            ],
            # Dua
            730852789546254338: [
                'Dua Join',
                genericDeafen,
                'Dua Leave'
            ],
            # Ginger Joe
            363984938791337995: [
                'Ginger Joe Join',
                genericDeafen,
                'Ginger Joe Leave'
            ],
            # Iris
            695918632080769075: [
                genericJoin,
                genericDeafen,
                'Iris has done a Leave'
            ],
            # Charlie
            342294110226481154: [
                'League Of Legends Friend omgg',
                genericDeafen,
                'Charlie Leave'
            ],
            # Monkey Man
            462358987917099018: [
                'Paper can speak?',
                genericDeafen,
                'Guess someone played scissors'
            ],
            # Shanelle
            627887410818318336: [
                'print(\'shanelle joined\')',
                genericDeafen,
                'print(\'shanelle left\')'
            ]
        }

        if greetings[member.id] is not None:
            if after.channel is None and before.channel is not None:
                await channel.send(greetings[member.id][2])
            if not before.self_deaf and after.self_deaf:
                await channel.send(greetings[member.id][1])
            if after.channel is not None and before.channel is None and not after.self_deaf:
                await channel.send(greetings[member.id][0])





client.run('OTI5NDE3NTc4MjU2OTQxMDg2.YdnBkg.8Jo52LlMaNfGBeoI1FWTz3dytHM')
