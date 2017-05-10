import sys
from chessPieces import Piece, Pawn
#input ("Welcome to Chess, press enter to load game")

#for _ in range(8):
#    print (". " * 8)

# Piece not Peice/ Peace

class Board:
    def __init__(self):
        self.matrix = self.create_board()

    def create_board(self):
        matrix = [[ None for _ in range(8)] for _ in range(8)]
        return matrix

    def printBoard(self):
        counter = 7
        for row in self.matrix:
            sys.stdout.write(str(counter) + ". ")
            counter += -1
            for square in row:
                if square:
                    sys.stdout.write((square.getName())+ " ")
                else:
                    sys.stdout.write(("[_] "))
            print()
        print("    a   b   c   d   e   f   g   h")

    def updateBoard(self, Piece):
        location = Piece.getLocation()
        self.matrix[7- location[1]] [location[0]]= Piece

    def getPiece(self, location):
        square = self.matrix[7- location[1]] [location[0]]
        return square

    def movePiece(self, piece, destination):
        print("here")
        print(destination)
        currentLocation= piece.getLocation()
        print(currentLocation)
        piece.changeLocation(destination)
        print(piece.getLocation())
        self.matrix[7 - destination[1]][destination[0]] = piece
        self.matrix[7 - currentLocation[1]][currentLocation[0]] = None



"""
    I need to identify a piece in the board. Then I need to get its range
    of motion (moves). Then I need to check which ones are legal by
    interacting with the board.
"""
class Parser:
    def __init__(self, board, whiteMove):
        self.board = board
        self.whiteMove = whiteMove
        self.location = None
        self.destination = None

    def waiter(self):
        if self.whiteMove:
            print("White Move")
        else:
            print("Black Move")
        properOrder = False
        while not properOrder:
            self.location= self.prompt()
            piece = self.board.getPiece(self.location)
            if piece:
                properOrder = True
            else:
                print("No Good Piece")
# The above gets a piece, I am going to ask for a valid spot to move to now
# The piece itself will have a function with the board as input deciding if
# the move is a valid one
        print("Where To?")
        moves = piece.getMoves()
        while True:
            while True:
                self.destination = self.prompt()
                inside = False
                for x in moves:
                    if self.destination == x:
                        inside = True
    # if the destination was not found in moveset... we do it again
                if inside:
                    break
                else:
                    print("Not good move")
    # Now that we have a destination, it will be up to the object to efficiently
    # check if that move is legal
            if piece.checkLegal(self.board, self.destination):
                print("Legal")
                break
# Now I am going to override the destination square and erase
# the leaving square
        self.board.movePiece(piece, self.destination)
        return self.board

# returns a valid square
    def prompt(self):
        properInput = False
# This checks if a letter then a number was put in
        while not properInput:
            location =input(">")
            properInput = True
            if not len(location) == 2:
                print("Incorrect Input")
                properInput = False

            elif not location[0].isalpha():
                print("Incorrect input")
                properInput = False
            elif properInput:
                try:
                    float(location[1])
                except ValueError:
                    print("Incorrect input")
                    properInput = False
# This converts location to coordinates and checks if its within range of board
    # This is still part of while loop
            if properInput:
                column = ord(location[0]) - 97
                row = location[1]
                location = [int(column), int(row)]

                if (location[0]< 0 or location[0] > 7):
                    print("Out of Range")
                    properInput = False
                elif (location[1] < 0 or location[1] >7):
                    print("Out of Range")
                    properInput = False

        return location



        #else:
        #   print(square.name)


boardObject = Board()
# True for whiteMove
getter = Parser(boardObject, True)

pw1 = Pawn([3, 1], "white")
pw2 = Pawn([2, 2], "white")
pw3 = Pawn([4, 2], "black")
temp = pw1.getMoves()
print (temp)

boardObject.updateBoard(pw1)
boardObject.updateBoard(pw2)
boardObject.updateBoard(pw3)
boardObject.printBoard()

boardObject= getter.waiter()
boardObject.printBoard()
# getter = Parser(boardObject, False)
