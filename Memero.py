import serial
import robotXY
import map_manager
import time
import tkinter as tk
import matplotlib.pyplot as plt
import numpy

HEIGHT = 700
WIDTH = 700
map_width = 2000
map_height = 2000
mMemero = robotXY.robot_xy(map_height/2, map_width/2, 0)
mMap = map_manager.my_map(map_width,map_height)
connected = False
liczba_krokow = 45


while connected == False:
    try:
            ser = serial.Serial('COM5',9600, timeout = 2)
            time.sleep(3)
            print('Połączono')
            connected = True
    except:
            print('Nie udało się nawiązać połączenia')

def create_map():
    mMemero = robotXY.robot_xy(map_height/2, map_width/2, 0)
    print(mMemero.position())
    mMap = map_manager.my_map(map_width,map_height)

def w_lewo():
    ser.write(b'a')
    mMemero.angle_change(9)

def w_prawo():
    ser.write(b'd')
    mMemero.angle_change(-9)

def do_przodu():
    ser.write(b'w')
    mMemero.x_change(45)

def do_tylu():
    ser.write(b's')
    mMemero.x_change(-45)

def skanuj():
    ser.write(b'm')
    get_data_memero()

def get_pos():
    print(mMemero.position())



def get_data_memero():
    for i in range (liczba_krokow):
        z_ard = ser.readline()
        if z_ard != 0xf0 or z_ard != 0xf8:
            str_ard = z_ard.decode()
            str_ard = str_ard.rstrip('\n')
            dane = str_ard.split('|')
            dane2 = mMemero.position().split('|')
            if len(dane) == 4:
                mMap.dane_na_mape(dane, dane2)
            #print(dane)
        #print(str_ard)

    mMap.rysuj_mape()







while 1:
    print("podaj komendę:")
    a = input()
    if a == 'c':
        create_map()
    elif a == 'w':
        do_przodu()
    elif a =='m':
        skanuj()
    elif a == 'a':
        w_lewo()
    elif a == 'd':
        w_prawo()
    elif a == 's':
        do_tylu()
    elif a == 'p':
        get_pos()











