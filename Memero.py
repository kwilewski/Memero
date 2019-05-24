import serial
import robotXY
import map_manager
import time
import tkinter as tk
import matplotlib as plt
import numpy

HEIGHT = 700
WIDTH = 700
map_width = 2000
map_height = 2000
mMemero = robotXY.robot_xy(map_height/2, map_width/2, 0)
mMap = map_manager.my_map(map_width,map_height)

try:
        ser = serial.Serial('COM5',9600, timeout = 1)
        time.sleep(3)
        print('Połączono')
except:
        print('Nie udało się nawiązać połączenia')

def create_map():
    mMemero = robotXY.robot_xy(map_height/2, map_width/2, 0)
    print(mMemero.position())
    mMap = map_manager.my_map(map_width,map_height)

def w_lewo():
    ser.write(b'a')

def w_prawo():
    ser.write(b'd')

def do_przodu():
    ser.write(b'w')
    get_data_memero()

def do_tylu():
    ser.write(b's')

def get_pos():
    print(mMemero.position())

def get_data_memero():
    for i in range (90):
        z_ard = ser.readline()
        if z_ard != 0xf0 or z_ard != 0xf8:
            str_ard = z_ard.decode()
            str_ard = str_ard.rstrip('\n')
            dane = str_ard.split('|')
            dane2 = mMemero.position().split('|')
            mMap.dane_na_mape(dane, dane2)
            print(dane)
        #print(str_ard)

    mp = numpy.zeros(map_width)
    mm = mMap.get_map()
    print(max(mm))
    for n in range (0, 1999):
        for m in range (0, 1999):
            mp[n, m] = mm[n][m]
    plt.matshow(mp)
    plt.show()







while 1:
    print("podaj komendę:")
    a = input()
    if a == 'c':
        create_map()
    elif a == 'w':
        do_przodu()
        
    elif a == 'a':
        w_lewo()
    elif a == 'd':
        w_prawo()
    elif a == 's':
        do_tylu()
    elif a == 'p':
        get_pos()











