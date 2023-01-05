from modules.Chess.AI import board, ai

PIECES = {
      "WRook": {
        0: "<:WWhiteRook:884006648727879701>",
        1: "<:BWhiteRook:884006690977091584>"
      },
      "WKnight": {
        0: "<:WWhiteKnight:884006670135607296>",
        1: "<:BWhiteKnight:884006691086155796>"
      },
      "WBishop": {
        0: "<:WWhiteBishop:884006649050832936>",
        1: "<:BWhiteBishop:884006691014844446>"
      },
      "WQueen": {
        0: "<:WWhiteQueen:884006649004703804>",
        1: "<:BWhiteQueen:884006691132305460>"
      },
      "WKing": {
        0: "<:WWhiteKing:884006649201819650>",
        1: "<:BWhiteKing:884006691132284968>"
      },
      "WPawn": {
        0: "<:WWhitePawn:884006648874672188>",
        1: "<:BWhitePawn:884006690989682709>"
      },
      "BRook": {
        0: "<:WBlackRook:884004604113723423>",
        1: "<:BBlackRook:884005038169677864>"
      },
      "BKnight": {
        0: "<:WBlackKnight:884004604495405066>",
        1: "<:BBlackKnight:884005038110965790>"
      },
      "BBishop": {
        0: "<:WBlackBishop:884004604445085696>",
        1: "<:BBlackBishop:884005038152908800>"
      },
      "BQueen": {
        0: "<:WBlackQueen:884004604482822174>",
        1: "<:BBlackQueen:884005037687312455>"
      },
      "BKing": {
        0: "<:WBlackKing:884004604579287040>",
        1: "<:BBlackKing:884005038001913887>"
      },
      "BPawn": {
        0: "<:WBlackPawn:884004604466061322>",
        1: "<:BBlackPawn:884005037792170015>"
      },
    }

class Piece():

    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, piece_type, value):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type
        self.value = value



    # Returns all diagonal moves for this piece. This should therefore only
    # be used by the Bishop and Queen since they are the only pieces that can
    # move diagonally.
    def get_possible_diagonal_moves(self, board):
        moves = []

        for i in range(1, 8):
            if (not board.in_bounds(self.x+i, self.y+i)):
                break

            piece = board.get_piece(self.x+i, self.y+i)
            moves.append(self.get_move(board, self.x+i, self.y+i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x+i, self.y-i)):
                break

            piece = board.get_piece(self.x+i, self.y-i)
            moves.append(self.get_move(board, self.x+i, self.y-i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x-i, self.y-i)):
                break

            piece = board.get_piece(self.x-i, self.y-i)
            moves.append(self.get_move(board, self.x-i, self.y-i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x-i, self.y+i)):
                break

            piece = board.get_piece(self.x-i, self.y+i)
            moves.append(self.get_move(board, self.x-i, self.y+i))
            if (piece != 0):
                break

        return self.remove_null_from_list(moves)

    # Returns all horizontal moves for this piece. This should therefore only
    # be used by the Rooks and Queen since they are the only pieces that can
    # move horizontally.
    def get_possible_horizontal_moves(self, board):
        moves = []

        # Moves to the right of the piece.
        for i in range(1, 8 - self.x):
            piece = board.get_piece(self.x + i, self.y)
            moves.append(self.get_move(board, self.x+i, self.y))

            if (piece != 0):
                break

        # Moves to the left of the piece.
        for i in range(1, self.x + 1):
            piece = board.get_piece(self.x - i, self.y)
            moves.append(self.get_move(board, self.x-i, self.y))
            if (piece != 0):
                break

        # Downward moves.
        for i in range(1, 8 - self.y):
            piece = board.get_piece(self.x, self.y + i)
            moves.append(self.get_move(board, self.x, self.y+i))
            if (piece != 0):
                break

        # Upward moves.
        for i in range(1, self.y + 1):
            piece = board.get_piece(self.x, self.y - i)
            moves.append(self.get_move(board, self.x, self.y-i))
            if (piece != 0):
                break

        return self.remove_null_from_list(moves)

    # Returns a Move object with (xfrom, yfrom) set to the piece current position.
    # (xto, yto) is set to the given position. If the move is not valid 0 is returned.
    # A move is not valid if it is out of bounds, or a piece of the same color is
    # being eaten.
    def get_move(self, board, xto, yto):
        move = 0
        if (board.in_bounds(xto, yto)):
            piece = board.get_piece(xto, yto)
            if (piece != 0):
                if (piece.color != self.color):
                    move = ai.Move(self.x, self.y, xto, yto, False)
            else:
                move = ai.Move(self.x, self.y, xto, yto, False)
        return move

    # Returns the list of moves cleared of all the 0's.
    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]

    def to_string(self):
        return self.color + self.piece_type + " "

