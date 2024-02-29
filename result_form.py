# result_form.py - Ethan Nguyen
import tkinter as tk
from completion_form import completionForm

myFont = ("Consolas", 13)

class ResultsForm:
    def __init__(self, master, obj_form, recorded_time, click_timestamps, diff_multi, trial_count):
        self.master = master
        self.obj_form = obj_form
        self.recorded_time = recorded_time
        self.click_timestamps = click_timestamps

        master.title("Fitts Law Experiment - Results")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}+0+0")

        # Prevent program from not completely exiting out
        master.protocol("WM_DELETE_WINDOW", self.back_obj)

        # Button to switch back to the trial form
        back_btn = tk.Button(master, text="Next Trial", command=self.back_obj)
        back_btn['font'] = myFont
        back_btn.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=15)
        
        if (diff_multi == 5) & (trial_count == 3):
            back_btn.config(text="Next", command=self.completion)

        # Display results
        result_label = tk.Label(master, text="Results ()", font=myFont)
        result_label.pack(pady=10)
        result_label.config(text=f"Results (Difficulty {diff_multi+1}: Trial {trial_count})")
        # Display time intervals between clicks
        intervals_label = tk.Label(master, text="Time Intervals:", font=myFont)
        intervals_label.pack(pady=10)

        for i in range(1, len(self.click_timestamps)):
            time_interval = self.click_timestamps[i] - self.click_timestamps[i - 1]
            interval_label = tk.Label(master, text=f"{i}-{i+1}. {time_interval:.2f} seconds", font=myFont)
            interval_label.pack()

        # Display recorded time
        time_warning_label = tk.Label(master, text="Warning: Time may be inaccurate due to the system calculations.", font=("Consolas", 8))
        recorded_time_label = tk.Label(master, text=f"Trial Time: {recorded_time:.2f} seconds", font=myFont)
        time_warning_label.pack(pady=10)
        recorded_time_label.pack(pady=5)


    def back_obj(self):
        self.master.destroy()
        self.obj_form.master.deiconify()
        
    def completion(self):
        self.completion_form = tk.Toplevel(self.master)
        self.master.withdraw()
        completionForm(self.completion_form)
