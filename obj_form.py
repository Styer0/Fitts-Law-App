import tkinter as tk
import time
import random
import math
from stopwatch import Stopwatch
from result_form import ResultsForm

myFont = ("Consolas", 13)
class ObjForm:
    def __init__(self, master, main_menu):
        # Inital variables
        self.master = master
        self.main_menu = main_menu
        self.stopwatch = Stopwatch()
        self.click_timestamps = [] #Stores the recorded time of each actions
        self.boxclick = 0
        self.left_press_count = 0
        self.right_press_count = 0
        self.recorded_time = 0
        self.prev_timestamp = None
        self.trial_count = 1  # Track the number of trials
        self.max_trials = 3   # Set the maximum number of trials
        self.diff_multi = 1 # The difficulty multiplier
        
        master.title("Fitts Law Game")
        master.geometry('1200x900')
        
        #Button to switch back to the main menu form
        back_btn = tk.Button(master, text="Quit", command=self.back_mm)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10,pady=15)
        
        self.Lbox_pos_label = tk.Label (master, text="Left box: x: , y: , width: ", font=("Consolas", 8))
        self.Rbox_pos_label = tk.Label (master, text="Right box: x: , y: , width: ", font=("Consolas", 8))
        self.distance_label = tk.Label (master, text="Distance: ", font=("Consolas", 8))
        self.Lbox_pos_label.pack(pady=5)
        self.Rbox_pos_label.pack(pady=5)
        self.distance_label.pack(pady=5)
        
        self.title_label = tk.Label(master, text="Difficulty 1: Trial 1", font=myFont)
        self.title_label.pack(pady=10)
        
        self.elapsed_time_label = tk.Label(master, text="", font = myFont)
        self.elapsed_time_label.pack(pady=10)
        
        self.clicks_label = tk.Label(master, text="", font=myFont)
        self.clicks_label.pack(pady=10)
        

        self.draw_boxes()

        #Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_mm)
    
    #Back to the main menu
    def back_mm(self):
        self.master.destroy()
        self.main_menu.master.deiconify()
    
    def showResult(self):
        self.result_form = tk.Toplevel(self.master)
        self.master.withdraw()
        ResultsForm(self.result_form, self, self.recorded_time, self.click_timestamps)
        
        if self.trial_count < self.max_trials:
            self.trial_count += 1
            self.title_label.config(text="Difficulty 1: Trial {:}" .format(self.trial_count))
            self.startNewTrial()
        
    def draw_boxes(self):
        box_width = 50
        box_height = 25
        
        #Left box coordinates
        left_box_x1 = 50
        left_box_y1 = 300
        
        right_box_x1 = 1500
        right_box_y1 = 300
        
        # Draw left box
        self.left_box = tk.Label(self.master, text="Left Box", bg="blue", width=box_width, height=box_height)
        self.left_box.place(x=left_box_x1, y=left_box_y1)
        self.left_box.bind('<Button-1>', lambda event: self.start_stopwatch_left())
        self.Lbox_pos_label.config(text=f"x: {left_box_x1}, y: {left_box_y1}, Width: {box_width}")
        
        # Draw right box
        self.right_box = tk.Label(self.master, text="Right Box", bg="red", width=box_width, height=box_height)
        self.right_box.place(x=right_box_x1, y=right_box_y1)
        self.right_box.bind('<Button-1>', lambda event: self.record_right_press())
        self.Rbox_pos_label.config(text=f"x: {right_box_x1}, y: {right_box_y1}, Width: {box_width}")
        distance = right_box_x1 - left_box_x1
        self.distance_label.config(text=f"Distance: {distance}")
    
    def start_stopwatch_left(self):
        if self.left_press_count == 0:
            self.stopwatch.startTime()
            self.timer()
            #self.left_press_count += 1
            #self.record_clicks()
            #self.record_timestamp()
        else:
            self.record_clicks()
            self.record_timestamp()
        self.left_press_count += 1
        
        if self.left_press_count > 5:
            self.stopwatch.stopTime()
            self.recorded_time = self.stopwatch.elapsed_time()
            self.reset_timer()
            self.showResult()
        
            
    def record_right_press(self):
        self.right_press_count += 1
        self.record_clicks()
        self.record_timestamp()
            
    def record_clicks(self):
        self.boxclick += 1
        self.clicks_label.config(text="Clicks: {:}" .format(self.boxclick))
        
    def timer(self):
        if self.stopwatch.start_time:
            elapsed_time = time.time() - self.stopwatch.start_time
            self.elapsed_time_label.config(text="Time: {:.2f} seconds." .format(elapsed_time))
            self.master.after(100, self.timer)
            
    def reset_timer(self):
        self.left_press_count = 0
        self.right_press_count = 0
        self.boxclick = 0
        self.stopwatch.reset()
        self.elapsed_time_label.config(text="")
        self.clicks_label.config(text="Clicks: 0")

    def record_timestamp(self):
        # Record the timestamp for each press
        timestamp = time.time()
        self.click_timestamps.append(timestamp)

        if self.prev_timestamp is not None:
            time_interval = timestamp - self.prev_timestamp
            print(f"Time Interval {len(self.click_timestamps) - 2}-{len(self.click_timestamps) - 1}: {time_interval:.2f} seconds")

        self.prev_timestamp = timestamp
    
    def startNewTrial(self):
        
        new_left_x = random.randint(50, 600)
        new_left_y = random.randint(300, 1000)
        new_right_x = random.randint(900, 1600)
        new_right_y = random.randint(300, 900)
        new_width = random.randint(100, 200)
        new_height = random.randint(50, 150)
        
        self.left_box.place_configure(x=new_left_x, y=new_left_y, width=new_width, height=new_height) 
        self.right_box.place_configure(x=new_right_x, y=new_right_y, width=new_width, height=new_height)
       
        self.Lbox_pos_label.config(text=f"x: {new_left_x}, y: {new_left_y}, Width: {new_width}")
        self.Rbox_pos_label.config(text=f"x: {new_right_x}, y: {new_right_y}, Width: {new_width}")
        
        distance = math.sqrt((new_right_x - new_left_x)**2 + (new_right_y - new_left_y)**2)
        self.distance_label.config(text="Distance:  {:.2f} ".format(distance))
        
        self.reset_timer()
        self.recorded_time = 0
        self.click_timestamps = []
        self.prev_timestamp = None
        