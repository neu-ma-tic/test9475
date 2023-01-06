import discord

'''
Als je kaal deze code gebruikt is het aan te raden je bot maar in één
server te gebruiken. Als je je bot in meerdere servers wilt gebruiken
moet je in veel functionaliteit nog iets van 'Guild' herkenning
inbouwen - dat is hoe Discord servers intern noemt.

Hier in ieder geval wat voorbeelden waar je op uit kunt breiden :) 

Let er op dat je voor berichten versturen altijd `await` moet gebruiken,
print en return zijn lokaal terwijl await ze naar je Discord stuurt.
'''

TOKEN = "ODc5NTQ1MDI3NDk0MzAxODA2.YSRSIw.9bms_UKzkZoRNOOOxngjRp0fw1E"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    # Zo kun je in je console zien dat de bot online gegaan is
    # Maar je kunt hier natuurlijk laten doen wat je wilt

@client.event
async def on_message(message):
    if message.author == client.user:
        # Zodat de bot niet op zichzelf reageert
        return
    
    if message.content.startswith("Hello"):
        # Met `await message.channel.send(...)` stuur je dus berichten
        # Terug naar het kanaal waar het ontvangen bericht vandaan kwam
        # Het originele bericht staat in `message.content`, en deze kun
        # Je dus ook gebruiken om op keywords te filteren
        await message.channel.send("Hey!")
    
    if message.content.lower() == 'taart':
        if message.channel.name == 'jouw_kanaal_naam':
            # Deze check kun je gebruiken als je wilt dat je bot alleen
            # In specifieke kanalen reageert
            await message.channel.send("Ik houd van appeltaart")
    
    if 'wanneer ben ik jarig' in message.content.lower():
        await message.channel.send("Maar ik ben helemaal niet jarig :(")
    
    else:
        await message.channel.send(message.content)

@client.event
async def on_member_join(member):
    # Deze functie stuurt een DM naar een nieuw lid dat de server met
    # je bot joint, maar je kunt natuurlijk laten doen wat je wilt
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)