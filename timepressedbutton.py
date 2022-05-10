import tkinter as tk
from tkinter import ttk
import serial
import time


class TimePressedButton(tk.Button):
    """A tkinter Button whose action depends on the
    duration it was pressed
    """

    def __init__(self, root,text,set_down_command ,set_up_command,memory_file,print_duration=False):
        super().__init__(root)
        self.start, self.end = 0, 0
        self.print_duration=print_duration
        self.set_down_command = set_down_command 
        self.set_up_command = set_up_command
        self.memory = memory_file

        self.duration=0

        self.bind("<ButtonPress>", self.on_press)
        self.bind("<ButtonRelease>", self.on_release)

        # self.set_down()
        # self.set_up()
        self["text"] = text
        self['command'] = self._no_op


    # def set_down(self):
    #     self.set_down_command()
    #     self.bind('<Button-1>', self.start_time)        

    # def set_up(self):
    #     self.set_up_command()
    #     self.bind('<ButtonRelease-1>', self.end_time)

    def _no_op(self):
        """keep the tk.Button default pressed/not pressed behavior
        """
        pass

    def on_press(self,event):
        self.set_down_command()
        self.start_time(event)
        
        

    def on_release(self,event):
        self.set_up_command()
        self.end_time(event)
        

    def start_time(self, e):
        self.start = time.time()

    def end_time(self, e):
        if self.start is not None:  # prevents a possible first click to take focus to generate an improbable time
            self.end = time.time()
            self.action()
        else:
            self.start = 0

    def action(self):
        """defines an action that varies with the duration
        the button was pressed
        """        
        self.duration = self.end - self.start
        self.start, self.end = 0, 0

        # if self.print_duration:print(f'the button was pressed for {self.duration} seconds')

        # self.memory.write(str(self.duration)+',')
        # self.memory.seek(0)
        # memory_contents = self.memory.read()
        # print('Reading memory:',memory_contents,len(memory_contents))

        self.memory.seek(0)    
        memory_contents = self.memory.readline()


        if len(memory_contents) > 0:
            
            previous_record = float(memory_contents)        
            if self.set_down_command.__name__ == 'move_right':
                # print("Moving right")
                updated_record = previous_record + self.duration            
            elif self.set_down_command.__name__ == 'move_left':
                # print("Moving left")
                updated_record = previous_record - self.duration
            self.memory.seek(0)
            self.memory.write(str(updated_record))
            # self.memory.seek(0)
            # memory_contents = self.memory.read()
            # print("There's previous memory:",memory_contents)    
        else:
            # print("No memory before")
            if self.set_down_command.__name__ == 'move_right':
                # print("Moving right")
                self.memory.seek(0)
                self.memory.write(str(self.duration))   
            elif self.set_down_command.__name__ == 'move_left':
                # print("Moving left")
                self.memory.seek(0)
                self.memory.write(str(0-self.duration))   
            
        

    def getDuration(self):
        return self.duration



# class pressedButton(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self,text, *args, **kwargs)
#         self.button = tk.Button(self, text="Press me!")
#         self.text = tk.Text(self, width=40, height=6)
#         self.vsb = tk.Scrollbar(self, command=self.text.yview)
#         self["text"] = text



#         self.button.bind("<ButtonPress>", self.on_press)
#         self.button.bind("<ButtonRelease>", self.on_release)

#     def on_press(self, event):
#         print("button was pressed")

#     def on_release(self, event):
#         print("button was released")

#     def log(self, message):
#         now = time.strftime("%I:%M:%S", time.localtime())
#         self.text.insert("end", now + " " + message.strip() + "\n")
#         self.text.see("end")