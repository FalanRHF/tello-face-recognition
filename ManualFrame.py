import tkinter as tk
import tkinter.messagebox as msgbox
from djitellopy import tello
from threading import Thread
import tkinter.font as font
import PygameControl
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import time
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ttkthemes import ThemedStyle


class ManualFrame(tk.Frame):
    counter = 1
    command = [] #comm
    def __init__(self):
        super().__init__()  # ADDED parent argument.
        
        # self.forget()
    def startFrame(self, drone, q):
        print('ManualFrame() initialized')
        # Let's create the fonts that we need.
        font_large = font.Font(family='Georgia', size='24', weight='bold')
        font_small = font.Font(family='Georgia', size='12')
        
        self.drone = drone
        self.label_text = tk.StringVar()
        self.label_text.set("Tello Commands")
        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(side=tk.TOP, padx=10, pady=10)

        self.config(bg='green')
        self.configure(background='#434343')


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

        down_button = ttk.Button(self, text="Down", width=10,
                                command=lambda: self.addCommand("down"))
        down_button.place(x=120, y=150)

        turn_left_button = ttk.Button(self, text="Turn Left", width=10, command=lambda: self.addCommand("rotate left"))
        turn_left_button.place(x=220, y=150)

        turn_right_button = ttk.Button(self, text="Turn Right", width=10, command=lambda: self.addCommand("rotate right"))
        turn_right_button.place(x=320, y=150)

        turn_360_button = ttk.Button(self, text="Perimeter Check", width=15, command=lambda: self.addCommand("rotate 360"))
        turn_360_button.place(x=100, y=200)

        run_button = ttk.Button(self, text="RUN", width=10, command=lambda: self.run())
        run_button.place(x=20, y=300)

        takeoff_button = ttk.Button(self, text="TAKE OFF", width=10, command=lambda: self.takeoff())
        takeoff_button.place(x=120, y=300)

        land_button = ttk.Button(self, text="LAND", width=10, command=lambda: self.land())
        land_button.place(x=220, y=300)

        clear_button = ttk.Button(self, text="CLEAR", width=10, command=lambda: self.clearCommand())
        clear_button.place(x=320, y=300)

        btn_controller_mode = tk.Button(self, text='WASD MODE', font=font_small, command=lambda: self.change_to_controller(drone, q))
        btn_controller_mode.pack(side=tk.BOTTOM, pady=20)

        self.testFrame = tk.Frame(self, height=117)
        self.testFrame.pack(side=tk.BOTTOM,fill=tk.X)

        labelImage = tk.Label(self.testFrame, height=117, width=208)
        labelImage.pack(side=tk.RIGHT, fill=tk.Y)

        # scroll bar
        self.scrollbar = ttk.Scrollbar(self.testFrame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #command listbox
        self.commandList = tk.Listbox(self.testFrame)
        self.commandList.pack(side=tk.RIGHT, expand=1, fill=tk.BOTH, padx=(5, 5), pady=(5, 5))
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
        
        self.getImage(labelImage, q)

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
                # self.drone.move(x, 20)
                print(x + " 20cm")
            elif x == "rotate right":
                # self.drone.rotate_clockwise(15)
                print(x)
            elif x == "rotate left":
                # self.drone.rotate_counter_clockwise(15)
                print(x)
            elif x == "rotate 360":
                # self.drone.rotate_counter_clockwise(360)
                print(x)
            self.addToListBox("Running: "+x,"green")
            self.plot(x,"green")

        self.clearCommand()
        self.clearPlots()
    
    def takeoff(self):
        # self.drone.takeoff()
        print("takeoff")
        # self.destroy()

    def land(self):
        # self.drone.land()
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
    
    def start(self, drone, q):
        self.startFrame(drone, q)
        self.mainloop()
    
    
    def change_to_controller(self ,drone, q):
        print('change_to_controller called')
        print('controller packing...')
        PygameControl.main(drone)
        self.forget()

    def getImage(self, labelImage, q):
        global img
        img_array = q.get() 
        img =  ImageTk.PhotoImage(image=Image.fromarray(img_array))
        labelImage.config(image=img)
        labelImage.image = img
        labelImage.after(34, lambda: self.getImage(labelImage, q))



