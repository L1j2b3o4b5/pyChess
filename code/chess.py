# Error codes: 0 = nothing, 1 = invalide position, 3 = against the rules
# When translating the chess algebraic notation, add 1 to the file

class Piece:
  def __init__(self, name, posX, posY, color):
    self.name = name
    self.posX = posX
    self.posY = posY
    self.color = color

    # For checking for castling
    self.moved = False


  def move(self, movX, movY, board, ):
    ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # For checking rules
    newX = self.prePosX + movX
    newY = ranks[ranks.index(self.prePosY) + movY]
    if newX > 7 or newY not in ranks or (board[newY][newX] is None and board[newY][newX].color == selfcolor):
      return 1
    else:
      
      # For freeing up previous spaces
      self.prePosX = self.posX
      self.prePosY = self.posY
      
      # To update new board
      newX = self.prePosX + movX
      self.posY += movY

      # To see if the piece should be removed when overlapping
      self.take = True

      return 0


  def endTurn(self):
    self.take = False


class Board:
  def __init__(self, board):
    self.currBoard = board
  


  def update(self, chgPieces)
    # Syntax for chgPieces is [piece1, piece2]

    # Initialization
    newBoard = {}
    ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Initializing new board
    for i in ranks:
      newBoard[i] = [index for index in self.currBoard[i]] 
    
    # Freeing up spaces
    for i, pieceName in enumerate(chgPieces):
      newBoard[pieceName.prePosY][pieceName.prePosX] = None

    # Taking pieces
    for i, name in enumerate(chgPieces):
      if not self.currBoard[chgPieces[i].posY][chgPieces[i].posX] is None:
        newBoard[chgPieces[i].posY][chgPieces[i].posX] = chgPieces[i]


    
    
