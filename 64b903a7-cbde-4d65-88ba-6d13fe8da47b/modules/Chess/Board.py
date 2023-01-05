from modules.Chess.Pieces import Pawn, Knight, Rook, Bishop, Queen, King, Piece
from modules.Chess.Player import Player
import numpy as np
import asyncio

class Board:

  WIDTH, HEIGHT = 8
  PATH = 'images/Chess/ChessBoard.png'
  PREFIX = 'images/Chess/'

  def __init__(self, P1: Player, P2: Player):
    self.P1 = P1
    self.P2 = P2
    self.board = np.array(
      [
        Rook(0, 0, Piece.BLACK, Board.PREFIX + 'BlackRook.png'),
        Knight(0, 1, Piece.BLACK, Board.PREFIX + 'BlackKnight.png'),
        Bishop(0, 2, Piece.BLACK, Board.PREFIX + 'BlackBishop.png'),
        Queen(0, 3, Piece.BLACK, Board.PREFIX + 'BlackQueen'),
        King(0, 4, Piece.BLACK, Board.PREFIX + 'BlackKing.png'),
        Bishop(0, 5, Piece.BLACK, Board.PREFIX + 'BlackBishop.png'),
        Knight(0, 6, Piece.BLACK, Board.PREFIX + 'BlackKnight.png'),
        Rook(0, 7, Piece.BLACK, Board.PREFIX + 'BlackRook.png')
      ],
      [Pawn(1, i, Piece.BLACK, Board.PREFIX + 'BlackPawn.png') for i in range(Board.WIDTH)],
      [None for _ in range(Board.WIDTH)],
      [None for _ in range(Board.WIDTH)],
      [None for _ in range(Board.WIDTH)],
      [None for _ in range(Board.WIDTH)],
      [Pawn(6, i, Piece.WHITE, Board.PREFIX + 'BlackPawn.png') for i in range(Board.WIDTH)],
      [
        Rook(7, 0, Piece.WHITE, Board.PREFIX + 'WhiteRook.png'),
        Knight(7, 1, Piece.WHITE, Board.PREFIX + 'WhiteKnight.png'),
        Bishop(7, 2, Piece.WHITE, Board.PREFIX + 'WhiteBishop.png'),
        Queen(7, 3, Piece.WHITE, Board.PREFIX + 'WhiteQueen'),
        King(7, 4, Piece.WHITE, Board.PREFIX + 'WhiteKing.png'),
        Bishop(7, 5, Piece.WHITE, Board.PREFIX + 'WhiteBishop.png'),
        Knight(7, 6, Piece.WHITE, Board.PREFIX + 'WhiteKnight.png'),
        Rook(7, 7, Piece.WHITE, Board.PREFIX + 'WhiteRook.png')
      ]
    )

  async def send(self, ctx):
    pass

  async def move(self, ctx, first, second, color):
    x1, y1 = first
    x2, y2 = second

  async def castle(self):
    pass

  async def promote(self):
    pass

  def __repr__(self):
    return f'{self.P1}\n{self.P2}'