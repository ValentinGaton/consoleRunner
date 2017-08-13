#!/usr/bin/env python3
# coding: utf-8


from importation.Easter.GameObject.Player import Player
import tkinter as tk

import random

def main():

    SCREENYSIZE = 8
    SCREENXSIZE = 60
    MAPCHARACTER = "_"
    PLAYERCHARACTER = "@"
    OBSTACLECHARACTER = "0"
    BORDER = "#"
    map = [[MAPCHARACTER for i in range(SCREENXSIZE)] for j in range(SCREENYSIZE)]
    Player1 = Player([4,10],PLAYERCHARACTER)
    futureString = "__*__*__"

    def LeftKey(event):
        Player1.moveLeft()
        # MapRefreshAfterMove()
    def RightKey(event):
        Player1.moveRight()
        # MapRefreshAfterMove()
    def DownKey(event):
        Player1.moveDown()
        # MapRefreshAfterMove()
    def UpKey(event):
        Player1.moveUp()
        # MapRefreshAfterMove()

    def MapRefreshAfterMove():
        OldPositionYX = Player1.getOldPosition()
        map[OldPositionYX[0]][OldPositionYX[1]] = map[OldPositionYX[0]][OldPositionYX[1]+1]
        PositionYX = Player1.getPosition()
        if(map[PositionYX[0]][PositionYX[1]] == OBSTACLECHARACTER):
            EndGame()
        map[PositionYX[0]][PositionYX[1]] = Player1.getCharacter()
        map[PositionYX[0]][PositionYX[1]-1] = map[PositionYX[0]][PositionYX[1]+1]
        MapPrinter()

    def MapPrinter():
        text.delete('1.0', "end")
        for i in range(SCREENXSIZE):
            text.insert('end', BORDER)
        text.insert('end', '\n')
        for y in map:
            for x in y:
                text.insert('end', x)
            text.insert('end', '\n')
        for i in range(SCREENXSIZE):
            text.insert('end', BORDER)
        text.insert('end', '\n')
        text.pack()

    def MapRefresh():
        futureString = FutureStringGenerator()
        Y = 0
        for y in map:
            y.pop(0)
            y.append(futureString[Y])
            if(PLAYERCHARACTER in y):
                map[Y][y.index(PLAYERCHARACTER)] = MAPCHARACTER
            if(Player1.getPosition()[0] == Y):
                pass
                # Player1.moveRight()
                # MapRefreshAfterMove()
            Y += 1
        MapRefreshAfterMove()
        root.after(35, MapRefresh)

    def FutureStringGenerator():
        futureString = ''.join(random.choice(MAPCHARACTER*50 + OBSTACLECHARACTER) for _ in range(SCREENYSIZE))
        return futureString

    def EndGame():
        root.cancel()


    root = tk.Tk()
    root.geometry('600x800')
    text = tk.Text(root, background='black', foreground='white', font=("Helvetica",12))

    # root.bind('<Left>', LeftKey)
    # root.bind('<Right>', RightKey)
    root.bind('<Up>', UpKey)
    root.bind('<Down>', DownKey)

    for i in range(SCREENXSIZE):
        text.insert('end', BORDER)
    text.insert('end', '\n')
    for y in map:
        for x in y:
            text.insert('end',x)
        text.insert('end', '\n')
    for i in range(SCREENXSIZE):
        text.insert('end', BORDER)
    text.insert('end', '\n')
    text.pack()
    MapRefresh()
    root.mainloop()
if __name__ == '__main__':
    main()