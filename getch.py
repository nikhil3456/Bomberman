#!/usr/bin/env python
# import msvcrt
import os, sys
from select import select

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchUnix()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            [i , o ,e] = select([sys.stdin.fileno()],[],[],0.5)
            if i:
                ch = sys.stdin.read(1)
            else:
                ch = None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        # termios.tcsdrain(fd, termios.TCSFLUSH)
        return ch


# class _GetchWindows:
#   def __init__(self):
#     import msvcrt

#   def __call__(self):
#     import msvcrt
#     return msvcrt.getch()

getch = _Getch()
