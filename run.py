'''
0 = AIR
1 = BLOCK
2 = DESTRUCTIBLE_BLOCK
3 = PLAYER_BOMB
4 = PLAYER,
5 = ENEMY
6 = EXPLOSION
'''

from board import brd
from config import *
from termcolor import colored, cprint
import numpy as np
import os, time, sys
from bomberman import bm
from enemy import Enemy
from getch import getch
from bomb import bomb

class Play(object):
    """docstring for Play"""
    def __init__(self):
        self.level = 1
        self.count_enemies = NO_OF_ENEMIES  
    def print_board(self): # For printing the board after every iteration 

        os.system('clear')

        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if brd.Matrix[i, j] == 4 and bm.is_alive:
                    print(colored(brd.PLAYER_TOP, "yellow")),
                elif brd.Matrix[i, j] == 5:
                    tmp = -1
                    for enem in brd.enemies:
                        tmp += 1
                        if enem.r == i and enem.c == j and enem.is_alive:
                            if self.level > 1 and enem.is_smart:
                                print(colored(brd.ENEMY_TOP, "yellow")),
                            else:
                                print(colored(brd.ENEMY_TOP, "red")),

                else:
                    print(colored(dict[brd.Matrix[i, j]][0], dict[brd.Matrix[i, j]][1])),
            print("\n"),
            for j in range(COL_SIZE):
                if brd.Matrix[i, j]==4 and bm.is_alive:
                    print(colored(brd.PLAYER_BOTTOM, "yellow")),
                elif brd.Matrix[i, j] == 5:
                    for enem in brd.enemies:
                        if enem.r == i and enem.c == j and enem.is_alive:
                            print(colored(brd.ENEMY_BOTTOM, "red")),
                else:
                    print(colored(dict[brd.Matrix[i, j]][0], dict[brd.Matrix[i, j]][1])),
            print("\n"),

        print("Your score: "),
        print(bm.score)
        print("Lifes Left: "),
        print(bm.no_of_life)
        print("Level number: "),
        print(self.level)

    # creating enemies
    def create_enemies(self):
        possible_places = [] # selecting possible places for creating enemies  
        for i in range(ROW_SIZE-2):
            for j in range(COL_SIZE-3):
                if brd.Matrix[i+1, j+2] == 0:
                    possible_places.append([i+1, j+2])
        length = len(possible_places)
        rand = list((np.random.randint(length, size=self.count_enemies)))
        for i in rand:
            temp = Enemy(possible_places[i][0], possible_places[i][1])
            temp.is_alive = True
            brd.enemies.append(temp)
        for i in range(self.count_enemies):
            brd.Matrix[brd.enemies[i].r, brd.enemies[i].c] = 5

    def changeLevel(self): # When Level changes
        self.level += 1
        brd.enemies = []
        bm.r = 1
        bm.c = 1
        os.system('clear')
        brd.generateBoundary()
        brd.generateBoard()
        self.count_enemies = self.count_enemies + 1
        self.create_enemies()
        for i in range(self.count_enemies):
            if (i&1): brd.enemies[i].is_smart = True     
            else: pass
        print "Level", self.level
        time.sleep(2)
        self.print_board()
        self.main()

    def gameOver(self):
        self.print_board()
        time.sleep(2)
        os.system('clear')
        print "Oops, you died. Your final score is:", bm.score
        time.sleep(1)
        exit()

    def gameWon(self):
        self.print_board()
        time.sleep(2)
        os.system('clear')
        print "Congrats!! you Won!!!. Your final score is:", bm.score
        time.sleep(1)
        exit()

    def reborn(self):
        bm.is_alive = True
        self.print_board()
        possible_places = []
        for i in range(ROW_SIZE-2):
            for j in range(COL_SIZE-2):
                if brd.Matrix[i+1, j+1] == 0:
                    possible_places.append([i+1, j+1])
        length = len(possible_places)
        rand = np.random.randint(length)
        brd.Matrix[possible_places[rand][0], possible_places[rand][1]] = 4
        bm.r = possible_places[rand][0]
        bm.c = possible_places[rand][1]
        time.sleep(2)
        self.print_board()

    def move(self, dr, dc):
        bool = bm.move(dr, dc)
        if bool == True and bm.is_alive == False and bm.no_of_life > 0:
            bm.no_of_life -= 1
            if bomb.is_active:
                bomb.is_active = False
                brd.Matrix[bomb.r, bomb.c] = 0
                if bomb.is_explosion_active:
                    self.clean_explosion()
                else: self.reborn()
        elif bm.is_alive==False and bm.no_of_life == 0:   
            self.gameOver()
        return

    def clean_explosion(self):
        bomb.is_explosion_active = False
        dr = [0, 0, 0, 1, -1]
        dc = [0, 1, -1, 0, 0]
        for i in range(5):
            if brd.Matrix[bomb.r + dr[i], bomb.c + dc[i]] == 6:
                brd.Matrix[bomb.r + dr[i], bomb.c + dc[i]] = 0
        flag = 0
        bomb.is_active = False
        if bm.is_alive == False and bm.no_of_life > 0:
            bm.no_of_life -= 1
            self.reborn()
        elif bm.is_alive == False and bm.no_of_life == 0:
            self.gameOver()
        for i in brd.enemies:
            if i.is_alive:
                flag = 1
        if flag == 0 and self.level == 3:
            self.gameWon()
        elif flag == 0:
            self.changeLevel()
        return

    def main(self):
        global dict
        startTime = time.time()
        keycode = 0
        bombCount = -1
        explosionCount = 0
        while True:
            key = getch()
            ##################################### Player movements
            '''
            Press w : UP
            Press s : Down
            Press a : Left
            Press d : Right
            '''
            if (key != None):
                keycode = ord(key)
                if keycode == ord('a'): #For moving Left
                    self.move(0, -1)
            
                elif keycode == ord('s'): #For moving down
                    self.move(1, 0)

                elif keycode == ord('w'): #For moving UP
                    self.move(-1, 0)

                elif keycode == ord('d'): #For moving Right
                    self.move(0, 1)

                elif keycode == ord('b'): # For Planting bomb
                    if bomb.is_active == False:
                        bomb.create_bomb(bm.r, bm.c)
                        bomb.is_active = True


                elif keycode == ord('q'): #For quiting
                    exit()

            if bomb.is_active:
                if int(time.time() - bomb.created_time) <= 2:
                    brd.Matrix[bomb.r, bomb.c] = 3
                if int(time.time() - bomb.created_time) == 1:
                    del dict[3]
                    dict[3] = ["0000", "red"]
                elif int(time.time() - bomb.created_time) == 2:
                    del dict[3]
                    dict[3] = ["1111", "red"]
                    bombCount = -1
                    bomb.explosion()


            if bomb.is_explosion_active:
                explosionCount += 1
                if explosionCount >= 3:
                    explosionCount = 0
                    self.clean_explosion()

            ############################### Move Enemy

            for i in brd.enemies:
                if i.is_alive:
                    i.enemy_move()
                    if bm.is_alive == False and bm.no_of_life > 0:
                        bm.no_of_life -= 1
                        if bomb.is_active:
                            bomb.is_active = False
                            brd.Matrix[bomb.r, bomb.c] = 0
                            if bomb.is_explosion_active:
                                self.clean_explosion()
                            else: self.reborn()
                        break
                    elif bm.is_alive == False and bm.no_of_life == 0:
                        self.gameOver()

            ############################## Print the board
            self.print_board()


game = Play()
game.create_enemies()
game.print_board()
game.main()
