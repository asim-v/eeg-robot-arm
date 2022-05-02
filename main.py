import tkinter as tk
from tkinter import ttk
import serial
import time

#open arduinoial port
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
print("Connected succesfully at: ",arduino.name)  

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


DEFAULT_PARAMS = [60,135,135,0,0,0]


def get_value_of(slider):
    return '{: .2f}'.format(slider.get())

def send_to_robot(data=None):
    if data!=None:
        data = str(data)
        data = data[1:len(data)-1]+'\n'
        response = b''
        while response == b'' or response == b'Error\r\n':
            
            arduino.write(bytes(data, 'utf-8'))
            time.sleep(0.05)
            response = arduino.readline()
            print('Sending default data...',data,'response:',response)
        print('Sent default data:',data)
        print(response) 

    else:
        try:
            to_robot = str(int(float(get_value_of(first_slider))))+','+str(int(float(get_value_of(second_slider))))+','+str(int(float(get_value_of(third_slider))))+','+str(int(float(get_value_of(fourth_slider))))+','+str(int(float(get_value_of(fifth_slider))))+','+str(int(float(get_value_of(sixth_slider))))+'\n'        
            arduino.write(bytes(to_robot, 'utf-8'))
            time.sleep(0.05)
            response = arduino.readline()
            print(response)
        except:
            print('Loading signals...')



first_slider = tk.DoubleVar()
def first_slider_changed(event):
    first_slider_label.configure(text=get_value_of(first_slider))   
    send_to_robot()     
# label for the first slider
first_slider_label = ttk.Label(root,text='Angulo:')
first_slider_label.grid(column=0,row=0,sticky='w')
#  first slider
first_slider = ttk.Scale(
    root,
    from_=0,
    to=165,
    orient='horizontal',  # vertical
    command=first_slider_changed,
    variable=first_slider
)
first_slider.set(DEFAULT_PARAMS[0])
first_slider.grid(column=1,row=0,sticky='we') 



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
    to=135,
    orient='horizontal',  # vertical
    command=second_slider_changed,
    variable=second_slider
)
second_slider.set(DEFAULT_PARAMS[1])
second_slider.grid(column=1,row=1,sticky='we') 



third_slider = tk.DoubleVar()
def third_slider_changed(event):
    third_slider_label.configure(text=get_value_of(third_slider))
    send_to_robot()
# label for the first slider
third_slider_label = ttk.Label(root,text='Codo:')
third_slider_label.grid(column=0,row=2,sticky='w')
#  first slider
third_slider = ttk.Scale(
    root,
    from_=0,
    to=135,
    orient='horizontal',  # vertical
    command=third_slider_changed,
    variable=third_slider
)
third_slider.set(DEFAULT_PARAMS[2])
third_slider.grid(column=1,row=2,sticky='we') 


fourth_slider = tk.DoubleVar()
def fourth_slider_changed(event):
    fourth_slider_label.configure(text=get_value_of(fourth_slider))
    send_to_robot()
# label for the first slider
fourth_slider_label = ttk.Label(root,text='MuñecaA:')
fourth_slider_label.grid(column=0,row=3,sticky='w')
#  first slider
fourth_slider = ttk.Scale(
    root,
    from_=0,
    to=125,
    orient='horizontal',  # vertical
    command=fourth_slider_changed,
    variable=fourth_slider
)
fourth_slider.set(DEFAULT_PARAMS[3])
fourth_slider.grid(column=1,row=3,sticky='we') 


fifth_slider = tk.DoubleVar()
def fifth_slider_changed(event):
    fifth_slider_label.configure(text=get_value_of(fifth_slider))
    send_to_robot()
# label for the first slider
fifth_slider_label = ttk.Label(root,text='MuñeacaB:')
fifth_slider_label.grid(column=0,row=4,sticky='w')
#  first slider
fifth_slider = ttk.Scale(
    root,
    from_=0,
    to=135,
    orient='horizontal',  # vertical
    command=fifth_slider_changed,
    variable=fifth_slider
)
fifth_slider.set(DEFAULT_PARAMS[4])
fifth_slider.grid(column=1,row=4,sticky='we') 


sixth_slider = tk.DoubleVar()
def sixth_slider_changed(event):
    sixth_slider_label.configure(text=get_value_of(sixth_slider))
    send_to_robot()
# label for the first slider
sixth_slider_label = ttk.Label(root,text='Pinza:')
sixth_slider_label.grid(column=0,row=5,sticky='w')
#  first slider
sixth_slider = ttk.Scale(
    root,
    from_=20,
    to=75,
    orient='horizontal',  # vertical
    command=sixth_slider_changed,
    variable=sixth_slider
)
sixth_slider.set(DEFAULT_PARAMS[5])
sixth_slider.grid(column=1,row=5,sticky='we') 



# send_to_robot(DEFAULT_PARAMS)
root.mainloop()
