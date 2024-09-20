from cell import Cell
import time
class Board:
    
    def __init__(self,win,cell_size=100):
        self._win = win
        self.__surface= [[None for i in range(3)] for j in range(3)]
        self.board_width = 200
        self.board_height = 250
        self.cell_size = cell_size
    
    def create_board(self):
        for i in range(3):
            for j in range(3):
                x1 = self.board_width+i*self.cell_size
                x2 = x1 + self.cell_size
                y1 = self.board_height+j*self.cell_size
                y2 = y1 +self.cell_size
                self.__surface[i][j] = Cell(x1,x2,y1,y2,self._win)
                
                if i ==0:
                    if j == 0:
                        self.__surface[i][j].draw(has_top = False,has_left = False)
                    elif j ==2:
                        self.__surface[i][j].draw(has_bottom = False,has_left = False)
                    else:
                        self.__surface[i][j].draw(has_left = False)
                elif i==1:
                    if j==0:
                        self.__surface[i][j].draw(has_top = False)
                    elif j==2:
                        self.__surface[i][j].draw(has_bottom=False)
                    else:
                        self.__surface[i][j].draw()
                elif i ==2:
                    if j ==0:
                        self.__surface[i][j].draw(has_right = False,has_top = False)
                    elif j== 1:
                        self.__surface[i][j].draw(has_right = False)
                    else:
                        self.__surface[i][j].draw(has_right= False,has_bottom = False)
            
                
                
                self._animate()
        return self.__surface
                
    def _animate(self):
        self._win.redraw()
        time.sleep(0.25)   
       
    def is_board_full(self):
        for row in self.__surface:
            for cell in row:
                if cell.get_val() is None:
                    return False
        return True