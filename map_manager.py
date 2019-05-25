import math
import numpy
import matplotlib.pyplot as plt

class my_map(object):

    def __init__(self, x_size, y_size):
        self.map_matrix = numpy.zeros((x_size, y_size))
        #self.map_matrix = [[0 for x in range(x_size)] for y in range(y_size)] 
        for i in range (0, x_size-1):
            for j in range (0, y_size-1):
                self.map_matrix[i, j] = 0.5
        self.x_size = x_size
        self.y_size = y_size
        self.poprz_x_1 = 0
        self.poprz_y_1 = 0
        self.poprz_x_2 = 0
        self.poprz_y_2 = 0
        self.poprz_x_3 = 0
        self.poprz_y_3 = 0
        self.map_reset()

    def get_map(self):
        return self.map_matrix

    def map_reset(self):
        for i in range(self.x_size):
            for j in range(self.y_size):
                self.map_matrix[i, j] = 0.5

    def get_value(self, x_pos, y_pos):
        return '{}'.format(self.map_matrix[x_pos, y_pos]) 

    def dane_na_mape(self, dane, pos):

        #self.rysuj_kreske(100, 195, 627, 320)

        rx = float(pos[0])
        ry = float(pos[1])
        ra = float(pos[2])
        n1 = float(dane[1])
        n2 = float(dane[2])
        n3 = float(dane[3])
        na = float(dane[0])
        if n1 > 0 and n1 < 800:
            dot1_x = round(rx+math.cos(math.radians(ra+na-90))*n1)
            dot1_y = round(ry+math.sin(math.radians(ra+na-90))*n1)
            self.map_matrix[dot1_x,dot1_y] = 1
            if self.poprz_x_1 > 0 and self.poprz_x_1 < 2000:
                if self.poprz_y_1 > 0 and self.poprz_y_1 < 2000:
                    self.rysuj_kreske(self.poprz_x_1, self.poprz_y_1, dot1_x, dot1_y)

            l1 = round(math.sqrt((rx-dot1_x)**2+(ry-dot1_y)**2))-1
            for i in range (0,l1):
                self.rysuj_puste(i, ra+na-90, rx, ry)

            self.poprz_x_1 = dot1_x
            self.poprz_y_1 = dot1_y



        if n2 > 0 and n2 < 800:
            dot2_x = round(rx+math.cos(math.radians(ra+na))*n2)
            dot2_y = round(ry+math.sin(math.radians(ra+na))*n2)
            self.map_matrix[dot2_x,dot2_y] = 1
            if self.poprz_x_2 > 0 and self.poprz_x_2 < 2000:
                if self.poprz_y_2 > 0 and self.poprz_y_2 < 2000:
                    self.rysuj_kreske(self.poprz_x_2, self.poprz_y_2, dot2_x, dot2_y)

            l2 = round(math.sqrt((rx-dot2_x)**2+(ry-dot2_y)**2))-1
            for j in range (0,l2):
                self.rysuj_puste(j, ra+na, rx, ry)

            self.poprz_x_2 = dot2_x
            self.poprz_y_2 = dot2_y


        if n3 > 0 and n3 < 800:
            dot3_x = round(rx+math.cos(math.radians(ra+na+90))*n3)
            dot3_y = round(ry+math.sin(math.radians(ra+na+90))*n3)
            self.map_matrix[dot3_x,dot3_y] = 1
            if self.poprz_x_3 > 0 and self.poprz_x_3 < 2000:
                if self.poprz_y_3 > 0 and self.poprz_y_3 < 2000:
                    self.rysuj_kreske(self.poprz_x_3, self.poprz_y_3, dot3_x, dot3_y)

            l3 = round(math.sqrt((rx-dot3_x)**2+(ry-dot3_y)**2))-1
            for k in range (0,l3):
                self.rysuj_puste(k, ra+na+90, rx, ry)

            self.poprz_x_3 = dot3_x
            self.poprz_y_4 = dot3_y


       


        
        
        




    def rysuj_puste(self, wa, a, rx, ry):
        ws_x = round(rx+math.cos(math.radians(a))*wa)
        ws_y = round(ry+math.sin(math.radians(a))*wa)
        self.map_matrix[ws_x,ws_y] = 0

    def rysuj_kreske(self, p_x, p_y, t_x, t_y):
        if p_x-t_x != 0 and abs(t_x-p_x) < 500 and abs(t_y-p_y) < 500:
            dlugosc = math.ceil(math.sqrt((t_x-p_x)**2+(t_y-p_y)**2))
            wsp_a = (p_y-t_y)/(p_x-t_x)
            wsp_b = (p_x*p_y-t_x*p_y)/(p_x-t_x)
            for i in range (p_x, t_x):
                temp = abs(t_x-i)
                nx = round(t_x-temp)
                ny = round(wsp_a*nx+wsp_b)
                if nx > 0 and nx < 2000:
                    if ny > 0 and ny < 2000:
                        self.map_matrix[nx, ny] = 1

    def rysuj_mape(self):
        plt.matshow(self.map_matrix)
        plt.show()