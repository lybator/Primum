from Actions import *
from Building import *
player = Create(200, 100, 100)

class map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.Matrix = []

    def draw_map(self):
        x = []
        y = []
        for i in range(self.height):
            for j in range(self.width):
                y.append('0')
            x.append(y)
            y = []

        self.Matrix = x


    def draw_matrix(self, matrix):
        for i in matrix:
            print(i)


    def map_add_object(self, object, position:list=[0, 0, 0, 0]):
        #object will have defined exact width and height in Building
        x1 = position[0]
        x2 = position[2]
        y1 = position[1]
        y2 = position[3]
        for i in range(x2-x1 or 1):
            for j in range(y2-y1 or 1):
                self.Matrix[x1+i[y1+j]] = object.get_icon()


