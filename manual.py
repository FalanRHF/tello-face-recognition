import tkinter as tk
import tkinter.messagebox as msgbox
from djitellopy import tello
from threading import Thread


class Window(tk.Tk):
    counter = 1
    command = [] #command array
    def __init__(self,drone):
        super().__init__()
        print(drone + " is inside manual.py")
        self.geometry("720x540")#window size

        self.title("Tello Controller")

        self.label_text = tk.StringVar()
        self.label_text.set("Tello Commands")
        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(side=tk.TOP, padx=10, pady=10)

        #buttons
        forward_button = tk.Button(self, text="Forward", width=10, command=lambda: self.addCommand("forward"))
        forward_button.place(x=20, y=100)

        back_button = tk.Button(self, text="back", width=10, command=lambda: self.addCommand("back"))
        back_button.place(x=120, y=100)

        right_button = tk.Button(self, text="Right", width=10, command=lambda: self.addCommand("right"))
        right_button.place(x=220, y=100)

        left_button = tk.Button(self, text="Left", width=10, command=lambda: self.addCommand("left"))
        left_button.place(x=320, y=100)

        up_button = tk.Button(self, text="Up", width=10, command=lambda: self.addCommand("up"))
        up_button.place(x=20, y=150)

        down_button = tk.Button(self, text="Down", width=10, command=lambda: self.addCommand("down"))
        down_button.place(x=120, y=150)

        turn_left_button = tk.Button(self, text="Turn Left", width=10, command=lambda: self.addCommand("rotate left"))
        turn_left_button.place(x=220, y=150)

        turn_right_button = tk.Button(self, text="Turn Right", width=10, command=lambda: self.addCommand("rotate right"))
        turn_right_button.place(x=320, y=150)

        turn_360_button = tk.Button(self, text="Perimeter Check", width=15, command=lambda: self.addCommand("rotate 360"))
        turn_360_button.place(x=100, y=200)

        
        run_button = tk.Button(self, text="RUN", width=10, command=lambda: self.run())
        run_button.place(x=20, y=300)

        land_button = tk.Button(self, text="LAND", width=10, command=lambda: self.land())
        land_button.place(x=120, y=300)

        clear_button = tk.Button(self, text="CLEAR", width=10, command=lambda: self.clearCommand())
        clear_button.place(x=220, y=300)

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
        
    def run(self):
        #command split -> move + rotate(- +) + liftoff + land + flip + etc
        #switch or if else 
        for x in self.command:
            if x in ["forward","back","right","left","up","down"]:
                # drone.move(x, 20)
                print(x + " 20cm")
            elif x == "rotate right":
                # drone.rotate_clockwise(90)
                print(x)
            elif x == "rotate left":
                # drone.rotate_counter_clockwise(90)
                print(x)
            elif x == "rotate 360":
                # drone.rotate_counter_clockwise(360)
                print(x)
        
        self.clearCommand()
    
    def land(self):
        # drone.land()
        print("landing")
        # self.destroy()

        
    def clearCommand(self):
        self.command.clear()
        print("Command array:", self.command)
        self.commandList.delete(0, tk.END)

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
  
