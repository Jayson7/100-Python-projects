import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from threading import Thread

class CountdownTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jayson Advanced Countdown Timer")
        self.geometry("400x300")
        self.resizable(False, False)

        self.create_widgets()
        self.running = False
        self.time_left = 0  # Total time in seconds

    def create_widgets(self):
        # Time input fields
        input_frame = tk.Frame(self)
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Hours:").grid(row=0, column=0)
        self.hours_entry = ttk.Entry(input_frame, width=5, justify="center")
        self.hours_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Minutes:").grid(row=0, column=2)
        self.minutes_entry = ttk.Entry(input_frame, width=5, justify="center")
        self.minutes_entry.grid(row=0, column=3)

        tk.Label(input_frame, text="Seconds:").grid(row=0, column=4)
        self.seconds_entry = ttk.Entry(input_frame, width=5, justify="center")
        self.seconds_entry.grid(row=0, column=5)

        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = ttk.Button(button_frame, text="Pause", command=self.pause_timer, state="disabled")
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_timer, state="disabled")
        self.reset_button.grid(row=0, column=2, padx=5)

        # Progress bar
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        # Timer display
        self.timer_label = tk.Label(self, text="00:00:00", font=("Helvetica", 24))
        self.timer_label.pack()

    def calculate_time(self):
        hours = int(self.hours_entry.get() or 0)
        minutes = int(self.minutes_entry.get() or 0)
        seconds = int(self.seconds_entry.get() or 0)
        return hours * 3600 + minutes * 60 + seconds

    def start_timer(self):
        if not self.running:
            self.time_left = self.calculate_time()
            if self.time_left <= 0:
                messagebox.showwarning("Invalid Input", "Please enter a valid time!")
                return

            self.running = True
            self.update_buttons(start="disabled", pause="normal", reset="normal")
            self.progress["maximum"] = self.time_left
            self.run_timer()

    def run_timer(self):
        def timer_thread():
            while self.running and self.time_left > 0:
                mins, secs = divmod(self.time_left, 60)
                hours, mins = divmod(mins, 60)
                self.timer_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
                self.progress["value"] = self.calculate_time() - self.time_left
                time.sleep(1)
                self.time_left -= 1

            if self.time_left == 0:
                self.running = False
                self.timer_label.config(text="Time's up!")
                messagebox.showinfo("Countdown Timer", "Time's up!")
                self.update_buttons(start="normal", pause="disabled", reset="disabled")

        Thread(target=timer_thread, daemon=True).start()

    def pause_timer(self):
        if self.running:
            self.running = False
            self.start_button.config(state="normal")
            self.pause_button.config(state="disabled")

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.timer_label.config(text="00:00:00")
        self.progress["value"] = 0
        self.update_buttons(start="normal", pause="disabled", reset="disabled")

    def update_buttons(self, start, pause, reset):
        self.start_button.config(state=start)
        self.pause_button.config(state=pause)
        self.reset_button.config(state=reset)

if __name__ == "__main__":
    app = CountdownTimer()
    app.mainloop()
