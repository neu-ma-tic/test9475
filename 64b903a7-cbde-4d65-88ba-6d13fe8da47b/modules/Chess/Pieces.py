import numpy as np
import asyncio

class Piece:

  BLACK = 'B'
  WHITE = 'W'

  def __init__(self, x, y, color, file_path):
    self.x = x
    self.y = y
    self.color = color
    self.file_path = file_path


  async def get_diagonal_moves(self, board):

    moves = set()

    for i in range(1, 8):

      if board[self.x + i][self.y + i] and board[self.x + i][self.y + i].color == self.color:
        break
      
      if self.x + i > 7 or self.y + i > 7:
        break

      moves.add((self.x + i, self.y + i))

      if board[self.x + i][self.y + i]:
        break

    for i in range(1, 8):

      if board[self.x - i][self.y - i] and board[self.x - i][self.y - i].color == self.color:
        break

      if self.x - i < 0 or self.y - i < 0:
        break

      moves.add((self.x - i, self.y - i))

      if board[self.x - i][self.y - i]:
        break

    for i in range(1, 8):

      if board[self.x - i][self.y + i] and board[self.x - i][self.y + i].color == self.color:
        break

      if self.x - i < 0 or self.y + i > 7:
        break

      moves.add((self.x - i, self.y + i))

      if board[self.x - i][self.y + i]:
        break

    for i in range(1, 8):

      if board[self.x + i][self.y - i] and board[self.x + i][self.y - i].color == self.color:
        break

      if self.x + i > 7 or self.y - i < 0:
        break

      moves.add((self.x + i, self.y - i))

      if board[self.x + i][self.y - i]:
        break

    return moves

  async def get_horizontal_vertical_moves(self, board):

    moves = set()

    for i in range(1, 8):
      
      if board[self.x + i][self.y] and board[self.x + i][self.y].color == self.color:
        break

      if self.x + i > 7:
        break

      moves.add((self.x + i, self.y))

      if board[self.x + i][self.y]:
        break

    for i in range(1, 8):

      if board[self.x - i][self.y] and board[self.x - i][self.y].color == self.color:
        break
      
      if self.x - i < 0:
        break

      moves.add((self.x - i, self.y))

      if board[self.x - i][self.y]:
        break

    for i in range(1, 8):

      if board[self.x][self.y + i] and board[self.x][self.y + i].color == self.color:
        break

      if self.y + i > 7:
        break

      moves.add((self.x, self.y + i))

      if board[self.x][self.y + i]:
        break

    for i in range(1, 8):

      if board[self.x][self.y - i] and board[self.x][self.y - i].color == self.color:
        break

      if self.y - i < 0:
        break

      moves.add((self.x, self.y - i))

      if board[self.x][self.y - i]:
        break

    return moves


class Rook(Piece):

  def __init__(self, x, y, color, file_path):
    super(Piece, self).__init__(x, y, color, file_path)
    self.point = 5

  async def get_possible_moves(self, board):
    return await self.get_horizontal_vertical_moves(board)

class Knight(Piece):

  def __init__(self, x, y, color, file_path):
    super(Piece, self).__init__(x, y, color, file_path)
    self.point = 3

  async def get_possible_moves(self, board):
    
    moves = set()

    if self.x + 1 <= 7:

      if self.y + 2 <= 7:
        
        if board[self.x + 1][self.y + 2] is None or board[self.x + 1][self.y + 2].color != self.color:
          moves.add((self.x + 1, self.y + 2))

      if self.y - 2 >= 0:

        if board[self.x + 1][self.y - 2] is None or board[self.x + 1][self.y - 2].color != self.color:
          moves.add((self.x + 1, self.y - 2))

    if self.x - 1 >= 0:
      
      if self.y + 2 <= 7:

        if board[self.x - 1][self.y + 2] is None or board[self.x - 1][self.y + 2].color != self.color:
          moves.add((self.x - 1, self.y + 2))

      if self.y - 2 >= 0:

        if board[self.x - 1][self.y - 2] is None or board[self.x - 1][self.y - 2].color != self.color:
          moves.add((self.x - 1, self.y - 2))

    if self.x + 2 <= 7:
      
      if self.y + 1 <= 7:

        if board[self.x + 2][self.y + 1] is None or board[self.x + 2][self.y + 1].color != self.color:
          moves.add((self.x + 2, self.y + 1))

      if self.y - 1 >= 0:

        if board[self.x + 2][self.y - 1] is None or board[self.x + 2][self.y - 1].color != self.color:
          moves.add((self.x + 2, self.y - 1))
    
    if self.x - 2 >= 0:
      
      if self.y + 1 <= 7:

        if board[self.x - 2][self.y + 1] is None or board[self.x - 2][self.y + 1].color != self.color:
          moves.add((self.x - 2, self.y + 1))

      if self.y - 1 >= 0:

        if board[self.x - 2][self.y - 1] is None or board[self.x - 2][self.y - 1].color != self.color:
          moves.add((self.x - 2, self.y - 1))

    return moves


