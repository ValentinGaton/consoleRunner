class Player():

    def __init__(self, Position, Character):

        self.Player = {
            "Position": Position,
            "OldPosition":Position,
            "Character": Character
                   }

    def getPosition(self):
        return self.Player["Position"]

    def getCharacter(self):
        return self.Player["Character"]

    def setPosition(self, Position):
        self.Player["Position"] = Position

    def setOldPosition(self,Position):
        self.Player["OldPosition"] = Position

    def getOldPosition(self):
        return self.Player["OldPosition"]

    def moveLeft(self):
        Position = self.getPosition()
        self.setOldPosition(Position)
        self.setPosition([Position[0],Position[1]-1])

    def moveRight(self):
        Position = self.getPosition()
        self.setOldPosition(Position)
        self.setPosition([Position[0],Position[1]+1])

    def moveUp(self):
        Position = self.getPosition()
        self.setOldPosition(Position)
        self.setPosition([Position[0]-1,Position[1]])

    def moveDown(self):
        Position = self.getPosition()
        self.setOldPosition(Position)
        self.setPosition([Position[0]+1,Position[1]])