#!/usr/bin/env python
import numpy as np
import random, os, time, sys, math
from config import ROW_SIZE, COL_SIZE, dict
from termcolor import colored
'''
row_size of board = 21
col_size of board = 21
'''

'''
0 = AIR
1 = BLOCK
2 = DESTRUCTIBLE_BLOCK
3 = PLAYER_BOMB
4 = PLAYER,
5 = ENEMY
6 = EXPLOSION
'''

class Board(object):
    """Board for playing game"""
    def __init__(self):
        s = (ROW_SIZE, COL_SIZE)
        self.columns = COL_SIZE
        self.rows = ROW_SIZE
        self.Matrix = np.zeros(s)
        self.brickSymbol = "####"
        self.wallSymbol = "%%%%"
        self.PLAYER_TOP = "[^^]"
        self.PLAYER_BOTTOM = " ][ "
        self.ENEMY_TOP = "(@@)"
        self.ENEMY_BOTTOM = " || "
        self.space = "    "
        self.level = 3 # no. of levels in the game
        self.enemies = [] 

    def generateBoundary(self): # genrate Boundary of the game made of walls[%%%%]

        for i in range(ROW_SIZE): # This is for initialising the whole matrix when level changes
            for j in range(COL_SIZE):
                self.Matrix[i, j] = 0

        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if (i == 0 or i == ROW_SIZE-1) or (j == 0 or j == COL_SIZE-1):
                    self.Matrix[i, j] = 1

    def generateBoard(self): # This function is for generating the board i.e within the boundary walls

        for i in range(ROW_SIZE-2):
            for j in range(COL_SIZE-2):
                if i + j == 0: # For placing the Player at (1, 1) [0 based indexing]
                    self.Matrix[i+1, j+1] = 4
                elif i + j == 1: 
                    self.Matrix[i+1, j+1] = 0
                elif i&1 and j&1: # For placing the wall [0 based indexing]
                    self.Matrix[i+1, j+1] = 1
                elif np.random.random(1) <= 0.2: # For placing the destructible_blocks [0 based indexing]
                    self.Matrix[i+1, j+1] = 2

brd = Board()
brd.generateBoundary()
brd.generateBoard()
