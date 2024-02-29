#stopwatch.py - Ethan Nguyen
import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
    def startTime(self):
        self.start_time = time.time()
    
    def stopTime(self):
        self.end_time = time.time()

    def elapsed_time(self):
        return self.end_time - self.start_time
    
    def reset(self):
        self.start_time = 0
        self.end_time = 0
        