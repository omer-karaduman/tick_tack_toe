from tkinter import *
from tkinter import ttk
from window import Window

from point import Point
from line import Line
from board import Board
from game import Game
def main():
    game = Game()
    game.test()

    game.win.wait_for_close()
main()