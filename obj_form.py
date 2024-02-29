#obj_form.py - Ethan Nguyen
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
        
        # form adjusted accordingly to the size of the users monitor
        master.title("Fitts Law Experiment")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Button to switch back to the main menu form
        back_btn = tk.Button(master, text="Quit", command=self.back_mm)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10,pady=15)
        
        # Left and Right Boxes position, width, and distance between each other
        self.Lbox_pos_label = tk.Label(master, text="Left box: x: , y: , Width: ,Height: ", font=("Consolas", 8))
        self.Rbox_pos_label = tk.Label(master, text="Right box: x: , y: , Width: ,Height: ", font=("Consolas", 8))
        self.distance_label = tk.Label(master, text="Distance: ", font=("Consolas", 8))
        self.Lbox_pos_label.pack(pady=5)
        self.Rbox_pos_label.pack(pady=5)
        self.distance_label.pack(pady=5)
        
        # Tip and difficulty indicator
        self.tip_label = tk.Label(master, text="For the best experience, please fullscreen the application!", font=("Consolas", 10))
        self.tip_label.pack(pady=10)
        self.title_label = tk.Label(master, text=f"Difficulty {self.diff_multi+1}: Trial 1", font=myFont)
        self.title_label.pack(pady=10)
        
        # Shows the stopwatch timer of the overall trial
        self.elapsed_time_label = tk.Label(master, text="", font = myFont)
        self.elapsed_time_label.pack(pady=10)
        
        # Counts the amount of clicks on the boxes
        self.clicks_label = tk.Label(master, text="", font=myFont)
        self.clicks_label.pack(pady=10)
        
        # Calls the draw_boxes function
        self.draw_boxes()

        #Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_mm)
    
    # Back to the main menu
    def back_mm(self):
        self.master.destroy()
        self.main_menu.master.deiconify()
    
    # Show the result screen per trial
    def showResult(self):
        self.result_form = tk.Toplevel(self.master)
        self.master.withdraw()
        ResultsForm(self.result_form, self, self.recorded_time, self.click_timestamps, self.diff_multi, self.trial_count)
        
        if self.trial_count <= self.max_trials:
            self.trial_count += 1
            self.title_label.config(text=f"Difficulty {self.diff_multi+1}: Trial {self.trial_count}")
            self.startNewTrial()
        
        if self.trial_count > self.max_trials:
            self.trial_count = 1
            self.diff_multi += 1
            self.title_label.config(text=f"Difficulty {self.diff_multi+1}: Trial {self.trial_count}")
            self.startNewTrial()

    # Draw the boxes and apply a function
    def draw_boxes(self):
        # Inital box heigh and width
        box_width = 350
        box_height = 350
        
        # Inital left box coordinates
        left_box_x1 = 350
        left_box_y1 = 400
        
        # Inital Right box coordinates
        right_box_x1 = 1200
        right_box_y1 = 400
        
        # Draw left box
        self.left_box = tk.Label(self.master, text="Left Box", bg="blue")
        self.left_box.place(x=left_box_x1, y=left_box_y1, width=box_width, height=box_height)
        self.left_box.bind('<Button-1>', lambda event: self.start_stopwatch_left())
        self.Lbox_pos_label.config(text=f"x: {left_box_x1}, y: {left_box_y1}, Width: {box_width}, Height: {box_height}")
        
        # Draw right box
        self.right_box = tk.Label(self.master, text="Right Box", bg="red")
        self.right_box.place(x=right_box_x1, y=right_box_y1, width=box_width, height=box_height)
        self.right_box.bind('<Button-1>', lambda event: self.record_right_press())
        self.Rbox_pos_label.config(text=f"x: {right_box_x1}, y: {right_box_y1}, Width: {box_width}, Height: {box_height}")
        distance = right_box_x1 - left_box_x1
        self.distance_label.config(text=f"Distance: {distance}")
    
    # Start the timer and records right to left actions
    def start_stopwatch_left(self):
        
        if self.left_press_count == 0: # Starts the timer 
            self.stopwatch.startTime()
            self.timer()
        else: # record actions right to left
            self.record_clicks()
            self.record_timestamp()

        self.left_press_count += 1

    # Records a time from left to right actions
    def record_right_press(self):
        # Prevents overclicking of the right box
        if self.left_press_count > self.right_press_count:
            self.right_press_count += 1
            self.record_clicks()
            self.record_timestamp()
        
        # if-statement for whenever right press count is over 5
        if self.right_press_count > 5:
            self.stopwatch.stopTime()
            self.recorded_time = self.stopwatch.elapsed_time()
            self.reset_timer()
            self.showResult()
    
    # Records the total clicks
    def record_clicks(self):
        self.boxclick += 1
        self.clicks_label.config(text=f"Clicks: {self.boxclick}")
    
    # Stopwatch timer
    def timer(self):
        if self.stopwatch.start_time:
            elapsed_time = time.time() - self.stopwatch.start_time
            self.elapsed_time_label.config(text="Time: {:.2f} seconds." .format(elapsed_time))
            self.master.after(100, self.timer)
    
    # Reset the timer and click count to zero
    def reset_timer(self):
        self.left_press_count = 0
        self.right_press_count = 0
        self.boxclick = 0
        self.stopwatch.reset()
        self.elapsed_time_label.config(text="")
        self.clicks_label.config(text="Clicks: 0")

    # Records the time stamp whenever an action was made.
    def record_timestamp(self):
        # Record the timestamp for each press
        timestamp = time.time()
        self.click_timestamps.append(timestamp)

        if self.prev_timestamp is not None:
            time_interval = timestamp - self.prev_timestamp
            print(f"Time Interval {len(self.click_timestamps) - 2}-{len(self.click_timestamps) - 1}: {time_interval:.2f} seconds")

        self.prev_timestamp = timestamp
    
    # Start a new trial with boxes in random position and width.
    def startNewTrial(self):
        
        # New coordinates for left box based on difficulty and randomness
        new_left_x = (1/self.diff_multi) * random.randint(300, 600)
        new_left_y = random.randint(400, 800)
        
        # New coordinates for right box based on difficulty and randomness
        new_right_x = (self.diff_multi*75) + random.randint(1200, 1400)
        new_right_y = random.randint(400, 700)
        
        # New sizes for the boxes based on difficulty and randomness
        new_width = (1/self.diff_multi) * random.randint(250, 300) + 10
        new_height = (1/self.diff_multi)* random.randint(250, 300) + 10
        
        # configures the boxes to its new variables
        self.left_box.place_configure(x=new_left_x, y=new_left_y, width=new_width, height=new_height) 
        self.right_box.place_configure(x=new_right_x, y=new_right_y, width=new_width, height=new_height)
       
        # configures the label to match the boxes new variables
        self.Lbox_pos_label.config(text=f"x: {new_left_x}, y: {new_left_y:.2f}, Width: {new_width:.2f}, Height: {new_height:.2f}")
        self.Rbox_pos_label.config(text=f"x: {new_right_x}, y: {new_right_y:.2f}, Width: {new_width:.2f}, Height: {new_height:.2f}")
        
        # calculates the distance of the newly positioned boxes
        distance = math.sqrt((new_right_x - new_left_x)**2 + (new_right_y - new_left_y)**2)
        self.distance_label.config(text="Distance: {:.2f} ".format(distance))
        
        # the usual reset trial and recordings.
        self.reset_timer()
        self.recorded_time = 0
        self.click_timestamps = []
        self.prev_timestamp = None
        