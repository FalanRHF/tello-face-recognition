import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from djitellopy import tello
from threading import Thread
import time
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from weakref import ref
from ttkthemes import ThemedStyle

class Window(tk.Tk):
    counter = 1
    command = [] #command array
    def __init__(self,drone):
        super().__init__()
        print(drone + " is inside manual.py")
        self.title("Tello Controller")
        # self.geometry("1000x540")#window size
        self.configure(background='#434343')

        self.width, self.height = 900, 600
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.center_window_on_screen()

        # Setting Theme
        style = ThemedStyle(self)
        style.set_theme("equilux")

        self.graphAngle = 0
        self.x, self.y = 0, 0
        #buttons
        forward_button = ttk.Button(self, text="Forward", width=10, command=lambda: self.addCommand("forward"))
        forward_button.place(x=20, y=100)

        back_button = ttk.Button(self, text="Back", width=10, command=lambda: self.addCommand("back"))
        back_button.place(x=120, y=100)

        right_button = ttk.Button(self, text="Right", width=10, command=lambda: self.addCommand("right"))
        right_button.place(x=220, y=100)

        left_button = ttk.Button(self, text="Left", width=10, command=lambda: self.addCommand("left"))
        left_button.place(x=320, y=100)

        up_button = ttk.Button(self, text="Up", width=10, command=lambda: self.addCommand("up"))
        up_button.place(x=20, y=150)

        down_button = ttk.Button(self, text="Down", width=10, command=lambda: self.addCommand("down"))
        down_button.place(x=120, y=150)

        turn_left_button = ttk.Button(self, text="Turn Left", width=10, command=lambda: self.addCommand("rotate left"))
        turn_left_button.place(x=220, y=150)

        turn_right_button = ttk.Button(self, text="Turn Right", width=10, command=lambda: self.addCommand("rotate right"))
        turn_right_button.place(x=320, y=150)

        turn_360_button = ttk.Button(self, text="Perimeter Check", width=15, command=lambda: self.addCommand("rotate 360"))
        turn_360_button.place(x=100, y=200)

        run_button = ttk.Button(self, text="RUN", width=10, command=lambda: self.run())
        run_button.place(x=20, y=300)

        land_button = ttk.Button(self, text="LAND", width=10, command=lambda: self.land())
        land_button.place(x=120, y=300)

        clear_button = ttk.Button(self, text="CLEAR", width=10, command=lambda: self.clearCommand())
        clear_button.place(x=220, y=300)

        # scroll bar
        self.scrollbar = ttk.Scrollbar()
        self.scrollbar.pack()
        #command listbox
        self.commandList = tk.Listbox()
        self.commandList.pack(side=tk.BOTTOM,fill=tk.BOTH, padx=(20, 20), pady=(20, 20))
        self.commandList.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.commandList.yview)

        # #matplotlib figure and canvas
        self.fig = Figure(figsize=(5, 5),dpi=100)
        self.fig.patch.set_facecolor('#434343')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT)
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.axis('off')
        self.plot1.axis('equal')

    def addCommand(self, direction):
        self.addToListBox("Adding: "+direction,"black")
        self.command.append(direction)
        self.plot(direction,"black")

    def addToListBox(self,direction,color):
        self.commandList.insert(self.counter, direction)
        self.commandList.itemconfig(self.counter-1, foreground = color)
        self.commandList.select_clear(self.commandList.size() - 2)  # Clear the current selected item
        self.commandList.yview(tk.END)
        self.counter += 1

    def run(self):
        print("Command array:", self.command)
        #command split -> move + rotate(- +) + liftoff + land + flip + etc
        #switch or if else
        self.clearPlots()
        self.clearPlots()
        self.clearPlots()
        for x in self.command:
            time.sleep(0.05)
            if x in ["forward","back","right","left","up","down"]:
                # drone.move(x, 20)
                print(x + " 20cm")
            elif x == "rotate right":
                # drone.rotate_clockwise(15)
                print(x)
            elif x == "rotate left":
                # drone.rotate_counter_clockwise(15)
                print(x)
            elif x == "rotate 360":
                # drone.rotate_counter_clockwise(360)
                print(x)
            self.addToListBox("Running: "+x,"green")
            self.plot(x,"green")

        self.clearCommand()
        self.clearPlots()
    
    def land(self):
        # drone.land()
        print("landing")
        # self.destroy()

    def clearCommand(self):
        self.command.clear()
        print("Command array:", self.command)
        self.commandList.delete(0, tk.END)
        self.clearPlots()
        self.counter=1
    def clearPlots(self):
        for line in self.plot1.lines:
            line.set_marker(None)
        for line in self.plot1.lines:
            for line in self.plot1.lines:
                line.remove()
        self.canvas.draw()
        self.x, self.y, self.preX, self.preY, self.graphAngle = 0, 0, 0, 0, 0

    def getSides(self, hypo, angle):
        x = math.sin(math.radians(angle)) * hypo
        y = math.cos(math.radians(angle)) * hypo
        return x, y

    def plot(self, direction, color):
        tempAngle = self.graphAngle
        if direction == "back":
            tempAngle += 180
        elif direction == "right":
            tempAngle += 90
        elif direction == "left":
            tempAngle -= 90
        elif direction == "rotate right":
            self.graphAngle += 15
            # tempAngle = self.graphAngle
            return None
        elif direction == "rotate left":
            self.graphAngle -= 15
            # tempAngle = self.graphAngle
            return None
        elif direction in ["up", "down","rotate 360"]:
            return None

        #handle rotation only
        hypo = 20
        # for i in droneAngle:
        self.preX, self.preY = self.x, self.y
        # self.graphAngle += i  # put angle

        self.x, self.y = self.getSides(hypo, tempAngle)
        self.x = self.preX + self.x
        self.y = self.preY + self.y

        line1 = [self.preX, self.x]
        line2 = [self.preY, self.y]
        self.plot1.plot(line1, line2, color=color)
        self.plot1.plot(self.x, self.y, marker='.', color=color)
        self.canvas.draw()

        self.canvas.flush_events()

        # toolbar = NavigationToolbar2Tk(self.canvas, self)
        # toolbar.update()

    def center_window_on_screen(self):
        x_cord = int((self.screen_width / 2) - (self.width / 2))
        y_cord = int((self.screen_height / 2) - (self.height / 2))
        self.geometry("{}x{}+{}+{}".format(self.width, self.height, x_cord, y_cord))
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
  
