import tkinter as tk
import HomeFrame as home

class Window(tk.Tk):
    def __init__(self, drone, q):
        super().__init__()
        self.title("Tello Face Recognition")
        self.configure(bg='lightyellow')

        self.width, self.height = 900, 600
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.center_window_on_screen()

        home_frame = home.HomeFrame()
        home_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        home_frame.start(drone, q)

    def center_window_on_screen(self):
        x_cord = int((self.screen_width/2) - (self.width/2))
        y_cord = int((self.screen_height/2) - (self.height/2))
        self.geometry("{}x{}+{}+{}".format(self.width, self.height, x_cord, y_cord))

