import discord, random
from discord.ext import commands
from webserver import keep_alive
import os


crosses_Game = False
player_One = None
player_Two = None
player_Turn = 1

colourgame_Running = False
guesses = 0
colours = []

row_A = ['/','/','/','/','/','/','/']
row_B = ['/','/','/','/','/','/','/']
row_C = ['/','/','/','/','/','/','/']


"""
def check(ctx,row):
    for row in rows:
        counter = 0
        for i in len(row - 1):
            if counter == 4:
                await ctx.send("we have a winner")
            elif row_A[i] == row_A[i+1]:
                counter += 1
        for i in range(6):
            if row_A[i] == row_B[i] and row_C[i] == row_D[i]:
                if row_E == row_D and row_E == row_F:
                    await ctx.send("we have a winner")
 """
def check_Crosses():
    global row_A
    global row_B
    global row_C
    if row_A[0] == row_A[1] and row_A[1] == row_A[2]:
        return row_A[1] 
    elif row_B[0] == row_B[1] and row_B[1] == row_B[2]:
        return row_B[1]
    elif row_C[0] == row_C[1] and row_C[1] == row_C[2]:
        return row_C[1]
    elif row_A[0] == row_B[0] and row_B[0] == row_C[0]:
        return row_A[0]
    elif row_A[1] == row_B[1] and row_B[1] == row_C[1]:
        return row_A[1]
    elif row_A[2] == row_B[2] and row_B[2] == row_C[2]:
        return row_A[2]
    elif row_A[0] == row_B[1] and row_B[1] == row_C[2]:
        return row_A[0]
    elif row_A[2] == row_B[1] and row_B[1] == row_C[0]:
        return row_A[2] 
    else:
        return False
    

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name ='Getting Bullied by Zomb', type=1))
    print("Bot is ready.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please send all required arguments')
    else:
        await ctx.send(error)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency *1000)} ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes defintely',
                'You may rely on it',
                'As I see it yes',
                'Most Likely',
                'outlook good',
                'yes',
                'Signs point to yes',
                'Reply Hazy, try again',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Do not count on it',
                'My sources say no',
                'Very doubtful',
                 'Ask Zonico',
                 'I am sleeping rn, ask me later',
                 'why did you ask me that',
                 'how am i supposed to know',
                 'Who do you think you are asking me that?',
                 'You tell me',
                 'Do not ask me, I am a ball',
                 'sure',
                 'whatever you say',
                 'I guess, maybe',
                 'meh',]
    
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def connectfour(ctx):
    await ctx.send('This feature is currently being developed')
    row_A = ['/','/','/','/','/','/','/']
    row_B = ['/','/','/','/','/','/','/']
    row_C = ['/','/','/','/','/','/','/']
    row_D = ['/','/','/','/','/','/','/']
    row_E = ['/','/','/','/','/','/','/']
    row_F = ['/','/','/','/','/','/','/']
    rows = [row_A,row_B,row_C,row_D,row_E,row_F]
    for row in rows:
        await ctx.send(row)


@client.command()
async def crosses(ctx, player : discord.Member):
    await ctx.send('Please note this feature is currently Alpha so there may be bugs \n if there are any bugs please contact @Zonico')
    global row_A
    global row_B
    global row_C
    row_A = ['','','']
    row_B = ['','','']
    row_C = ['','','']
    await ctx.send(row_A)
    await ctx.send(row_B)
    await ctx.send(row_C)
    global crosses_Game
    crosses_Game = True
    global player_Turn
    player_Turn = 1
    global player_One
    global player_Two
    player_One = ctx.message.author.name
    player = str(player)
    length = len(player)
    player_Two = player[:length-5]
    await ctx.send(f"it's @{player_One}'s Turn")
    


