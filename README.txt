Language: Python 2.7
Python Libraries Needed:
	- numpy
	- termcolor

How to run:
    - python run.py

Features:
	- Different Characters have different color
	- Scoring: 
		* Kill Enemies: 100 pts
		* Destroy Bricks: 20 pts
	- There are a total of 4 lives per game
	- 2 types of enemies:
		* Enemy[RED]: Will move randomly 
		* Smart_enemy[Top: Yellow, Bottom: Red]: Will move towards the bomberman and appear in level-2 and level-3 only.
	- 3 types of levels:
		* Level 1: Few enemies, only single(Enemy) type of enemy is present
		* Level 2: More enemies, Both Smart_enemys and Enemy are present
		* Level 3: Lots of enemies, All the types of enemies are present
	- Input timeout: If no input is given in 1 second then the input timeouts and the next frame is printed.

Code Features:
    - Highly modular code (Most of the core game play elements have been separated into different modules)
    - Encapsulation (The various game play elements have been made into classes. eg Bomberman, Bomb etc)
    - Inheritance (Has been used whenever required. eg. Bomberman and Enemy classes inherits from Person class, Smart_enemy inherits from Enemy)
    - Polymorphism (eg. check_move of Person class has been overridden by Enemy as well as Bomberman class)
    - Certain important variables have been placed in config.py and are used everywhere by importing them.
      Thus, changing values in just one place will reflect in the whole game.
    - Conforms to the PEP8 coding standards

Symbols:
	- % : Wall
	- # : Bricks
	- Yellow color character: Bomberman
	- Red : Enemy
    - [Top: Yellow, Bottom: Red] : Smart_enemys
	- Red Numbers : Bomb 
    - [eeee] : Denotes Explosion Area
    
Controls:
	- a: left
	- s: down
	- d: right
	- w: up
	- b: plant bomb
	- q: quit game

Some important rules:
    - Enemy or Player can move in Explosion area and they will destroy if they do so.
    - Smart enemies can't move in explosion
    - No one can move on the Bomb after planting the bomb by bomberman
