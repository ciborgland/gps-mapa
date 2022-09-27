from cProfile import label
from tkinter import Scale, font
from tkinter import ttk
from tkinter.ttk import Entry, Label, LabelFrame
from turtle import bgcolor
from matplotlib.ft2font import HORIZONTAL
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkintermapview
import tkinter
import time
import serial
from threading import Thread



ventana = tkinter.Tk()
ventana.geometry('900x820')
ventana.title('Proyectos PROA')

arduino = serial.Serial('/dev/ttyACM0',9600)

isReceive = False 
isRun = True
value = ''
a=''
b=''

def getData():
    time.sleep(1.0)
    arduino.reset_input_buffer()

    while(isRun):
        global isReceive
        global value
        global a
        global b
        value = arduino.readline().decode('ascii')
        isReceive = True
        
        pos = value.index(":")
        label=value[:pos]
        resultado=value[pos+1:]

        if label == 'latitud':
            a=float(resultado)
            print(a)
        if label == 'longitud':
            b=float(resultado)
            print(b)

hilo = Thread(target=getData)
hilo.start()

while isReceive != True:
    #print("OK")
    time.sleep(1)



def buscar():
    map_widget.set_address(my_entry.get())

def salir():
    exit()


my_label = LabelFrame(ventana)
my_label.pack(pady=20)


map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600)


marker_1 = map_widget.set_address("Buenos Aires", marker=True)
marker_1.set_position(a, b)



map_widget.set_position(a,b)
map_widget.set_zoom(20)
map_widget.pack()


my_frame = LabelFrame(ventana)
my_frame.place(x=70,y=680)


my_entry = Entry(my_frame, font=("Helvetica", 28), background='yellow')
my_entry.grid(row=0, column=0, pady=20, padx=10)


boton2 = tkinter.Button(ventana, text = 'Mostrar Localización', height='2', width='20', command = buscar)
boton2.place(x=640,y=720)


ventana.mainloop()
