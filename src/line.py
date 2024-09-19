
class Line:
    def __init__(self, point1,point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas,fill_color="black",width=2):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y,fill=fill_color,width=width)