class Bishop(Piece):

  def __init__(self, x, y, color, file_path):
    super(Piece, self).__init__(x, y, color, file_path)
    self.point = 3

  async def get_possible_moves(self, board):
    return await self.get_diagonal_moves(board)



class Queen(Piece):

  def __init__(self, x, y, color, file_path):
    super(Piece, self).__init__(x, y, color, file_path)
    self.point = 9

  async def get_possible_moves(self, board):
    moves = set()

    moves.update(await self.get_diagonal_moves(board))
    moves.update(await self.get_horizontal_vertical_moves(board))

    return moves

class King(Piece):

  def __init__(self, x, y, color, file_path):
    super(Piece, self).__init__(x, y, color, file_path)
    self.first_move = True

  async def get_possible_moves(self, board):
    moves = set()

    if self.first_move:
      for i in range(self.y + 1, 8):
        
        if board[self.x][i] is None:
          continue
        elif isinstance(board[self.x][i], Rook):
          moves.add((self.x, self.y + 2))
          break
        else:
          break

      for i in range(self.y - 1, -1, -1):

        if board[self.x][i] is None:
          continue
        elif isinstance(board[self.x][i], Rook):
          moves.add((self.x, self.y - 2))
          break
        else:
          break

    if self.x - 1 >= 0:

      if board[self.x - 1][self.y] is None or board[self.x - 1][self.y].color != self.color:
        moves.add((self.x - 1, self.y))

    if self.x + 1 <= 7:

      if board[self.x + 1][self.y] is None or board[self.x + 1][self.y].color != self.color:
        moves.add((self.x + 1, self.y)) 

    if self.y - 1 >= 0:

      if board[self.x][self.y - 1] is None or board[self.x][self.y - 1].color != self.color:
        moves.add((self.x, self.y - 1))

    if self.y + 1 <= 7:

      if board[self.x][self.y + 1] is None or board[self.x][self.y + 1].color != self.color:
        moves.add((self.x, self.y + 1))

    if self.x - 1 >= 0 and self.y - 1 >= 0:

      if board[self.x - 1][self.y - 1] is None or board[self.x - 1][self.y - 1].color != self.color:
        moves.add((self.x - 1, self.y - 1))

    if self.x - 1 >= 0 and self.y + 1 <= 7:

      if board[self.x - 1][self.y + 1] is None or board[self.x - 1][self.y + 1].color != self.color:
        moves.add((self.x - 1, self.y + 1))

    if self.x + 1 <= 7 and self.y - 1 >= 0:

      if board[self.x + 1][self.y - 1] is None or board[self.x + 1][self.y - 1].color != self.color:
        moves.add((self.x + 1, self.y - 1))

    if self.x + 1 <= 7 and self.y + 1 <= 7:

      if board[self.x + 1][self.y + 1] is None or board[self.x + 1][self.y + 1].color != self.color:
        moves.add((self.x + 1, self.y + 1))

    return moves

class Pawn(Piece):

  def __init__(self, x, y, color, file_path):
    super(Piece, self).__init__(x, y, color, file_path)
    self.point = 1
    self.first_move = True

  async def get_possible_moves(self, board):

    moves = set()

    if self.color == Piece.BLACK:
      
      if self.first_move:

        if board[self.x + 1][self.y] is None and (board[self.x + 2][self.y] is None or board[self.x + 2][self.y].color != self.color):
          moves.add((self.x + 2, self.y))

      if self.x + 1 <= 7:

        if board[self.x + 1][self.y] is None or board[self.x + 1][self.y].color != self.color:
          moves.add((self.x + 1, self.y))

        if self.y - 1 >= 0 and board[self.x + 1][self.y - 1]:
          moves.add((self.x + 1, self.y - 1))

        if self.y + 1 <= 0 and board[self.x + 1][self.y + 1]:
          moves.add((self.x + 1, self.y + 1))


    if self.color == Piece.WHITE:
      if self.first_move:

        if board[self.x - 1][self.y] is None and (board[self.x - 2][self.y] is None or board[self.x - 2][self.y].color != self.color):
          moves.add((self.x - 2, self.y))

      if self.x - 1 >= 0:

        if board[self.x - 1][self.y] is None or board[self.x - 1][self.y].color != self.color:
          moves.add((self.x - 1, self.y))

        if self.y - 1 >= 0 and board[self.x - 1][self.y - 1]:
          moves.add((self.x - 1, self.y - 1))

        if self.y + 1 <= 0 and board[self.x - 1][self.y + 1]:
          moves.add((self.x - 1, self.y + 1))

    return moves