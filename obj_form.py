import tkinter as tk
import time
from stopwatch import Stopwatch

myFont = ("Consolas", 13)
class ObjForm:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        self.stopwatch = Stopwatch()
        
        master.title("Fitts Law Game")
        master.geometry('1200x900')

        #Button to switch back to the main menu form
        back_btn = tk.Button(master, text="Quit", command=self.back_mm)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10,pady=15)
        
        self.draw_boxes()
        
        #Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_mm)
    
    #Back to the main menu
    def back_mm(self):
        self.master.destroy()
        self.main_menu.master.deiconify()
    
    def draw_boxes(self):
        box_width = 50
        box_height = 25
        
        #Left box coordinates
        left_box_x1 = 50
        left_box_y1 = 300
        left_box_x2 = left_box_x1 + box_width
        left_box_y2 = left_box_y1 + box_height
        
        right_box_x1 = 1500
        right_box_y1 = 300
        right_box_x2 = right_box_x1 + box_width
        right_box_y2 = right_box_y1 + box_height
        
        # Draw left box
        self.left_box = tk.Label(self.master, text="Left Box", bg="blue", width=box_width, height=box_height)
        self.left_box.place(x=left_box_x1, y=left_box_y1)
        self.left_box.bind('<Button-1>', lambda event: self.start_stopwatch_left())

        # Draw right box
        self.right_box = tk.Label(self.master, text="Right Box", bg="red", width=box_width, height=box_height)
        self.right_box.place(x=right_box_x1, y=right_box_y1)
        self.right_box.bind('<Button-1>', lambda event: self.record_right_press())