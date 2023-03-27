import tkinter as tk
from datetime import datetime

class StopWatch:
    def __init__(self, master):
        self.master = master
        self.display = tk.Label(self.master, text="00:00:00", font=("Arial", 20), width=10)
        self.display.pack()
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self._update()

        button_frame = tk.Frame(self.master)
        start_button = tk.Button(button_frame, text="Start", command=self.start)
        start_button.pack(side=tk.LEFT)
        stop_button = tk.Button(button_frame, text="Stop", command=self.stop)
        stop_button.pack(side=tk.LEFT)
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset)
        reset_button.pack(side=tk.LEFT)
        button_frame.pack()

    def _update(self):
        if self.running:
            delta_time = datetime.now() - self.start_time
            self.elapsed_time = delta_time.seconds
        mins, secs = divmod(self.elapsed_time, 60)
        hours, mins = divmod(mins, 60)
        time_str = f"{hours:02d}:{mins:02d}:{secs:02d}"
        self.display.config(text=time_str)
        self.display.after(1000, self._update)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = datetime.now()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.elapsed_time = 0
        self.running = False
        self.display.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stopwatch")
    stopwatch = StopWatch(root)
    root.mainloop()
