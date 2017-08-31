'''
0 = AIR 
1 = BLOCK
2 = DESTRUCTIBLE_BLOCK
3 = PLAYER_BOMB
4 = PLAYER,
5 = ENEMY
6 = EXPLOSION
'''
 
ROW_SIZE = 19 # Keep this odd Integer greater than 11
COL_SIZE = 19 # Keep this odd Integer greater than 11
SCORE_BRICK = 20 # Points for destroying the brick
SCORE_ENEMY = 100 # Points awarded for destroying Enemies
NO_OF_ENEMIES = 3 
dict = {} # contains symbols and colours for entities
dict[0] = ["    ", "white"]
dict[1] = ["%%%%", "white"]
dict[2] = ["####", "magenta"]
dict[3] = ["1111", "red"] ###don't change this
dict[6] = ["eeee", "green"]
