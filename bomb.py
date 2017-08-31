'''
0 = AIR
1 = BLOCK
2 = DESTRUCTIBLE_BLOCK
3 = PLAYER_BOMB
4 = PLAYER,
5 = ENEMY
6 = EXPLOSION
'''
from config import dict
from board import brd
from bomberman import bm
from config import *
import time


class Bomb(object):
    """Bomb class for creating and exploding the bomb"""
    def __init__(self, r, c):
        self.symbol = dict[3][0]
        self.is_active = False
        self.is_explosion_active = False
        self.r = r
        self.c = c
        self.created_time = time.time()

    def create_bomb(self, r, c): # for creating the bomb i.e changing the attributes of object bomb
        brd.Matrix[r, c] = 3
        self.r = r
        self.c = c
        self.created_time = time.time()

    def explosion(self): # for exploding the bomb
        self.is_explosion_active = True
        dr = [0, 0, 0, 1, -1]
        dc = [0, 1, -1, 0, 0]
        # brd.Matrix[self.r, self.c] = 6
        for i in range(5):
            if brd.Matrix[self.r+dr[i], self.c+dc[i]] in [0, 2, 3 ,4 ,5, 6]:
                if bm.r == self.r+dr[i] and bm.c == self.c+dc[i]:
                    bm.is_alive = False
                if brd.Matrix[self.r+dr[i], self.c+dc[i]] == 2:
                    bm.score += 20
                if brd.Matrix[self.r+dr[i], self.c+dc[i]] == 5:
                    for j in brd.enemies:
                        if j.r == self.r + dr[i] and j.c == self.c + dc[i]:
                            if j.is_alive:
                                j.is_alive = False
                                bm.score += 100
                                break
                brd.Matrix[self.r+dr[i], self.c+dc[i]] = 6

bomb = Bomb(-1, -1) # creating an instance object of the class Bomb
