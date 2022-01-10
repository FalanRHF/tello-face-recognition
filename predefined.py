import tkinter as tk
import tkinter.messagebox as msgbox
from djitellopy import tello
from threading import Thread

class Window(tk.Tk):
    counter = 1
    command = [] #command array
    def __init__(self,drone):
        super().__init__()
        # print(drone + " is inside manual.py")
        self.geometry("720x540")#window size

        self.title("Tello Controller")

        self.label_text = tk.StringVar()
        self.label_text.set("Tello Commands")
        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(side=tk.TOP, padx=10, pady=10)

        #buttons
        
        start_button = tk.Button(self, text="START", width=10, command=lambda: self.run(drone))
        start_button.place(x=20, y=300)

        stop_button = tk.Button(self, text="STOP", width=10, command=lambda: self.land(drone))
        stop_button.place(x=120, y=300)

        override_button = tk.Button(self, text="OVERRIDE", width=10, command=lambda: self.clearCommand())
        override_button.place(x=220, y=300)

        # scroll bar
        self.scrollbar = tk.Scrollbar()
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        #command listbox
        self.commandList = tk.Listbox(width=50)
        self.commandList.pack(side=tk.RIGHT, padx=(20, 0), pady=(0, 20),fill=tk.BOTH)

        self.commandList.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.commandList.yview)

    def addCommand(self, direction):
        self.commandList.insert(self.counter, direction)
        self.counter += 1
        self.command.append(direction)
        
    def run(self, drone):
        #command split -> move + rotate(- +) + liftoff + land + flip + etc
        #switch or if else 
        moveDistance = 50
        for x in self.command:
            if x in ["forward","back","right","left","up","down"]:
                # drone.move(x, 20)
                print(x + " 20cm")
            elif x == "rotate right":
                drone.rotate_clockwise(90)
                print(x)
            elif x == "rotate left":
                drone.rotate_counter_clockwise(90)
                print(x)
            elif x == "rotate 360":
                drone.rotate_counter_clockwise(360)
                print(x)
            elif x == "rotate 180":
                drone.rotate_counter_clockwise(180)
                print(x)
        
        self.clearCommand()
    
    def land(self, drone):
        drone.land()
        print("landing")
        # self.destroy()

        
    def clearCommand(self):
        self.destroy()

# if __name__ == "__main__":
#     # drone = tello.Tello()
#     # drone.connect()
#     # print(donna.get_battery())
#     # drone.takeoff()

#     window = Window()
#     window.mainloop()

def startWindow(drone):
  window = Window(drone)
  window.mainloop()

def init(drone):
  thread = Thread(target=startWindow(drone))
  thread.start()
  thread.join()
  
