import discord, os
from rythm import music_bot

# Globals and variables I don't wanna put in main

intents = discord.Intents.all()
client = discord.Client(intents=intents)
rythm2 = music_bot(client)
my_token = os.environ['TOKEN']
db_url = os.environ['DB_PASSWORD']
dev_id = int(os.environ['DEV'])
dev_guild_id = int(os.environ['DEV_GUILD'])
berencek_id = int(os.environ['BERENCEK'])
uptime_channel_id = int(os.environ['UPTIME'])

birthdays_db = "birthdays2"
command_logs_db = "commandLogs"

command_prefix = "!"
description = "A legendary Jedi Master, Obi-Wan Kenobi is a noble man and gifted in the ways of the Force."

yesdoit = "https://media.tenor.com/images/32c950f36a61ec7e5060f5eee9140396/tenor.gif"
dontdoit = "https://media.tenor.com/images/efe75f294292b65bd21e32541d298994/tenor.gif"
hello = "https://media.tenor.com/images/dc26484243124b4f42647f3eff67f637/tenor.gif"
happy = "http://media.tenor.com/images/d77404d99b2c8e7c8060656a291bea75/tenor.gif"
xmas = "https://www.youtube.com/watch?v=Al_y-v7qcjg"
not_sanyi_text = "This isn't the function you’re looking for."

commands_text = 'Commands:\n'
commands_text += '\t' + command_prefix + 'hello - Köszön egyet\n'
commands_text += '\t' + command_prefix + 'coinflip - <https://youtu.be/dmQDVHjTveI>\n'
commands_text += '\t' + command_prefix + 'newbd - Születésnapi köszöntő hozzáadása\n'
commands_text += '\t' + command_prefix + 'delbd - Születésnapi köszöntő törlése\n'
commands_text += '\t' + command_prefix + 'setchannel - Születésnapi köszöntő szoba beállítása\n'
commands_text += '\t' + command_prefix + 'forbidden - Egy ősi sith technika\n'
commands_text += '\t' + command_prefix + 'play / p - hangos 2.0\n'
commands_text += '\t' + command_prefix + 'queue / q\n'
commands_text += '\t' + command_prefix + 'skip / s\n'
commands_text += '\t' + command_prefix + 'leave / l\n'
