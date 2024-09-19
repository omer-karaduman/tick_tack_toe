from board import Board
from window import Window
from tkinter import *
from tkinter import ttk

class Game:
    def __init__(self):
        self.win = Window(720,720)
        self.board =Board(self.win)
        self.surface = self.board.create_board() 

    def on_mouse_move(self,event):
        x, y = event.x, event.y
        if 50 < x < 150 and 50 < y < 150:
            print("Fare 50x150 alanında!")
        else:
            print(f"Fare pozisyonu: {x}, {y}")
    def test(self):
        self.win.canvas.bind("<Button>", self.on_mouse_move)