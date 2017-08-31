from board import brd
from person import Person
import numpy as np
# from bomb import bm
'''
0 = AIR
1 = BLOCK
2 = DESTRUCTIBLE_BLOCK
3 = PLAYER_BOMB
4 = PLAYER,
5 = ENEMY
6 = EXPLOSION
'''

class Bomberman(Person):
    """docstring for Bomberman"""
    def __init__(self, r, c):
        Person.__init__(self, r, c) # Inheritance of Class Person for bomberman
        self.no_of_life = 3
        self.is_alive = True
        self.score = 0
        
    def checkMove(self, dr, dc): # For checking that this move is possible or not (i.e not blocked by any brick or wall)
        a = self.r + dr
        b = self.c + dc
        if brd.Matrix[a, b] in [0, 5, 6]: return True
        else: return False

    def move(self, dr, dc): # for movement of the bomberman
        flag = 0
        if self.checkMove(dr, dc):
            if brd.Matrix[self.r, self.c] == 3: pass
            elif brd.Matrix[self.r, self.c] == 4:
                brd.Matrix[self.r, self.c] = 0
                
            if brd.Matrix[self.r + dr, self.c + dc] == 5:
                self.is_alive = False
                flag = 1
            elif brd.Matrix[self.r + dr, self.c + dc] == 6:
                self.is_alive = False
            else:
                brd.Matrix[self.r + dr, self.c + dc] = 4
            self.r += dr
            self.c += dc
        if flag == 1: return True
        else: return False 

    # def dropBomb(self):
    #   brd.Matrix[self.r, self.c] = 3

bm = Bomberman(1, 1)
