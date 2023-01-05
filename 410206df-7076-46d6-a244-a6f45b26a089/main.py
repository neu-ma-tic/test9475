import discord
from discord.ext import commands
from keep_online import keep_online
import random

client = commands.Bot(command_prefix="$")
client.remove_command("help")

@client.event
async def on_ready():
  print("ready")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

helplist = "tictactoe",\
  "Hello",\
  "photo"


@client.command()
async def help(ctx):
  global helplist
  em = discord.Embed(title = "Help",description = "" )

  em.add_field(name="樂趣", value=helplist)
  await ctx.send(embed=em)
  
@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("是 <@" + str(player1.id) + "> 的回合.")
        elif num == 2:
            turn = player2
            await ctx.send("是 <@" + str(player2.id) + "> 的回合.")
    else:
        await ctx.send("一場比賽已經在進行中！在開始新的之前完成它.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " 勝利!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("這是一個平局!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("請務必選擇 1 到 9(含)之間的整數和未標記的圖塊.")
        else:
            await ctx.send("不是你的回合.")
    else:
        await ctx.send("請使用 $tictactoe 命令開始新遊戲.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("請在此命令中提及 2 名玩家.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("請務必提及玩家（即 <@688534433879556134> ).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("請輸入您要標記的位置.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("請確保輸入一個整數.")

@client.command()
async def shutdown(ctx):
  author = str(ctx.author)
  yep = "Kingsley1116#1292"
  global gameOver
  if author == yep:
    gameOver = True
    await ctx.send(f"game shutdown by {ctx.author}.")
  else:
    await ctx.send("you can't shutdown.")

@client.command()
async def Hello(ctx):
 await ctx.send(f"Hello! {ctx.author}")

@client.command()
async def ping(ctx):
  await ctx.send(f"round{client.latency*1000} [ms]")

@client.command()
async def photo(ctx):
  await ctx.send("https://www.cgi.com/sites/default/files/styles/hero_banner/public/space_astronaut.jpg?itok=k2oFRHrr")

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " 服務器信息",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="服務器主人", value=owner, inline=True)
    embed.add_field(name="服務器 ID", value=id, inline=True)
    embed.add_field(name="地區", value=region, inline=True)
    embed.add_field(name="人數", value=memberCount, inline=True)

    await ctx.send(embed=embed)
  
keep_online()
client.run("ODQ5MjQ1Mjg0MjIyODk0MTAw.YLYXTQ.XXfl27Z-GPfJo_bQeadoeARLrWs")