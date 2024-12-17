from .chess import Piece

# Error codes: 0 = nothing, 1 = invalid, 2 = against the rules

# Pieces
class PieceTemplate(Piece):
  def __init__(self, name, whStartX, whStartY, bkStartX, bkStartY, color):
    if color == "white":
      super.__init__(name, whStartX, whStartY, color)
    elif color == "black":
      super.__init__(name, bkStartX, bkStartY, color)

  def move(self, movX, movY, knight, board):
    # if <enter condition here>:
    blocked = False
    dictIndex1 = range(self.posY, self.posY + movY)
    dictIndex2 = range(self.posX
    super.move(movX, movY, board)

  # Enter other special moves here
class King(PieceTemplate):
  def __init__(self, color):
    super.__init__(

  def move(self, movX, movY, board):
    if (abs(movX) < 2) and (abs(movY) < 2):
      return super.move(movX, movY, board)
    else:
      return 2

  def castle(self, board):
    if ((not self.moved) and board[0]['h'].name == "rook" and board[0]['h'].color == "white") or ((not self.moved) and board[7]['a'].name == "rook" and board[7]['a'].color == "black"):
      self.prePosX = self.posX
      self.prePosY = self.posY
      
      
    
    
  
    
