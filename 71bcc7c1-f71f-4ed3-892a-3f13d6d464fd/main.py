import discord
from discord.ext import commands
from discord.ext.commands.core import check
from keep_alive import keep_alive
import random
import os

# Buat prefix fleksibel, Help commands!
client = commands.Bot(command_prefix='$')

# Menghapus command 'help' agar kita bisa membuat command sendiri (biar bisa custom)
client.remove_command('help')

@client.command(name='guess')
async def guess(context):

    await context.message.channel.send('Guess the number (1-10):')

# Memilih angka random, dari 1-10
    random_number = int(random.choice(range(1, 10)))
    print(random_number)

# Membaca input user
    msg = await client.wait_for("message", check=check)

# Mengulangi kesempatan jawab user 2x, total kesempatan 3x. Menggunakan cara memanggil ASYNC
    async def kesempatan_3():
        msg = await client.wait_for("message", check=check)
        try:
            if int(msg.content) == random_number:
                await context.message.channel.send('You WIN, the number was ' + str(random_number))
            elif int(msg.content) != random_number:
                await context.message.channel.send('You LOSE, the number was ' + str(random_number)) # Kesempatan habis. Kalah.

        except:
            await context.message.channel.send('Not a number')

    async def kesempatan_2():
        msg = await client.wait_for("message", check=check)
        try:
            if int(msg.content) == random_number:
                await context.message.channel.send('You WIN, the number was ' + str(random_number))
            elif int(msg.content) < random_number:
                await context.message.channel.send(msg.content + ' is too low')
                await kesempatan_3() # Memanggil kesempatan kedua. Memanggil function ASYNC
            elif int(msg.content) > random_number:
                await context.message.channel.send(msg.content + ' is too high')
                await kesempatan_3()
        except:
            await context.message.channel.send('Not a number') # Memanggil kesempatan ketiga
            
# Kesempatan jawab yang pertama. "try" dan "except" digunakan agar jika user memasukkan yang bukan integer, maka mengirimkan "Not a number"
    try:
        if int(msg.content) == random_number:
            await context.message.channel.send('You WIN, the number was ' + str(random_number))
        elif int(msg.content) < random_number:
            await context.message.channel.send(msg.content + ' is too low')
            await kesempatan_2() # Memanggil kesempatan kedua. Memanggil function ASYNC
        elif int(msg.content) > random_number:
            await context.message.channel.send(msg.content + ' is too high')
            await kesempatan_2()
    except:
        await context.message.channel.send('Not a number')

@client.command(name='credits')
async def credits(context):
    credits_embed = discord.Embed(
        title = 'Name of the bot',
        description = 'This bot was made out of curiosity of the coder, I [coder] have no intentions of copying/plagiarism.',
        colour = discord.Colour.red()
    )

    credits_embed.add_field(
        name = 'Coder',
        value = 'This bot was coded by "cghixcoh#0841" what a brilliant person!',
        inline = False
    )

    credits_embed.add_field(
        name = 'Programming Language',
        value = 'This bot was created with "Python 3"',
        inline = False
    )

    credits_embed.add_field(
        name = 'Libraries',
        value = 'This bot was created using "Random.py" and "Discord.py" library',
        inline = False
    )

    await context.message.channel.send(embed = credits_embed)

@client.command(name='greet')
async def greet(context):
    await context.message.channel.send('Hello User!')

@client.command(name='help')
async def help(context):
    help_embed = discord.Embed(
        title = 'List of Commands',
        description = 'Here are the list of commands and a little description for each.\n Note: The prefix is "$"',
        colour = discord.Colour.red()
    )

    help_embed.add_field(
        name = 'guess',
        value = 'Guess the number between 1-10, user has 3 chances',
        inline = False
        )

    help_embed.add_field(
        name = 'credits',
        value = 'Just credits',
        inline = False
        )
    
    help_embed.add_field(
        name = 'greet',
        value = 'Greets you, so you do not get lonely :)',
        inline = False
        )

    await context.message.channel.send(embed = help_embed)

keep_alive()
client.run(os.getenv('Token'))