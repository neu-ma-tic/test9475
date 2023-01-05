import numpy as np, discord, asyncio, chess, chess.svg

from cairosvg import svg2png
from modules.Chess.AI import board, pieces, ai
from discord.ext import commands
from discord_components import Button
from random import choice
from io import BytesIO

class Games(commands.Cog, description='Games to play while you are bored'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def mchess(self, ctx: commands.Context, oponent: discord.Member):

      category = discord.utils.get(ctx.guild.categories, name='Chess')

      if not category:

        category = await ctx.guild.create_category(
          'Chess',
          position=2
        )

      channel = await ctx.guild.create_text_channel(
        ctx.author.display_name,
        category=category,
        overwrite={
          ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False),
          ctx.guild.me: discord.PermissionOverwrite(send_messages=True),
          ctx.author: discord.PermissionOverwrite(send_messages=True),
          oponent: discord.PermissionOverwrite(send_messages=True)
        }
      )

      await channel.send(f"{oponent.mention}{ctx.author.mention}")

      board = chess.Board()
      svg = chess.svg.board(board)
      byte = svg2png(bytestring=svg)
      message = await channel.send(file=discord.File(BytesIO(byte), filename="board.png"))
      turn = 0
      players = (oponent, ctx.author)
      colors = (discord.Colour.lighter_grey(), discord.Colour.dark_blue())
      embed = discord.Embed(
        title=f"{players[0].display_name} vs {players[1].display_name}",
        description=f"**{players[turn].display_name} TURN**",
        color=colors[turn]
      )
      emb = await channel.send(embed=embed)
      while not board.is_insufficient_material() or not board.is_stalemate() or not board.outcome():
        try:
          message = await self.bot.wait_for(
            'message',
            check=lambda x: x.channel == channel and x.author == players[turn] and x.content.startswith(".move"),
            timeout=600.0
          )
          msg = message.content[5:].replace(" ", "")
          if not (msg[0].isalpha() and msg[2].isalpha() and msg[1].isdigit() and msg[3].isdigit()):
            continue
          msg = "".join([i.lower() if i.isalpha() else i for i in msg])
          if not (ord("a") <= ord(msg[0]) <= ord("h")) or not (ord("a") <= ord(msg[2]) <= ord("h")):
            continue
          if not (1 <= int(msg[1]) <= 8) or not (1 <= int(msg[1]) <= 8):
            continue
          m = chess.Move.from_uci(msg)
          board.push(m)
          svg = chess.svg.board(board)
          byte = svg2png(bytestring=svg)
          await channel.send(file=discord.File(BytesIO(byte), filename="board.png"))
          turn = (turn + 1) % 2
          embed.color = colors[turn]
          embed.description = f"**{players[turn].display_name} TURN**"
          await channel.send(embed=embed)
        except:
          return await channel.send("Game ended")
      else:
        return await channel.send(f"{players[1 - turn]} WON")

      

    @commands.command()
    async def chess(self, ctx: commands.Context):

      category = discord.utils.get(ctx.guild.categories, name='Chess')

      if not category:

        category = await ctx.guild.create_category(
          'Chess',
          position=2
        )

      channel = await ctx.guild.create_text_channel(
        ctx.author.display_name,
        category=category,
        overwrite={
          ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False),
          ctx.guild.me: discord.PermissionOverwrite(send_messages=True),
          ctx.author: discord.PermissionOverwrite(send_messages=True),
        }
      )

      # Returns a move object based on the users input. Does not check if the move is valid.
      async def get_user_move():

          try:
            message = await self.bot.wait_for(
                'message',
                check=lambda x: x.channel == channel and x.author == ctx.author,
                timeout=1800.0
              )

          except asyncio.TimeoutError as e:
            await channel.send("Time's out")
            raise e

          if not message.content.startswith(".move"):
            await channel.send("Please use correct syntax")
            await message.delete(delay=2.0)
            return await get_user_move()

          move_str = message.content[5:]
          move_str = move_str.replace(" ", "")

          await message.delete(delay=2.0)

          try:
              xfrom = await letter_to_xpos(move_str[0:1])
              yfrom = 8 - int(move_str[1:2]) # The board is drawn "upside down", so flip the y coordinate.
              xto = await letter_to_xpos(move_str[2:3])
              yto = 8 - int(move_str[3:4]) # The board is drawn "upside down", so flip the y coordinate.
              return ai.Move(xfrom, yfrom, xto, yto, False)
          except ValueError:
              await channel.send("Invalid format. Example: .move A2 A4", delete_after=2.0)
              return await get_user_move()

      # Returns a valid move based on the users input.
      async def get_valid_user_move(board):
          while True:
              move = await get_user_move()
              possible_moves = board.get_possible_moves(pieces.Piece.WHITE)
              # No possible moves
              if (not possible_moves):
                  return 0

              for possible_move in possible_moves:
                  if (move.equals(possible_move)):
                      move.castling_move = possible_move.castling_move
                      return move

              
              await channel.send("Invalid move.", delete_after=2.0)

      # Converts a letter (A-H) to the x position on the chess board.
      async def letter_to_xpos(letter):
          letter = letter.upper()
          try:
            if 65 <= (ascii := ord(letter)) <= 72:
                return ascii - 65

            await channel.send("Invalid letter.", delete_after=2.0)
          except:
            await channel.send("Not a valid moves")

      message = await channel.send(ctx.author.mention)
      await channel.send('Use ".move <first> <second>" to move\nEg: .move a2 a4')

      await asyncio.sleep(4.0)

      game = board.Board.new()
      await message.edit(content=str(game)) 

      while True:
          move = await get_valid_user_move(game)
          if (move == 0):
              if (game.is_check(pieces.Piece.WHITE)):
                  return await channel.send("Checkmate. Black Wins.")
              else:
                  return await channel.send("Stalemate.")

          game.perform_move(move)

          await channel.send("User move: " + move.to_string(), delete_after=2.0)
          await message.edit(content=str(game))

          await asyncio.sleep(2.0)

          ai_move = ai.AI.get_ai_move(game, [])
          if (ai_move == 0):
              if (game.is_check(pieces.Piece.BLACK)):
                  return await channel("Checkmate. White wins.")
              else:
                  return await channel("Stalemate.")

          game.perform_move(ai_move)
          await channel.send("AI move: " + ai_move.to_string(), delete_after=2.0)
          await message.edit(content=str(game))

    @commands.command()
    async def roulette(self, ctx: commands.Context):
      message = await ctx.send('**React to this message**')
      await message.add_reaction('<:flooppa:866343842511716402>')
      role = discord.utils.find(
        lambda r: r.permissions.send_messages == False,
        ctx.guild.roles
      )
      await asyncio.sleep(10.0)

      reactions = discord.utils.get(
        self.bot.cached_messages,
        id=message.id
      ).reactions[0]

      players = await reactions.users().flatten()
      players.remove(self.bot.user)
      hit = choice(players)

      member = await ctx.guild.fetch_member(hit.id)
      roles = member.roles[:]

      await ctx.send(f'{member.display_name} has been hit')
  
      await member.edit(
        roles = [role]
      )
      await asyncio.sleep(10.0)
      await member.edit(
        roles = roles
      )

    @commands.command()
    async def roulette(self, ctx: commands.Context):
      message = await ctx.send('**React to this message**')
      await message.add_reaction('<:flooppa:866343842511716402>')
      role = discord.utils.find(
        lambda r: r.permissions.send_messages == False,
        ctx.guild.roles
      )
      await asyncio.sleep(10.0)

      reactions = discord.utils.get(
        self.bot.cached_messages,
        id=message.id
      ).reactions[0]

      players = await reactions.users().flatten()
      players.remove(self.bot.user)
      hit = choice(players)

      member = await ctx.guild.fetch_member(hit.id)
      roles = member.roles[:]

      await ctx.send(f'{member.display_name} has been hit')
  
      await member.edit(
        roles = [role]
      )
      await asyncio.sleep(10.0)
      await member.edit(
        roles = roles
      )      

    @commands.command(description='Under construction')
    async def sokoban(self, ctx: commands.Context):
      from modules.Sokoban.Level import level

      player = '😳'
      target = '🟥'
      wall = '🟫'
      box = '❎'
      space = '⬛'
      box_on_target = '☑'
      entity = [space, wall, player, target, box, box_on_target]
      randstage = list(range(len(level)))
      random = None

      moves = [
        [
          Button(style=1, id='UpLeft', emoji='↖'),
          Button(style=1, id='Up', emoji='⬆'),
          Button(style=1, id='UpRight', emoji='↗')
        ],
        [
          Button(style=1, id='Left', emoji='⬅'),
          Button(emoji='😶', disabled=True),
          Button(style=1, id='Right', emoji='➡')
        ],
        [
          Button(style=1, id='DownLeft', emoji='↙'),
          Button(style=1, id='Down', emoji='⬇'),
          Button(style=1, id='DownRight', emoji='↘')
        ],
        [
          Button(style=4, id='Stop', emoji='⛔'),
          Button(style=2, id='Restart', emoji='🔄'),
          Button(style=3, id='Next', emoji='⏩', disabled=True)
        ]
      ]

      board = np.array(
        [
          [0, 0, 1, 1, 1, 0, 0, 0],
          [0, 0, 1, 3, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 1, 1, 1],
          [1, 1, 1, 4, 0, 4, 3, 1],
          [1, 3, 0, 4, 2, 1, 1, 1],
          [1, 1, 1, 1, 4, 1, 0, 0],
          [0, 0, 0, 1, 3, 1, 0, 0],
          [0, 0, 0, 1, 1, 1, 0, 0],
        ], dtype='i'
      )

      posX, posY = 4, 4
      targetpos = {(1, 3), (3, 6), (4, 1), (6, 4)}
      stage = 1
      
      def get_content():
        content = f'***Level {stage}***\n'
        for i in board:
          content += ''.join(list(map(lambda x: entity[x], i))) + '\n'
        return content

      message = await ctx.send(get_content(), components = moves)
      

      def game_hove(x, y):
        nonlocal posX, posY
        X, Y = posX + x, posY + y
        if board[X, Y] == 1:
          return
        if board[X, Y] == 4:
          if board[X + x, Y + y] in {1, 4, 5}:
            return
          elif board[X + x, Y + y] == 3:
            board[X + x, Y + y] = 5
            board[X, Y] = 2
            board[posX, posY] = 0 if (posX, posY) not in targetpos else 3
            posX, posY = X, Y
            return
          else:
            board[X + x, Y + y] = 4
            board[X, Y] = 2
            board[posX, posY] = 0 if (posX, posY) not in targetpos else 3
            posX, posY = X, Y
            return
        if board[X, Y] == 5:
          if board[X + x, Y + y] in {1, 4, 5}:
            return
          elif board[X + x, Y + y] == 3:
            board[X + x, Y + y] = 5
            board[X, Y] = 2
            board[posX, posY] = 0 if (posX, posY) not in targetpos else 3
            posX, posY = X, Y
            return
          else:
            board[X + x, Y + y] = 4
            board[X, Y] = 2
            board[posX, posY] = 0 if (posX, posY) not in targetpos else 3
            posX, posY = X, Y
            return
        board[X, Y] = 2
        board[posX, posY] = 0 if (posX, posY) not in targetpos else 3
        posX, posY = X, Y
        return

      def game_diag(x, y):
        nonlocal posX, posY
        X, Y = posX + x, posY + y
        if board[X, Y] in {1, 4, 5}:
          return
        if board[X, posY] in {1, 4, 5} and board[posX, Y] in {1, 4, 5}:
          return
        board[X, Y] = 2
        board[posX, posY] = 0 if (posX, posY) not in targetpos else 3
        posX, posY = X, Y
        return

      def check_win():
        for pos in targetpos:
          x, y = pos
          if board[x, y] != 5:
            return False
        return True

      while True:
        try:
          interaction = await self.bot.wait_for(
            'button_click',
            check = lambda x: x.message == message and x.user == ctx.author,
            timeout = 120.0
          )
          id = interaction.component.id
          if id == 'Stop':
            return await interaction.respond(
              type=7,
              components=[]
            )
          if id == 'Restart':
            if stage == 1:
              board = np.array(
                [
                  [0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 1, 3, 1, 0, 0, 0],
                  [0, 0, 1, 0, 1, 1, 1, 1],
                  [1, 1, 1, 4, 0, 4, 3, 1],
                  [1, 3, 0, 4, 2, 1, 1, 1],
                  [1, 1, 1, 1, 4, 1, 0, 0],
                  [0, 0, 0, 1, 3, 1, 0, 0],
                  [0, 0, 0, 1, 1, 1, 0, 0],
                ], dtype='i'
              )
              posX, posY = 4, 4
              targetpos = {(1, 3), (3, 6), (4, 1), (6, 4)}

            else:
              board = np.copy(level[random][0])
              targetpos = level[random][1]
              posX, posY = level[random][2]

            await interaction.respond(
              type=7,
              content=get_content(),
              components=moves
            )
            continue
          if id == 'Next':
            stage += 1
            random = choice(randstage)
            board = np.copy(level[random][0])
            targetpos = level[random][1]
            posX, posY = level[random][2]
            moves[3][2].disabled = True
            randstage.remove(random)
            await interaction.respond(
              type=7,
              content=get_content(),
              components=moves
            )
            continue
          if id == 'Left':
            game_hove(0, -1)
          if id == 'Right':
            game_hove(0, 1)
          if id == 'Up':
            game_hove(-1, 0)
          if id == 'Down':
            game_hove(1, 0)
          if id == 'UpLeft':
            game_diag(-1, -1)
          if id == 'UpRight':
            game_diag(-1, 1)
          if id == 'DownLeft':
            game_diag(1, -1)
          if id == 'DownRight':
            game_diag(1, 1)

          await interaction.respond(
            type=7,
            content=get_content(),
            components = moves
          )

          if check_win():
            if stage == len(level) + 1:
              await asyncio.sleep(1.0)
              return await message.edit(
                type=7,
                content=get_content() + 'You win',
                components = []
              )
            else:
              moves[3][2].disabled = False
              await message.edit(
                components = moves
              )

        except asyncio.TimeoutError:
          return await message.edit(components=[])
        

    @commands.command(aliases=['tic', 'tac', 'toe'], description='Play a game of tic tac toe', help='<tictactoe | tic | tac | toe> <member mention | member id>')
    async def tictactoe(self, ctx: commands.Context, member: discord.Member):
      to_member = commands.MemberConverter()
      try:
        player_2 = await to_member.convert(ctx, str(member))
        player_1 = ctx.author
        message = await ctx.send(
          embed=discord.Embed(
            title=f"{player_1.display_name} has challenged {player_2.display_name} to a tic tac toe battle",
            description=f"{player_2.mention} Do you accept the challenge?",
            color=discord.Colour.lighter_grey()
          ),
          components=[[
            Button(
              label="I accept",
              style=3
            ),
            Button(
              label='I refuse',
              style=4
            )
          ]]
        )
        try:
          interaction = await self.bot.wait_for(
            'button_click',
            check=lambda x: x.user == player_2 and x.message == message and x.channel == ctx.channel,
            timeout=15.0
          )
          decision = interaction.component.label
          if decision == 'I refuse':
            return await interaction.respond(
              type=7,
              embed=discord.Embed(
                title=f'{player_2.display_name} has refused to play',
                description='What a loser',
                color=discord.Colour.darker_grey()
              ),
              components=[]
            )
          grid = [
            [
              Button(label='_', id='00'),
              Button(label='_', id='01'),
              Button(label='_', id='02')
            ],
            [
              Button(label='_', id='10'),
              Button(label='_', id='11'),
              Button(label='_', id='12')
            ],
            [
              Button(label='_', id='20'),
              Button(label='_', id='21'),
              Button(label='_', id='22')
            ]
          ]
          turn = 1
          green, red = discord.Colour.green(), discord.Colour.red()
          players = [(player_1, 'O', 3, green), (player_2, 'X', 4, red)]
          embed = discord.Embed(
                    title=f'{player_1.display_name} vs {player_2.display_name}',
                    description=f'**Turn:** {players[turn % 2][0].display_name}',
                    color=players[turn%2][3]
                  )
          embed.set_footer(text='1/9')
          await interaction.respond(
            type=7,
            embed=embed,
            components=grid
          )
          board = [[None for _ in range(3)] for _ in range(3)]
          def check():
            if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != None:
              return True
            if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != None:
              return True
            if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != None:
              return True
            if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != None:
              return True
            if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != None:
              return True
            if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != None:
              return True
            if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != None:
              return True
            if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != None:
              return True
            return False
          while turn <= 9:
            try:
              move = await self.bot.wait_for(
                'button_click',
                check=lambda x: x.message == message and x.user == players[turn%2][0] and x.channel == ctx.channel,
                timeout=60.0
              )
              i, j = int(move.component.id[0]), int(move.component.id[1])
              board[i][j] = turn % 2
              grid[i][j] = Button(label=players[turn%2][1], style=players[turn%2][2], disabled=True)


              if turn >= 5 and check():
                embed.title = f'{players[turn%2][0].display_name} has won'
                embed.description = f'GGWP {players[1 - (turn%2)][0].display_name}'
                embed.set_footer(text=f'{turn}/9')
                return await move.respond(
                  type=7,
                  embed=embed,
                  components=grid
                )

              turn += 1
              embed.description = f'**Turn:** {players[turn%2][0].display_name}'
              embed.color = players[turn%2][3]
              embed.set_footer(text=f'{turn}/9')
              await move.respond(
                type=7,
                embed=embed,
                components=grid
              )

            except asyncio.TimeoutError:
              return await message.edit(
                embed=discord.Embed(
                  title='Game has ended',
                  description=f'{player_2.display_name} took too much time to make a move',
                  color=discord.Colour.darker_grey()
                ),
                components=[]
                )
          else:
            return await message.edit(
              embed=discord.Embed(
                title=f'{player_1.display_name} and {player_2.display_name} has tied',
                description='lmao 2 losers',
                color=discord.Colour.blurple()
              ),
              components=grid
            )
        except asyncio.TimeoutError:
          return await message.edit(
            embed=discord.Embed(
              title='Invitation has ended',
              description=f'{player_2.display_name} took too much time to respond',
              color=discord.Colour.darker_grey()
              ),
            components=[]
            )
      except commands.BadArgument:
        return await ctx.send('Not a valid member')
      except commands.MemberNotFound:
        return await ctx.send('Member not found')


    @commands.command(aliases=['tic5', 'tac5', 'toe5'], description='Play a game of tic tac toe', help='<tictactoe5 | tic5 | tac5 | toe5> <member mention | member id>')
    async def tictactoe5(self, ctx: commands.Context, member: discord.Member):
      to_member = commands.MemberConverter()
      try:
        player_2 = await to_member.convert(ctx, str(member))
        player_1 = ctx.author
        message = await ctx.send(
          embed=discord.Embed(
            title=f"{player_1.display_name} has challenged {player_2.display_name} to a tic tac toe 5x5 battle",
            description=f"{player_2.mention} Do you accept the challenge?",
            color=discord.Colour.lighter_grey()
          ),
          components=[[
            Button(
              label="I accept",
              style=3
            ),
            Button(
              label='I refuse',
              style=4
            )
          ]]
        )
        try:
          interaction = await self.bot.wait_for(
            'button_click',
            check=lambda x: x.user == player_2 and x.message == message and x.channel == ctx.channel,
            timeout=15.0
          )
          decision = interaction.component.label
          if decision == 'I refuse':
            return await interaction.respond(
              type=7,
              embed=discord.Embed(
                title=f'{player_2.display_name} has refused to play',
                description='What a loser',
                color=discord.Colour.darker_grey()
              ),
              components=[]
            )
          grid = [
            [
              Button(label='_', id='00'),
              Button(label='_', id='01'),
              Button(label='_', id='02'),
              Button(label='_', id='03'),
              Button(label='_', id='04'),
            ],
            [
              Button(label='_', id='10'),
              Button(label='_', id='11'),
              Button(label='_', id='12'),
              Button(label='_', id='13'),
              Button(label='_', id='14'),
            ],
            [
              Button(label='_', id='20'),
              Button(label='_', id='21'),
              Button(label='_', id='22'),
              Button(label='_', id='23'),
              Button(label='_', id='24'),
            ],
            [
              Button(label='_', id='30'),
              Button(label='_', id='31'),
              Button(label='_', id='32'),
              Button(label='_', id='33'),
              Button(label='_', id='34'),
            ],
            [
              Button(label='_', id='40'),
              Button(label='_', id='41'),
              Button(label='_', id='42'),
              Button(label='_', id='43'),
              Button(label='_', id='44'),
            ],
          ]
          turn = 1
          green, red = discord.Colour.green(), discord.Colour.red()
          players = [(player_1, 'O', 3, green), (player_2, 'X', 4, red)]
          embed = discord.Embed(
                    title=f'{player_1.display_name} vs {player_2.display_name}',
                    description=f'**Turn:** {players[turn % 2][0].display_name}',
                    color=players[turn%2][3]
                  )
          embed.set_footer(text='1/25')
          await interaction.respond(
            type=7,
            embed=embed,
            components=grid
          )
          board = np.array([[None for _ in range(5)] for _ in range(5)])
          def check():
            for i in range(5):
              if board[i, 0] == board[i, 1] and board[i, 1] == board[i, 2] and board[i, 2] == board[i, 3] and board[i, 3] != None:
                return True
              if board[i, 1] == board[i, 2] and board[i, 2] == board[i, 3] and board[i, 3] == board[i, 4] and board[i, 4] != None:
                return True
              if board[0, i] == board[1, i] and board[1, i] == board[2, i] and board[2, i] == board[3, i] and board[3, i] != None:
                return True
              if board[1, i] == board[2, i] and board[2, i] == board[3, i] and board[3, i] == board[4, i] and board[4, i] != None:
                return True
            if board[0, 0] == board[1, 1] and board[1, 1] == board[2, 2] and board [2, 2] == board[3, 3] and board[3, 3] != None:
              return True
            if board[1, 1] == board[2, 2] and board[2, 2] == board[3, 3] and board [3, 3] == board[4, 4] and board[4, 4] != None:
              return True
            if board[0, 1] == board[1, 2] and board[1, 2] == board[2, 3] and board [2, 3] == board[3, 4] and board[3, 4] != None:
              return True
            if board[1, 0] == board[2, 1] and board[2, 1] == board[3, 2] and board [3, 2] == board[4, 3] and board[4, 3] != None:
              return True
            if board[0, 4] == board[1, 3] and board[1, 3] == board[2, 2] and board[2, 2] == board[3, 1] and board[3, 1] != None:
              return True
            if board[1, 3] == board[2, 2] and board[2, 2] == board[3, 1] and board[3, 1] == board[4, 0] and board[4, 0] != None:
              return True
            if board[0, 3] == board[1, 2] and board[1, 2] == board[2, 1] and board[2, 1] == board[3, 0] and board[3, 0] != None:
              return True
            if board[1, 4] == board[2, 3] and board[2, 3] == board[3, 2] and board[3, 2] == board[4, 1] and board[4, 1] != None:
              return True
            return False
          while turn <= 25:
            try:
              move = await self.bot.wait_for(
                'button_click',
                check=lambda x: x.message == message and x.user == players[turn%2][0] and x.channel == ctx.channel,
                timeout=60.0
              )
              i, j = int(move.component.id[0]), int(move.component.id[1])
              board[i][j] = turn % 2
              grid[i][j] = Button(label=players[turn%2][1], style=players[turn%2][2], disabled=True)


              if turn >= 7 and check():
                embed.title = f'{players[turn%2][0].display_name} has won'
                embed.description = f'GGWP {players[1 - (turn%2)][0].display_name}'
                embed.set_footer(text=f'{turn}/25')
                return await move.respond(
                  type=7,
                  embed=embed,
                  components=grid
                )

              turn += 1
              embed.description = f'**Turn:** {players[turn%2][0].display_name}'
              embed.color = players[turn%2][3]
              embed.set_footer(text=f'{turn}/25')
              await move.respond(
                type=7,
                embed=embed,
                components=grid
              )

            except asyncio.TimeoutError:
              return await message.edit(
                embed=discord.Embed(
                  title='Game has ended',
                  description=f'{player_2.display_name} took too much time to make a move',
                  color=discord.Colour.darker_grey()
                ),
                components=[]
                )
          else:
            return await message.edit(
              embed=discord.Embed(
                title=f'{player_1.display_name} and {player_2.display_name} has tied',
                description='lmao 2 losers',
                color=discord.Colour.blurple()
              ),
              components=grid
            )
        except asyncio.TimeoutError:
          return await message.edit(
            embed=discord.Embed(
              title='Invitation has ended',
              description=f'{player_2.display_name} took too much time to respond',
              color=discord.Colour.darker_grey()
              ),
            components=[]
            )
      except commands.BadArgument:
        return await ctx.send('Not a valid member')
      except commands.MemberNotFound:
        return await ctx.send('Member not found')


    @commands.command(description='Play a game of Rock-Paper-Scissors with bot', help='rps')
    async def rps(self, ctx: commands.Context, member: discord.Member = None):
      def result(c1: str, c2: str):
          if c1 == c2:
            return 0
          if c1 == 'Rock':
            if c2 == 'Paper':
              return 2
          if c1 == 'Paper':
            if c2 == 'Scissors':
              return 2
          if c1 =='Scissors':
            if c2 == 'Rock':
              return 2
          return 1
      choices = [[
          Button(label = 'Rock', style = 4, id='0'),
          Button(label = 'Paper', style = 3, id='1'),
          Button(label = 'Scissors', style = 1, id='2')
        ]]
      if not member:
        bot_choice = choice(('Rock', 'Paper', 'Scissors'))
        player = ctx.author.display_name

        msg = await ctx.send(f"**{player}'s Rock Paper Scissor game**\nMake your move", components = choices)
        
        def check(res):
          return res.user == ctx.author and res.channel == ctx.channel and res.message == msg

        try:
          res = await self.bot.wait_for('button_click', check = check, timeout = 15)
          player_choice = res.component.label
          index = int(res.component.id)
          style = res.component.style
          choices[0][index] = Button(
            style=style,
            label=player_choice,
            disabled=True
          )

          Win = f'{player} has ***WON***\tCongrats\nBot chose **{bot_choice}**\nYou chose **{player_choice}**'
          Lose = f'{player} has ***LOST***\tBetter be lucky next time\nBot chose **{bot_choice}**\nYou chose **{player_choice}**'
          Tie = f'{player} has ***TIED***\tYou almost did it\nBot chose **{bot_choice}**\nYou chose **{player_choice}**'

          ans = result(player_choice, bot_choice)
          if ans == 0:
            return await res.respond(
              type=7,
              content = Tie,
              components = choices
            )
          if ans == 1:
            return await res.respond(
              type=7,
              content = Win,
              components = choices
            )
          if ans == 2:
            return await res.respond(
              type=7,
              content = Lose,
              components = choices
            )
        except asyncio.TimeoutError:
          return await msg.edit(content="Time's out\nBetter be fast next time", components = [])
      else:
        to_member = commands.MemberConverter()
        try:
          player_2 = await to_member.convert(ctx, str(member))
          player_1 = ctx.author
          message = await ctx.send(
            embed=discord.Embed(
              title=f"{player_1.display_name} has challenged {player_2.display_name} to a Rock Paper Scissors battle",
              description=f"{player_2.mention} Do you accept the challenge?",
              color=discord.Colour.lighter_grey()
            ),
            components=[[
              Button(
                label="I accept",
                style=3
              ),
              Button(
                label='I refuse',
                style=4
              )
            ]]
          )
          try:
            interaction = await self.bot.wait_for(
              'button_click',
              check=lambda x: x.user == player_2 and x.message == message and x.channel == ctx.channel,
              timeout=15.0
            )
            decision = interaction.component.label
            if decision == 'I refuse':
              return await interaction.respond(
                type=7,
                embed=discord.Embed(
                  title=f'{player_2.display_name} has refused to play',
                  description='What a loser',
                  color=discord.Colour.darker_grey()
                ),
                components=[]
              )
            await interaction.respond(
              type=7,
              embed=discord.Embed(
                title=f'The fight between {player_1.display_name} and {player_2.display_name} has begun',
                description=f'Amen'
              ),
              components = choices
            )
            try:
              d1, d2 = await asyncio.wait(
                [
                  self.bot.wait_for(
                    'button_click',
                    check=lambda x: x.message == message and x.user == player_1,
                    timeout = 15.0
                  ),
                  self.bot.wait_for(
                    'button_click',
                    check=lambda x: x.message == message and x.user == player_2,
                    timeout=15.0
                  )
                ]
              )
              l1, l2 = d1.component.label, d2.component.label
              if l1 == l2:
                return ctx.send('Tie')
              if l1 == 'Rock' and l2 == 'Scissors':
                return ctx.send(f'{player_1.display_name} win')
              if l1 == 'Scissors' and l2 == 'Paper':
                return ctx.send(f'{player_1.display_name} win')
              if l1 == 'Paper' and l2 == 'Rock':
                return ctx.send(f'{player_1.display_name} win')
              return ctx.send(f'{player_2.display_name} win')
            except:
              return await interaction.respond(
                type=7,
                embed=discord.Embed(
                  title='The war is over',
                  description=f'{player_2.display_name} did not make a move'
                )
              )
          except asyncio.TimeoutError:
            return await message.edit(
              embed=discord.Embed(
                title='Invitation has ended',
                description=f'{player_2.display_name} took too much time to respond',
                color=discord.Colour.darker_grey()
                ),
              components=[]
              )
        except commands.MemberNotFound:
          return await ctx.send('Member not found')
        except commands.BadArgument:
          return await ctx.send('Not a valid member')

    @commands.command(description='Play a game of hangman', help='hangman')
    async def hangman(self, ctx: commands.Context):
      with open('data_file/wordbank.txt', 'r') as f:
          word = choice(f.read().split(', '))
          states = ['''
        _________
        |       |
        |
        |
        |
        |
        |
       _|_
      |___|
      ''',
      '''
        _________
        |       |
        |      (_)
        |
        |
        |
        |
       _|_
      |___|
      ''',
      '''
        _________
        |       |
        |      (_)
        |       |
        |       |
        |
        |
       _|_
      |___|
      ''',
      '''
        _________
        |       |
        |      (_)
        |      \|
        |       |
        |
        |
       _|_
      |___|
      ''',
      '''
        _________
        |       |
        |      (_)
        |      \|/
        |       |
        |
        |
       _|_
      |___|
      ''',
      '''
        _________
        |       |
        |      (_)
        |      \|/
        |       |
        |      /
        |
       _|_
      |___|
      ''',
      '''
        _________
        |       |
        |      (_)
        |      \|/
        |       |
        |      / \\
        |
       _|_
      |___|
      '''
  ]
          print(word)
          health = 6
          guesses = []
          blanks = ['_' for i in range(len(word))]
          embed = discord.Embed(
            title=f"{ctx.author.display_name}'s Hangman game",
            description='''
            ```
    {}
    {} ({} words)
    Guesses: 
            ```
            '''.format(states[- health - 1], ''.join(blanks), len(word))
          )
          message = await ctx.send(embed=embed)
          while health > 0:
            try:
              msg = await self.bot.wait_for(
                'message',
                check=lambda m: m.author == ctx.author and m.content.startswith('.') and m.channel == ctx.channel,
                timeout=100
              )
              ans = msg.content[1:].strip()
              if len(ans) > 1:
                if ans == word:
                  await msg.delete()
                  emb = discord.Embed(
                    title = f'{ctx.author.display_name} has won the hangman game',
                    description='''
                    ```
    You have won!! Congrats
    {}
    The answer is: {} 
    Guesses: {}
                    ```
                    '''.format(states[-health-1], word, ' '.join(guesses))
                  )
                  return await message.edit(embed=emb)
                else:
                  await ctx.send('Not correct answer', delete_after=2.0)
              elif len(ans) == 1:
                if ord('a') <= ord(ans) <= ord('z'):
                  if ans in guesses:
                    await ctx.send('Already guesses', delete_after=2.0)
                    await msg.delete()
                    continue
                  if ans in word:
                    guesses.append(ans)
                    for i in range(len(word)):
                      if word[i] == ans:
                        blanks[i] = ans
                  else:
                    health -= 1
                    guesses.append(ans)
                else:
                  await ctx.send('Not a valid answer', delete_after=2.0)
                  continue
              await msg.delete()
              if '_' not in blanks:
                emb = discord.Embed(
                  title = f'{ctx.author.display_name} has won the hangman game',
                  description='''
                  ```
    You have won!! Congrats
    {}
    The answer is: {} 
    Guesses: {}
                  ```
                  '''.format(states[-health-1], word, ' '.join(guesses))
                )
                return await message.edit(embed=emb)
              embed = discord.Embed(
                title=f"{ctx.author.display_name}'s Hangman game",
                description='''
                ```
    {}
    {} ({} words)
    Guesses: {}
                ```
                '''.format(states[- health - 1], ''.join(blanks), len(word), ' '.join(guesses))
              )
              await message.edit(embed=embed)
            except:
              e = discord.Embed(
                title=f"{ctx.author.display_name}'s hangman game has ended",
                description='No one has been playing me so i went adios'
              )
              return await message.edit(embed=e)
          else:
            emb = discord.Embed(
              title = f'{ctx.author.display_name} has won the hangman game',
              description='''
              ```
  You have lost!! Big F
  {}
  The answer is: {} 
  Guesses: {}
              ```
              '''.format(states[-health-1], word, ' '.join(guesses))
            )
            return await message.edit(embed=emb)
    
    @commands.command(description='Under Construction', help='None')
    async def tophangman(self, ctx: commands.Context):
      return await ctx.send('Under Constructing')