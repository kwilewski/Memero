import math

class my_map(object):

    def __init__(self, x_size, y_size):
        self.map_matrix = [[0 for x in range(x_size)] for y in range(y_size)] 
        self.x_size = x_size
        self.y_size = y_size
        self.map_reset()

    def get_map(self):
        return self.map_matrix

    def map_reset(self):
        for i in range(self.x_size):
            for j in range(self.y_size):
                self.map_matrix[i][j] = 0.5

    def get_value(self, x_pos, y_pos):
        return '{}'.format(self.map_matrix[x_pos][y_pos]) 

    def dane_na_mape(self, dane, pos):
        rx = float(pos[0])
        ry = float(pos[1])
        ra = float(pos[2])
        n1 = float(dane[1])
        n2 = float(dane[2])
        n3 = float(dane[3])
        na = float(dane[0])
        dot1_x = round(rx+math.cos(math.radians(ra+na-90))*n1+math.sin(math.radians(ra+na-90))*n1)
        dot1_y = round(ry+math.sin(math.radians(ra+na-90))*n1+math.cos(math.radians(ra+na-90))*n1)
        dot2_x = round(rx+math.cos(math.radians(ra+na))*n2+math.sin(math.radians(ra+na-90))*n2)
        dot2_y = round(ry+math.sin(math.radians(ra+na))*n2+math.cos(math.radians(ra+na-90))*n2)
        dot3_x = round(rx+math.cos(math.radians(ra+na+90))*n3+math.sin(math.radians(ra+na+90))*n3)
        dot3_y = round(ry+math.sin(math.radians(ra+na+90))*n3+math.cos(math.radians(ra+na+90))*n3)
        self.map_matrix[dot1_x][dot1_y] = 1
        self.map_matrix[dot2_x][dot2_y] = 1
        self.map_matrix[dot3_x][dot3_y] = 1
        l1 = round(math.sqrt((rx-dot1_x)**2+(ry-dot1_y)**2))-1
        l2 = round(math.sqrt((rx-dot2_x)**2+(ry-dot2_y)**2))-1
        l3 = round(math.sqrt((rx-dot1_x)**2+(ry-dot3_y)**2))-1
        for i in range (0,l1):
            self.rysuj_kropke(i, ra+na-90, rx, ry)
        for j in range (0,l2):
            self.rysuj_kropke(j, ra+na, rx, ry)
        for k in range (0,l2):
            self.rysuj_kropke(k, ra+na+90, rx, ry)







    def rysuj_kropke(self, wa, a, rx, ry):
        ws_x = round(rx+math.cos(wa*a))
        ws_y = round(ry+math.sin(+wa*a))
        self.map_matrix[ws_x][ws_y] = 0