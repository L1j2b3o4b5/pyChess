class Piece(name, posX, posY, color):
  def __init__(self, name, posX, posY, color):
    self.name = name
    self.posX = posX
    self.posY = posY
    self.color = color

    # For checking for castling
    self.moved = False


  def move(self, movX, movY):

    # For freeing up previous spaces
    self.prePosX = self.posX
    self.prePosY = self.posY

    # To update new board
    self.posX += movX
    self.posY += movY

    # To see if the piece should be removed when overlapping
    self.take = True


  def endTurn(self):
    self.take = False


class Board:
  def __init__():
    self.currBoard = {}
  


  def update(self, chgPieces)
    # Syntax for chgPieces is [white#1, black#1, white#2, black#2]

    # Initialization
    dict newBoard = {}
    ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Initializing new board
    for i in ranks:
      newBoard[i] = [index for index in self.currBoard[i]] 
    
    # Freeing up spaces
    changedRankOne = newBoard[chgPieces[0].prePosY]
    
    changedRowTwo = newBoard[chgPieceTwo.prePosX]
