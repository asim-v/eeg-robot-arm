import tkinter as tk
from tkinter import ttk
import serial
import time

#open arduinoial port
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
print(arduino.name)  

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider first_slider
first_slider = tk.DoubleVar()


def get_value_of(slider):
    return '{: .2f}'.format(slider.get())

def send_to_robot():
    to_robot = str(int(float(get_value_of(first_slider))))+','+str(int(float(get_value_of(second_slider))))+','+str(int(float(get_value_of(third_slider))))+',0,0,0\n'
    arduino.write(bytes(to_robot, 'utf-8'))
    time.sleep(0.05)
    response = arduino.readline()
    print(response)



first_slider = tk.DoubleVar()
def first_slider_changed(event):
    first_slider_label.configure(text=get_value_of(first_slider))   
    send_to_robot()     
# label for the first slider
first_slider_label = ttk.Label(root,text='Angulo:')
first_slider_label.grid(column=0,row=0,sticky='w')
#  first slider
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=first_slider_changed,
    variable=first_slider
)
slider.grid(column=1,row=0,sticky='we') 



second_slider = tk.DoubleVar()
def second_slider_changed(event):
    second_slider_label.configure(text=get_value_of(second_slider))
    send_to_robot()
# label for the first slider
second_slider_label = ttk.Label(root,text='Levantamiento:')
second_slider_label.grid(column=0,row=1,sticky='w')
#  first slider
second_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=second_slider_changed,
    variable=second_slider
)
second_slider.grid(column=1,row=1,sticky='we') 



third_slider = tk.DoubleVar()
def second_slider_changed(event):
    third_slider_label.configure(text=get_value_of(third_slider))
    send_to_robot()
# label for the first slider
third_slider_label = ttk.Label(root,text='Codo:')
third_slider_label.grid(column=0,row=2,sticky='w')
#  first slider
third_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=second_slider_changed,
    variable=second_slider
)
third_slider.grid(column=1,row=2,sticky='we') 



root.mainloop()