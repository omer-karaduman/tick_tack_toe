from tkinter import *
from tkinter import ttk


class Window:
    def __init__(self,width,height):
        self.__root= Tk()
        self.__root.title("Tik Tak Toe")
        self.__root.resizable(False,False)
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)

        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
        
    
    def get_root(self):
        return self.__root

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

    def welcome_label(self):
        label = Label(self.__root, text="WELCOME", font=("Arial", 20, "bold"), foreground="#0056b3", background="white", borderwidth=0, relief="groove")
        self.canvas.create_window(350, 100, window=label)
        
    def add_button_2player(self,command):
        button = Button(self.__root, text="2 Player",font=("Arial", 15, "bold"),borderwidth=2, command=lambda: command(),activebackground="#0056b3",
                        activeforeground="#ffffff")
        self.canvas.create_window(250,165, window=button) 
    def add_button_pc(self,command):
        button = Button(self.__root, text="Play with PC",font=("Arial", 15, "bold"),borderwidth=2, command=lambda: command(),activebackground="#0056b3",
                        activeforeground="#ffffff")
        self.canvas.create_window(450,165, window=button)
    def draw_label(self):
        label = Label(self.__root, text="DRAW!!!", font=("Arial", 40, "bold"), foreground="#344b52", background="white", borderwidth=0, relief="groove")
        self.canvas.create_window(350, 100, window=label)
    def turn_label(self,who_turn):
        text= f"{who_turn} Turn!!"
        label = Label(self.__root, text=text, font=("Arial", 30, "bold"), foreground="#6e9ccc", background="white", borderwidth=0, relief="groove")
        self.canvas.create_window(350, 100, window=label)    
    
    def winner_label(self,winner):
        text = f"{winner} WIN!!"
        label = Label(self.__root, text=text, font=("Arial", 40, "bold"), foreground="#0056b3", background="white", borderwidth=0, relief="groove")
        self.canvas.create_window(350, 100, window=label)  