@client.command()
async def turn(ctx, position : int):
    correct = False
    global row_A
    global row_B
    global row_C
    global crosses_Game
    global player_Turn
    global player_One
    global player_Two
    if crosses_Game == True:
        if player_Turn == 1:
            if player_One == (ctx.message.author.name):
                player_Turn = 2
                if position == 1:
                    if row_A[0] != 'o':
                        if row_A[0] != 'x':
                            row_A[0] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                elif position == 2:
                    if row_A[1] != 'o':
                        if row_A[1] != 'x':
                            row_A[1] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1                
                elif position == 3:
                    if row_A[2] != 'o':
                        if row_A[2] != 'x':
                            row_A[2] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                elif position == 4:
                    if row_B[0] != 'o':
                        if row_B[0] != 'x':
                            row_B[0] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1 
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                elif position == 5:
                    if row_B[1] != 'o':
                        if row_B[1] != 'x':
                            row_B[1] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                
                elif position == 6:
                    if row_B[2] != 'o':
                        if row_B[2] != 'x':
                            row_B[2] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                elif position == 7:
                    if row_C[0] != 'o':
                        if row_C[0] != 'x':
                            row_C[0] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                elif position == 8:
                    if row_C[1] != 'o':
                        if row_C[1] != 'x':
                            row_C[1] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
                
                elif position == 9:
                    if row_C[2] != 'x':
                        if row_C[2] != 'o':
                            row_C[2] = 'x'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 1
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 1
            else:
                return None
                
                
        else:
            player_Turn = 1
            if player_Two == (ctx.message.author.name):
                correct = True
                await ctx.send(player_Two)
                if position == 1:
                    if row_A[0] != 'o':
                        if row_A[0] != 'x':
                            row_A[0] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                elif position == 2:
                    if row_A[1] != 'o':
                        if row_A[1] != 'x':
                            row_A[1] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2                
                elif position == 3:
                    if row_A[2] != 'o':
                        if row_A[2] != 'x':
                            row_A[2] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                elif position == 4:
                    if row_B[0] != 'o':
                        if row_B[0] != 'x':
                            row_B[0] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                elif position == 5:
                    if row_B[1] != 'o':
                        if row_B[1] != 'x':
                            row_B[1] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                
                elif position == 6:
                    if row_B[2] != 'o':
                        if row_B[2] != 'x':
                            row_B[2] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                elif position == 7:
                    if row_C[0] != 'o':
                        if row_C[0] != 'x':
                            row_C[0] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                elif position == 8:
                    if row_C[1] != 'o':
                        if row_C[1] != 'x':
                            row_C[1] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                
                elif position == 9:
                    if row_C[2] != 'x':
                        if row_C[2] != 'o':
                            row_C[2] = 'o'
                        else:
                            await ctx.send("sorry that position is already taken have another go")
                            player_Turn = 2
                    else:
                        await ctx.send("sorry that position is already taken have another go")
                        player_Turn = 2
                else:
                    player_Turn = 2
                    await ctx.send("Have another go but enter a value from 1-9 for the position you want it")
            else:
                return None
                player_Turn = 1
    await ctx.send(row_A)
    await ctx.send(row_B)
    await ctx.send(row_C)
    if check_Crosses() == 'x':
        await ctx.send(f"{player_One} has won!")
        crosses_Game = False
        return None
    elif check_Crosses() == 'o':
        await ctx.send(f"{player_Two} has won!")
        crosses_Game = False
        return None
    if player_Turn == 1:
        await ctx.send(f"It's now {player_One}'s go")
    else:
        await ctx.send(f"It's now {player_Two}'s go")

@client.command()
async def stop(ctx):
    global crosses_Game
    crosses_Game = False
    colourgame_Running = False
    await ctx.send("Game Stopped")

@client.command()
async def plzhelp(ctx):
    await ctx.send('My prefix is . \n8ball - to play magic 8 ball \ncrosses - to play noughts and crosses \nhelpcrosses - for help on how to play noughts and crosses \ncolourgame - to play colour guessing game \ncolourhelp - for help on how to play the colour guessing game\nconnectfour - WIP do not call')

@client.command()
async def helpcrosses(ctx):
    await ctx.send("To start type [.crosses @player], when its your turn type [.turn number], where number is the square you want to place your counter \n for example \n 1 2 3 \n 4 5 6 \n 7 8 9 \nTo end the game or if it's a draw type [.stop] to stop")

@client.command()
async def colourhelp(ctx):
    await ctx.send("To start type .colourgame, Then to start guess type [.colourguess colours], with colours being the 4 colours you with to guess, the colours are: \n r -red, y -yellow, g -green, b -blue, pi -pink, br -brown, bl -black, w - white, pu - purple, o -orange \nPLEASE NOTE you must type the colours in the format y,g,y,br with no spaces for example: \n .colourguess r,y,g,pr")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def colourgame(ctx):
    global colourgame_Running
    global colours
    global quesses
    guesses = 0
    colourgame_Running = True
    posible_colours = ['r','y','g','b','pi','br','bl','w','pu','o']
    colours = []
    for i in range(4):
        colours.append(posible_colours[random.randint(0,9)])
    print(colours)
    await ctx.send("I have a combation of 4 colours type [.colourguess colours] to guess")
        
@client.command()
async def colourguess(ctx, colour_guessed):
    global colourgame_Running
    global guesses
    global colours
    if colourgame_Running == True:
        if guesses < 10:
            correct = 0
            guess = colour_guessed.split(',')
            for i in range(4):
                if guess[i] == colours[i]:
                    correct +=1
            if correct == 4:
                await ctx.send("Well done, You have got them all right!")
                colourgame_Running = False
                pass
            guesses += 1
            await ctx.send(f"you have {correct} correct, and you have {(10 - guesses)} guesses left.")
        else:
            await ctx.send("You have run out of guesses")
            colourgame_Running = False
            await ctx.send(f"The correct answer was:\ncolours")
    else:
        await ctx.send("Please start the game by typing .colourgame")

@client.command()
async def admin(ctx):
    if ctx.message.author.name == 'Zonico':
        await ctx.send("Hello Master!")
    else:
        await ctx.send("Stop trying to hack me!!!")
    

keep_alive()
Token = os.environ.get("DISCORD_BOT_SECRET")
client.run(Token)