class Rook(Piece):

    PIECE_TYPE = "R"
    VALUE = 500

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE, Rook.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def clone(self):
        return Rook(self.x, self.y, self.color)

    def __repr__(self) -> str:
        return PIECES[f"{self.color}Rook"][(self.x + self.y) % 2]


class Knight(Piece):

    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)

    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x+2, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y+2))
        moves.append(self.get_move(board, self.x-2, self.y+1))
        moves.append(self.get_move(board, self.x+1, self.y-2))
        moves.append(self.get_move(board, self.x+2, self.y-1))
        moves.append(self.get_move(board, self.x+1, self.y+2))
        moves.append(self.get_move(board, self.x-2, self.y-1))
        moves.append(self.get_move(board, self.x-1, self.y-2))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Knight(self.x, self.y, self.color)

    def __repr__(self) -> str:
        return PIECES[f"{self.color}Knight"][(self.x + self.y) % 2]


class Bishop(Piece):

    PIECE_TYPE = "B"
    VALUE = 330

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE, Bishop.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_diagonal_moves(board)

    def clone(self):
        return Bishop(self.x, self.y, self.color)

    def __repr__(self) -> str:
        return PIECES[f"{self.color}Bishop"][(self.x + self.y) % 2]


class Queen(Piece):

    PIECE_TYPE = "Q"
    VALUE = 900

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE, Queen.VALUE)

    def get_possible_moves(self, board):
        diagonal = self.get_possible_diagonal_moves(board)
        horizontal = self.get_possible_horizontal_moves(board)
        return horizontal + diagonal

    def clone(self):
        return Queen(self.x, self.y, self.color)

    def __repr__(self) -> str:
        return PIECES[f"{self.color}Queen"][(self.x + self.y) % 2]


class King(Piece):

    PIECE_TYPE = "K"
    VALUE = 20000

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE, King.VALUE)

    def get_top_castling_move(self, board):
        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        piece = board.get_piece(self.x-4, self.y)
        if (piece != 0):
            if (piece.color == self.color and piece.piece_type == Rook.PIECE_TYPE):
                if (board.get_piece(self.x-1, self.y) == 0 and board.get_piece(self.x-2, self.y) == 0 and board.get_piece(self.x-3, self.y)):
                    return ai.Move(self.x, self.y, self.x-2, self.y, True)

        return 0

    def get_bottom_castling_move(self, board):
        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        piece = board.get_piece(self.x+3, self.y)
        if (piece != 0):
            if (piece.color == self.color and piece.piece_type == Rook.PIECE_TYPE):
                if (board.get_piece(self.x+1, self.y) == 0 and board.get_piece(self.x+2, self.y) == 0):
                    return ai.Move(self.x, self.y, self.x+2, self.y, True)

        return 0

    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x+1, self.y))
        moves.append(self.get_move(board, self.x+1, self.y+1))
        moves.append(self.get_move(board, self.x, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y))
        moves.append(self.get_move(board, self.x-1, self.y-1))
        moves.append(self.get_move(board, self.x, self.y-1))
        moves.append(self.get_move(board, self.x+1, self.y-1))

        moves.append(self.get_top_castling_move(board))
        moves.append(self.get_bottom_castling_move(board))

        return self.remove_null_from_list(moves)

    


    def clone(self):
        return King(self.x, self.y, self.color)

    def __repr__(self) -> str:
        return PIECES[f"{self.color}King"][(self.x + self.y) % 2]


class Pawn(Piece):

    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)

    def is_starting_position(self):
        if (self.color == Piece.BLACK):
            return self.y == 1
        else:
            return self.y == 8 - 2

    def get_possible_moves(self, board):
        moves = []

        # Direction the pawn can move in.
        direction = -1
        if (self.color == Piece.BLACK):
            direction = 1

        # The general 1 step forward move.
        if (board.get_piece(self.x, self.y+direction) == 0):
            moves.append(self.get_move(board, self.x, self.y + direction))

        # The Pawn can take 2 steps as the first move.
        if (self.is_starting_position() and board.get_piece(self.x, self.y+ direction) == 0 and board.get_piece(self.x, self.y + direction*2) == 0):
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        # Eating pieces.
        piece = board.get_piece(self.x + 1, self.y + direction)
        if (piece != 0):
            moves.append(self.get_move(board, self.x + 1, self.y + direction))

        piece = board.get_piece(self.x - 1, self.y + direction)
        if (piece != 0):
            moves.append(self.get_move(board, self.x - 1, self.y + direction))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)

    def __repr__(self) -> str:
        return PIECES[f"{self.color}Pawn"][(self.x + self.y) % 2]
