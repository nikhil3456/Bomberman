from person import Person
from board import brd
from bomberman import bm
import numpy as np
'''
0 = AIR
1 = BLOCK
2 = DESTRUCTIBLE_BLOCK
3 = PLAYER_BOMB
4 = PLAYER,
5 = ENEMY
6 = EXPLOSION
'''

class Enemy(Person):
    """docstring for Enemy"""
    def __init__(self, r, c):
        Person.__init__(self, r, c) # Inheritance of Class Person for bomberman
        self.is_alive = False
        self.is_smart = False

    def checkMove(self, dr, dc): # For checking that this move is possible or not (i.e not blocked by any brick or wall)
        a = self.r + dr
        b = self.c + dc
        if 0 < a < brd.rows-1 and 0 < b < brd.columns-1:
            if brd.Matrix[a, b] in [0, 4, 6]:
                if self.is_smart and brd.Matrix[a, b] == 6: 
                    return False
                return True
            return False
        return False

    def enemy_move(self): # For moving different types of enemies
        if self.is_smart == True: # For moving Minions
            dr = [0, 0, 1, -1]
            dc = [1, -1, 0, 0]
            min_dis = 20000
            choosen_dir = [0, 0]
            for pos in range(4):
                if self.checkMove(dr[pos], dc[pos]):
                    dis = abs(bm.r -(self.r + dr[pos])) + abs(bm.c - (self.c + dc[pos]))
                    if min_dis >= dis:
                        choosen_dir = [dr[pos], dc[pos]]
                        min_dis = dis
            self.move(choosen_dir[0], choosen_dir[1])
        else:
            self.rand_move()

    def rand_move(self): # For randomly selecting and moving the enemy
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        rand = np.random.randint(4)
        if self.checkMove(dr[rand], dc[rand]):
            self.move(dr[rand], dc[rand])
        else:
            pass

    def move(self, dr, dc): # For moving the enemy
        brd.Matrix[self.r, self.c] = 0
        if brd.Matrix[self.r + dr, self.c + dc] == 4:
            bm.is_alive = False
            brd.Matrix[self.r+dr, self.c+dc] = 5
        elif brd.Matrix[self.r+dr, self.c+dc] == 6:
            if self.is_alive:
                self.is_alive = False
                bm.score += 100
        else: brd.Matrix[self.r+dr, self.c+dc] = 5
        self.r += dr
        self.c += dc

    


