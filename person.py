from config import ROW_SIZE, COL_SIZE, dict
from config import ROW_SIZE, COL_SIZE, dict
from termcolor import colored
import numpy as np

class Person(object):
    """docstring for Person: Common base class for all persons
    Subclasses of Person : Bomberman and Enemy"""
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def checkMove(self):
        pass
