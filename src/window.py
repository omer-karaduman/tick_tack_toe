from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self,width,height):
        self.__root= Tk()
        self.__root.title("Tik Tak Toe")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Closed...")

    def close(self):
        self.running = False

    def draw_line(self,line,width,fill_color="black"):
        line.draw(self.canvas,fill_color,width=width)

    def draw_oval(self,x1,y1,x2,y2):
        self.canvas.create_oval(x1, y1, x2, y2, fill='white', outline='gray', width=6)