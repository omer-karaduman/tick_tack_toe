from board import Board
from window import Window
from tkinter import *
from tkinter import ttk
from line import Line
from point import Point
import time

class Game:
    def __init__(self):
        self.win = Window(720,720)
        self.board =Board(self.win)
        self.surface = self.board.create_board()
        self.mouse_listener = 0
        self.turn_player= True


    def start_game(self):
        self.win.welcome_label()
        self.win.add_button_2player(self.play)
        
        self.win.add_button_pc(self.play_with_pc)

        self.surface[0][0].fill_with_O()
        time.sleep(0.10)
        self.surface[1][1].fill_with_X()
        time.sleep(0.10)
        self.surface[2][0].fill_with_X()
        time.sleep(0.10)
        self.surface[0][1].fill_with_O()
        time.sleep(0.10)
        self.surface[2][2].fill_with_X()
        
    def on_mouse_click(self,event):
        x, y = event.x, event.y
        if self.board.board_width < x < self.board.board_width+self.board.cell_size*3 and self.board.board_height < y <self.board.board_height+3*self.board.cell_size:
           position_horizontal = ((x-self.board.board_width) // self.board.cell_size) 
           position_vertical = (y-self.board.board_height) // self.board.cell_size
           cell = self.surface[position_horizontal][position_vertical]
           if not  cell.is_fill():          
            return position_horizontal,position_vertical
        return -1,-1

    def fill_with_o_x(self,event):
        if self.check_winner() is not False:  
            return
        horizontal,vertical = self.on_mouse_click(event)
        if horizontal == -1:
            return
        if self.mouse_listener%2 == 0:
            self.win.canvas.config(cursor="circle")
            self.win.turn_label("O")
            self.surface[horizontal][vertical].fill_with_X()
        else:
            self.win.canvas.config(cursor="cross")
            self.win.turn_label("X")
            self.surface[horizontal][vertical].fill_with_O()
        self.mouse_listener+=1
        if self.check_winner() !=None:
            if self.check_winner():
                if self.surface[horizontal][vertical].get_val():
                    self.win.winner_label("X")
                else:
                    self.win.winner_label("O")
                self.win.canvas.config(cursor="")
                self.win.add_button_2player(self.play)
                self.win.add_button_pc(self.play_with_pc)
                


    def play(self):
        time.sleep(1)
        self.win.canvas.delete("all")
        self.board = Board(self.win)
        self.mouse_listener = 0
        self.surface = self.board.create_board()
        self.win.canvas.config(cursor="cross")
        self.win.canvas.bind("<Button>", self.fill_with_o_x)
    
    
    def check_winner(self):
        for row in self.surface:
            if row[0].get_val() == row[1].get_val() == row[2].get_val() and row[0].get_val() != None:
                point1 = Point((row[0]._x1+row[0]._x2)//2,(row[0]._y1))
                point2 = Point((row[2]._x1+row[2]._x2)//2,(row[2]._y2))
                self.win.draw_line(Line(point1,point2),width=10,fill_color="red")
                return True
            
        for col in range(3):
            if self.surface[0][col].get_val() == self.surface[1][col].get_val() == self.surface[2][col].get_val() and self.surface[0][col].get_val() != None:
                point3 = Point((self.surface[0][col]._x1),((self.surface[0][col]._y1+self.surface[0][col]._y2)//2))
                point4 = Point((self.surface[2][col]._x2),((self.surface[2][col]._y1+self.surface[2][col]._y2))//2)
                self.win.draw_line(Line(point3,point4),width=10,fill_color="red")
                return True
        
        if self.surface[0][0].get_val() == self.surface[1][1].get_val() == self.surface[2][2].get_val() and self.surface[0][0].get_val() != None:
            point5 = Point(self.surface[0][0]._x1,self.surface[0][0]._y1)
            point6 = Point(self.surface[2][2]._x2,self.surface[2][2]._y2)
            self.win.draw_line(Line(point5,point6),width=10,fill_color="red")
            return True
        
        if self.surface[0][2].get_val() == self.surface[1][1].get_val() == self.surface[2][0].get_val() and self.surface[0][2].get_val() != None:
            point7 = Point(self.surface[0][2]._x1,self.surface[0][2]._y2)
            point8 = Point(self.surface[2][0]._x2,self.surface[2][0]._y1)
            self.win.draw_line(Line(point7,point8),width=10,fill_color="red")
            return True
        
        if self.board.is_board_full():
            self.win.draw_label()
            time.sleep(1)
            self.win.add_button_2player(self.play)
            self.win.add_button_pc(self.play_with_pc)
            return None
        return False
    
    def fill_with_x_vs_pc(self,event):
        if self.check_winner() is not False:  
            return

        if self.turn_player:
            horizontal,vertical = self.on_mouse_click(event)
            if horizontal == -1:
                return
            self.win.canvas.config(cursor="circle")
            self.win.turn_label("O")
            self.surface[horizontal][vertical].fill_with_X()
            self.turn_player = False
            if self.check_winner() !=None:
                if self.check_winner():
                    if self.surface[horizontal][vertical].get_val():
                        self.win.winner_label("X")
                    else:
                        self.win.winner_label("O")
                    self.win.canvas.config(cursor="")
                    self.win.add_button_2player(self.play)
                    self.win.add_button_pc(self.play_with_pc)
            self.win.canvas.update()
            self.pc_algo()
        
        else:
            return
        
            

    def play_with_pc(self):
        time.sleep(1)
        self.win.canvas.delete("all")
        self.board = Board(self.win)
        self.mouse_listener = 0
        self.surface = self.board.create_board()
        self.turn_player = True
        self.win.canvas.config(cursor="cross")
        self.win.canvas.bind("<Button>", self.fill_with_x_vs_pc)

    def pc_algo(self):
        if self.check_winner() is not False:
            return
        is_filled = False

        if not is_filled and self.surface[1][1].get_val() == None:
            self.surface[1][1].fill_with_O()
            is_filled = True
        if not is_filled:

            for i in range(3):
                if (self.surface[i][0].get_val() and self.surface[i][1].get_val()) and not self.surface[i][2].is_fill():
                    self.surface[i][2].fill_with_O()
                    is_filled = True
                    break
                if (self.surface[i][0].get_val() and self.surface[i][2].get_val()) and not self.surface[i][1].is_fill():
                    self.surface[i][1].fill_with_O()
                    is_filled = True
                    break
                if self.surface[i][1].get_val() and self.surface[i][2].get_val() and not self.surface[i][0].is_fill():
                    self.surface[i][0].fill_with_O()
                    is_filled = True
                    break
        if not is_filled:
            for i in range(3):
                    if (self.surface[0][i].get_val() and self.surface[1][i].get_val()) and not self.surface[2][i].is_fill():
                        self.surface[2][i].fill_with_O()
                        is_filled = True
                        break
                    if (self.surface[0][i].get_val() and self.surface[2][i].get_val()) and not self.surface[1][i].is_fill():
                        self.surface[1][i].fill_with_O()
                        is_filled = True
                        break
                    if self.surface[1][i].get_val() and self.surface[2][i].get_val() and not self.surface[0][i].is_fill():
                        self.surface[0][i].fill_with_O()
                        is_filled = True
                        break
        if not is_filled:
            if self.surface[0][0].get_val() and self.surface[1][1].get_val() and not self.surface[2][2].is_fill():
                self.surface[2][2].fill_with_O()
                is_filled = True
            elif self.surface[0][0].get_val() and self.surface[2][2].get_val() and not self.surface[1][1].is_fill():
                self.surface[1][1].fill_with_O()
                is_filled = True
            elif self.surface[1][1].get_val() and self.surface[2][2].get_val() and not self.surface[0][0].is_fill():
                self.surface[0][0].fill_with_O()
                is_filled = True
            elif self.surface[0][2].get_val() and self.surface[1][1].get_val() and not self.surface[2][0].is_fill():
                self.surface[2][0].fill_with_O()
                is_filled = True
            elif self.surface[0][2].get_val() and self.surface[2][0].get_val() and not self.surface[1][1].is_fill():
                self.surface[1][1].fill_with_O()
                is_filled = True
            elif self.surface[2][0].get_val() and self.surface[1][1].get_val() and not self.surface[0][2].is_fill():
                self.surface[0][2].fill_with_O()
                is_filled = True

        if not is_filled and self.surface[1][0].get_val() == None:
            self.surface[1][0].fill_with_O()
            is_filled = True
        if not is_filled and self.surface[1][2].get_val() == None:
            self.surface[1][2].fill_with_O()
            is_filled = True
        if not is_filled and self.surface[0][1].get_val() == None:
            self.surface[0][1].fill_with_O()
            is_filled = True
        if not is_filled and self.surface[2][1].get_val() == None:
            self.surface[2][1].fill_with_O()
            is_filled = True
        
        self.win.canvas.config(cursor="cross")
        self.win.turn_label("X")
        self.turn_player =True
        
        if self.check_winner():
            
            self.win.winner_label("PC")
            time.sleep(2)
            self.win.canvas.config(cursor="")
            self.win.add_button_2player(self.play)
            self.win.add_button_pc(self.play_with_pc)