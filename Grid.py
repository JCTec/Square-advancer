#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from tabulate import tabulate

class Grid:

    x = 0
    y = 0

    pos = 'R'

    steps = 0
    count = 0

    def __init__(self, col, row):
        self.col = col
        self.row = row

        self.verbosee = str(col) + "x" + str(row)

        self.steps = col * row

        self.matrix = []

        for y in range(self.row):
            row = []
            for x in range(self.col):
                row.append(Node(x,y))

            self.matrix.append(row)

        self.get(self.x, self.y).visitNode()
        self.count += 1


    def get(self, x, y):
        try:
            return self.matrix[y][x]
        except IndexError:
            print("Error: x -> " + str(x) + ", y -> " + str(y))
            exit()


    def isRight(self):
        return self.pos == 'R'

    def isLeft(self):
        return self.pos == 'L'

    def isUp(self):
        return self.pos == 'U'

    def isDown(self):
        return self.pos == 'D'

    def right(self):
        self.pos = 'R'

    def left(self):
        self.pos = 'L'

    def up(self):
        self.pos = 'U'

    def down(self):
        self.pos = 'D'

    def nextHasBoundaries(self, noVisited=False):

        if noVisited:
            if self.isRight():

                if self.x + 1 >= self.col:
                    return True
                else:
                    return False

            elif self.isDown():

                if self.y + 1 >= self.row:
                    return True
                else:
                    return False

            elif self.isLeft():

                if self.x - 1 < 0:
                    return True
                else:
                    return False

            elif self.isUp():

                if self.y - 1 < 0:
                    return True
                else:
                    return False

        else:
            if self.isRight():

                if self.get(self.x+1, self.y).isVisited():
                    return True
                else:
                    return False

            elif self.isDown():

                if self.get(self.x, self.y+1).isVisited():
                    return True
                else:
                    return False

            elif self.isLeft():

                if self.get(self.x-1, self.y).isVisited():
                    return True
                else:
                    return False

            elif self.isUp():

                if self.get(self.x, self.y-1).isVisited():
                    return True
                else:
                    return False

        return False

    def next(self):

        if self.isRight():
            self.x += 1
            self.get(self.x, self.y).visitNode()

        elif self.isDown():
            self.y += 1
            self.get(self.x, self.y).visitNode()

        elif self.isLeft():
            self.x -= 1
            self.get(self.x, self.y).visitNode()

        elif self.isUp():
            self.y -= 1
            self.get(self.x, self.y).visitNode()

        self.count += 1

    def moveLastly(self):

        if self.isRight():
            self.down()

        elif self.isDown():
            self.left()

        elif self.isLeft():
            self.up()

        elif self.isUp():
            self.right()


    def calculate(self, timer=True, verbose=False):

        start = time.time()

        if verbose:
            print(self.verbosee)
            print("Calculando...")
            self.verbose()

        while self.count < self.steps:

            if self.isRight():

                if self.nextHasBoundaries(True) or self.nextHasBoundaries(False):
                    self.down()
                else:
                    self.next()

            elif self.isDown():

                if self.nextHasBoundaries(True) or self.nextHasBoundaries(False):
                    self.left()
                else:
                    self.next()

            elif self.isLeft():

                if self.nextHasBoundaries(True) or self.nextHasBoundaries(False):
                    self.up()
                else:
                    self.next()

            elif self.isUp():

                if self.nextHasBoundaries(True) or self.nextHasBoundaries(False):
                    self.right()

                else:
                    self.next()

            if verbose:
                self.verbose()


        if self.row == 1 and self.col != 1:
            self.moveLastly()

        if verbose:
            self.verbose()

        end = time.time()

        elapsed = end - start

        if verbose:
            self.verbose()

        if timer or verbose:
            print("Tiempo transcurrido: " + str(elapsed))

        if self.allVisited:
            print("Ultima Posición: " + self.pos)
            return self.pos


    def verbose(self):
        print("------------------------------")
        print("Steps:" + str(self.steps))
        print("Count:" + str(self.count))

        print("Pos:" + self.pos)
        print("X:" + str(self.x))
        print("Y:" + str(self.y))
        print("------------------------------")
        print(tabulate(self.matrix))
        print("------------------------------")
        time.sleep(1)

    def allVisited(self):
        for y in range(self.row):
            for x in range(self.col):
                if self.matrix[y][x].isVisited() == False:
                    return False

        return True



class Node:

    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.visited = False

    def visitNode(self):
        self.visited = True

    def isVisited(self):
        return self.visited

    def __str__(self):
        if self.isVisited():
            return "."
        else:
            return "o"

    def __float__(self):
        if self.isVisited():
            return 1.00
        else:
            return 0.00
