import tkinter as tk
from tkinter import ttk
import serial
import time
from timepressedbutton import *

#open arduinoial port
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
print("Connected succesfully at: ",arduino.name)  

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')

#memory_file = open('base_servo_memory.txt','w+')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


DEFAULT_PARAMS = [60,135,135,0,0,20]


def get_value_of(slider):
    return '{: .2f}'.format(slider.get())

def send_to_robot(data=None):

    '''
        Inputs:
            None -> Grabs the data from the sliders
            Specified -> Grab list of the format [1,2,3,4,5,6] <- Formatting and encoding
            'Reset' -> Work in progress
    '''

    def send_data(data):
        arduino.write(bytes(data, 'utf-8'))
        time.sleep(0.05)
        response = arduino.readline()
        return(response)

    if data!=None:
        data = str(data)
        if data == 'reset':send_data(data)
        else:
            data = data[1:len(data)-1]+'\n'
            response = b''
            responses = ''
            #Sening signals until the arduino is prepared
            while response == b'' or response == b'Error\r\n' :
                response = send_data(data)
            #Recieving data
            while response.decode('utf-8') not in responses:
                response = send_data(data)
                responses += response.decode('utf-8')
                # print('--> Sending default data...',data,' <-- Response:',response)  
                # Prints which data is being send and what is the response
            time.sleep(0.5)
            print('<-- Sent:',response)


    else:
        try:
            to_robot = str(int(float(get_value_of(first_slider))))+','+str(int(float(get_value_of(second_slider))))+','+str(int(float(get_value_of(third_slider))))+','+str(int(float(get_value_of(fourth_slider))))+','+str(int(float(get_value_of(fifth_slider))))+','+str(int(float(get_value_of(sixth_slider))))+'\n'        
            # to_robot = str(int(float(get_value_of(first_slider))))+',91,'+str(int(float(get_value_of(third_slider))))+','+str(int(float(get_value_of(fourth_slider))))+','+str(int(float(get_value_of(fifth_slider))))+','+str(int(float(get_value_of(sixth_slider))))+'\n'
            # print(send_data(to_robot)) 
            # Prints response
            send_data(to_robot)
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
first_slider.grid(column=1,row=0,sticky='we',columnspan=3) 




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
second_slider.grid(column=1,row=1,sticky='we',columnspan=3) 


# def stop():
#     data = [int(float(get_value_of(first_slider))),90,int(float(get_value_of(third_slider))),int(float(get_value_of(fourth_slider))),int(float(get_value_of(fifth_slider))),int(float(get_value_of(sixth_slider)))]
#     send_to_robot(data)

# def move_left():
#     data = [int(float(get_value_of(first_slider))),180,int(float(get_value_of(third_slider))),int(float(get_value_of(fourth_slider))),int(float(get_value_of(fifth_slider))),int(float(get_value_of(sixth_slider)))]
#     send_to_robot(data)
# button_right =  TimePressedButton(root,text="Left",set_up_command=stop,set_down_command=move_left,print_duration=True,memory_file=memory_file)
# button_right.grid(column=2,row=1,sticky='we') 

# def move_right():
#     data = [int(float(get_value_of(first_slider))),0,int(float(get_value_of(third_slider))),int(float(get_value_of(fourth_slider))),int(float(get_value_of(fifth_slider))),int(float(get_value_of(sixth_slider)))]
#     send_to_robot(data)
# button_left = TimePressedButton(root,text="Right",set_up_command=stop,set_down_command=move_right,print_duration=True,memory_file=memory_file)
# button_left.grid(column=3,row=1,sticky='we') 






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
third_slider.grid(column=1,row=2,sticky='we',columnspan=3) 


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
fourth_slider.grid(column=1,row=3,sticky='we',columnspan=3) 


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
fifth_slider.grid(column=1,row=4,sticky='we',columnspan=3) 


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
    to=100,
    orient='horizontal',  # vertical
    command=sixth_slider_changed,
    variable=sixth_slider
)
sixth_slider.set(DEFAULT_PARAMS[5])
sixth_slider.grid(column=1,row=5,sticky='we',columnspan=3) 



def reset_default_position():
    try:

        #grabs the memory time it rotated and rotates on the opposite direction
        # memory_file.seek(0)
        # rotation_time_string = memory_file.read()
        # if rotation_time_string != '':
        #     rotation_time = round(float(rotation_time_string),5)
        #     # print('Time going back:-',float(rotation_time),'-')
        #     t_end = time.time() + abs(rotation_time)
        #     if rotation_time > 0:
        #         while time.time() < t_end:  
        #             move_left()
        #     elif rotation_time < 0:
        #         while time.time() < t_end:  
        #             move_right()
        #     # print('Deleting')
        #     memory_file.truncate(0)




        first_slider.set(DEFAULT_PARAMS[0])
        second_slider.set(DEFAULT_PARAMS[1])            
        third_slider.set(DEFAULT_PARAMS[2])
        fourth_slider.set(DEFAULT_PARAMS[3])
        fifth_slider.set(DEFAULT_PARAMS[4])
        sixth_slider.set(DEFAULT_PARAMS[5])        
        send_to_robot()
        
        
    except exception as e: print("couldn't send default data",e)    
default_button = tk.Button(root, text ="Default Position", command = reset_default_position)
default_button.grid(column=2,row=6,columnspan=2)





# send_to_robot(data=DEFAULT_PARAMS)
def on_closing():

    print('Closing...')
    try:
        send_to_robot(data=DEFAULT_PARAMS)
        time.sleep(1)
        # send_to_robot('reset')
    except: print("couldn't send default data")
    # memory_file.close()
    arduino.close()    
    root.destroy()

# def keep_motor_straight():
#     stop()
#     # root.after(0,keep_motor_straight)

# root.after(0,keep_motor_straight)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
