from line import Line
from point import Point
import time
class Cell:
    global CELL_WIDTH ,O_TUNE,X_TUNE
    CELL_WIDTH =8 
    O_TUNE = 10
    X_TUNE = 10
    def __init__(self,x1,x2,y1,y2,win) -> None:
        
        self.__is_x = None
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.win = win

    def set_val(self,val):
        if val == "x":
            self.__is_x = True
        else:
            self.__is_x = False

    def get_val(self):
        return self.__is_x
    
    def draw(self,has_left= True,has_right = True,has_bottom= True,has_top = True):
        if has_left:
            self.win.draw_line(Line(point1=Point(self._x1,self._y1),point2=Point(self._x1,self._y2)),CELL_WIDTH)
        if has_top:
            self.win.draw_line(Line(point1=Point(self._x1,self._y1),point2=Point(self._x2,self._y1)),CELL_WIDTH)
        if has_bottom:
            
            self.win.draw_line(Line(point1=Point(self._x1,self._y2),point2=Point(self._x2,self._y2)),CELL_WIDTH)
        if has_right:
            self.win.draw_line(Line(point1=Point(self._x2,self._y1),point2=Point(self._x2,self._y2)),CELL_WIDTH)

    def fill_with_X(self):
        line1 = Line(point1=Point(self._x1+X_TUNE,self._y1+X_TUNE),point2=Point(self._x2-X_TUNE,self._y2-X_TUNE))
        line2 = Line(point1=Point(self._x1+X_TUNE,self._y2-X_TUNE),point2=Point(self._x2-X_TUNE,self._y1+X_TUNE))
        self.win.draw_line(line1,width=6,fill_color = "red")
        self._animate()
        self.win.draw_line(line2,width=6,fill_color = "red")
        self._animate()


    def fill_with_O(self):
        self.win.draw_oval(self._x1+O_TUNE,self._y1+O_TUNE,self._x2-O_TUNE,self._y2-O_TUNE)
        self._animate()
    

    def _animate(self):
        self.win.redraw()
        time.sleep(0.30)   