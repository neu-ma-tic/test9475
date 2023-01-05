-3 -m pip install -U discord.py
 import discordimport os

client = discord.Client()

@client.eventasync def on_ready(): print(‘We have logged in as {0.user}’.format(client))

@client.eventasync def on_message(message): if message.author == client.user: return

if message.content.startswith(‘$hello’): await message.channel.send(‘Hello!’)

client.run(os.getenv(‘OTE4NTY4NDA1Mzc0NzQ2NjQ0.YbJJfg.TlQRpgQe4SvzkTiW8pifYuO5LLw’))
py -3 main.py