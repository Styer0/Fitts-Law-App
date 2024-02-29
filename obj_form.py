import tkinter as tk
import time
from stopwatch import Stopwatch
from result_form import ResultsForm

myFont = ("Consolas", 13)
class ObjForm:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        self.stopwatch = Stopwatch()
        self.click_timestamps = [] #Stores the recorded time of each actions
                
        master.title("Fitts Law Game")
        master.geometry('1200x900')

        #Button to switch back to the main menu form
        back_btn = tk.Button(master, text="Quit", command=self.back_mm)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10,pady=15)
        
        self.elapsed_time_label = tk.Label(master, text="", font = myFont)
        self.elapsed_time_label.pack(pady=10)
        
        self.clicks_label = tk.Label(master, text="", font=myFont)
        self.clicks_label.pack(pady=10)
        
        self.boxclick = 0
        self.left_press_count = 0
        self.right_press_count = 0
        self.recorded_time = 0
        self.prev_timestamp = None
        
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
        ResultsForm(self.result_form, self, self.recorded_time)
        
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
        
            
    def record_right_press(self):
        self.right_press_count += 1
        self.record_clicks()
        self.record_timestamp()
        
        if self.right_press_count >= 6:
            self.stopwatch.stopTime()
            self.recorded_time = self.stopwatch.elapsed_time()
            self.reset_timer()
            self.showResult()
            
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