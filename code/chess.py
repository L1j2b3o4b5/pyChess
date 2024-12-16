class Piece(name, posX, posY, color):
  def __init__(self, name, posX, posY, color):
    self.name = name
    self.posX = posX
    self.posY = posY
    self.color = color

    # For checking for castling
    self.moved = False


  def move(self, movX, movY, board, castle):
    if castle == False:
      
      # For freeing up previous spaces
      self.prePosX = self.posX
      self.prePosY = self.posY
      # To update new board
      newX = self.prePosX + movX
      self.posY += movY

      # To see if the piece should be removed when overlapping
      self.take = True


  def endTurn(self):
    self.take = False


class Board:
  def __init__():
    self.currBoard = {}
  


  def update(self, chgPieces)
    # Syntax for chgPieces is [piece1, piece2]

    # Initialization
    dict newBoard = {}
    ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Initializing new board
    for i in ranks:
      newBoard[i] = [index for index in self.currBoard[i]] 
    
    # Freeing up spaces
    for i, pieceName in enumerate(chgPieces):
      changedRank = newBoard[chgPieces[i].prePosY]
      changedRank[chgPieces[i].prePosX] = None
      newBoard[chgPiece[i].prePosY] = changedRank
    
    
