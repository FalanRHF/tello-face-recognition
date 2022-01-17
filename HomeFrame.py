import tkinter as tk
import tkinter.font as font 
import ManualFrame as manual

class HomeFrame(tk.Frame):
    def __init__(self):
        super().__init__()  # ADDED parent argument.

  
    def startFrame(self, drone, q):
        font_large = font.Font(family='Georgia', size='24', weight='bold')
        font_small = font.Font(family='Georgia', size='12')

        self.manual_frame = manual.ManualFrame()

        self.config(bg='lightblue')

        btn_manual_mode = tk.Button(self,  text='START', font=font_small, command=lambda: self.change_to_manual(drone, q))
        btn_manual_mode.pack(expand=1, pady=10)
    
    def start(self, drone, q):
        self.startFrame(drone, q)
        self.mainloop()

    def change_to_manual(self ,drone, q):
        self.forget()
        self.manual_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.manual_frame.start(drone, q)