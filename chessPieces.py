class Piece:
    def __init__(self, location, name, color):
        self.location = location
        self.name = name
        self.color = color
        #place on Board

class Pawn(Piece):
    def __init__(self, location, color):
        Piece.__init__(self, location, "Pawn", color)

    def getLocation(self):
        return self.location

    def getName(self):
        if self.color== "white":
            name = "w_P"
        else:
            name = "b_P"
        return name

    def getMoves(self):
        if self.color == "white":
            moves = self.getMovesWhite()
        #else:
        #   moves = getMovesBlack()
        return moves

    def changeLocation(self, location):
        self.location= location

#location = column then row [#, #]
    def getMovesWhite(self):
        moves = [[]]
        moves[0]=[self.location[0], self.location[1]+ 1]
        moves.append([self.location[0] -1, self.location[1]+ 1])
        moves.append([self.location[0] + 1, self.location[1]+ 1])
        if self.location[1] == 1:
            moves.append([self.location[0], 3])
        return moves

# check legal only works for white so far
    def checkLegal(self, board, destination):
        legal = True
        location = self.location
# forward movement
        if destination[0] == location [0]:
            counter = destination[1] - location[1]
            square = location
            while counter > 0 :
                square[1] = square[1] + 1
                counter -= 1
                print (square)
                obstacle = board.getPiece(square)
                if obstacle:
                    print("Something in the way")
                    return False
            return True
# capturing diagonal
        else:
            target = board.getPiece(destination)
            if target:
                if target.color == "black":
                    return True
                else:
                    print("Cannot capture your own piece")
                    return False
            else:
                print("Nothing to Capture there")
                return False
