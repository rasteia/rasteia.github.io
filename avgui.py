import tkinter as tk
import subprocess
import threading
import os

class JPyPAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JPyPA")
        self.geometry("500x300")

        self.jekyll_proc = None
        self.newpost_proc = None

        self.create_widgets()

    def create_widgets(self):
        self.jekyll_label = tk.Label(self, text="Jekyll Serve:")
        self.jekyll_label.grid(row=0, column=0, pady=10)

        self.newpost_label = tk.Label(self, text="Newpost.py:")
        self.newpost_label.grid(row=1, column=0, pady=10)

        self.jekyll_button = tk.Button(self, text="Start", command=self.toggle_jekyll)
        self.jekyll_button.grid(row=0, column=1, pady=10)

        self.newpost_button = tk.Button(self, text="Start", command=self.toggle_newpost)
        self.newpost_button.grid(row=1, column=1, pady=10)

    def toggle_jekyll(self):
        if not self.jekyll_proc:
            self.start_jekyll()
        else:
            self.stop_jekyll()

    def toggle_newpost(self):
        if not self.newpost_proc:
            self.start_newpost()
        else:
            self.stop_newpost()

    def start_jekyll(self):
        self.jekyll_proc = subprocess.Popen(["jekyll", "serve"])
        self.jekyll_button.config(text="Stop")

    def stop_jekyll(self):
        self.jekyll_proc.terminate()
        self.jekyll_proc = None
        self.jekyll_button.config(text="Start")

    def start_newpost(self):
        self.newpost_proc = subprocess.Popen(["python", "newpost.py"])
        self.newpost_button.config(text="Stop")

    def stop_newpost(self):
        self.newpost_proc.terminate()
        self.newpost_proc = None
        self.newpost_button.config(text="Start")

if __name__ == "__main__":
    app = JPyPAApp()
    app.mainloop()
