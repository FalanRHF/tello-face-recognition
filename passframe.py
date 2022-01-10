import tkinter as tk
import numpy as np
from PIL import Image, ImageTk 
import tkinter.messagebox as msgbox
from djitellopy import tello
from threading import Thread

class Window(tk.Tk):
    counter = 1
    command = [] #command array
    def __init__(self,drone,q):
        super().__init__()
        # print(drone + " is inside manual.py")
        self.geometry("900x600")#window size

        self.title("Tello Controller")

        self.label_text = tk.StringVar()
        self.label_text.set("Tello Commands")
        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(side=tk.TOP, padx=10, pady=10)

        #buttons
        array = q.get()
        print(array)
        img =  ImageTk.PhotoImage(image=Image.fromarray(array))

        canvas = tk.Canvas(self,width=300,height=300)
        canvas.pack()
        canvas.create_image(20,20, anchor="nw", image=img)
        canvas.place(x=220, y=300)
    
    print('keluar init')

# if __name__ == "__main__":
#     # drone = tello.Tello()
#     # drone.connect()
#     # print(donna.get_battery())
#     # drone.takeoff()

#     window = Window()
#     window.mainloop()

def startWindow(drone, q):
  window = Window(drone, q)
  window.mainloop()


