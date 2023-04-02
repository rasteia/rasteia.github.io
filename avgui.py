import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import threading

# Function to run newpost.py in a new thread
def run_newpost():
    global process
    process = subprocess.Popen(["python", "newpost.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        output_text.insert(tk.END, line)
    process.communicate()

def start_newpost():
    if process is None or process.poll() is not None:
        threading.Thread(target=run_newpost, daemon=True).start()
    else:
        messagebox.showerror("Error", "newpost.py is already running!")

def stop_newpost():
    if process is not None and process.poll() is None:
        process.terminate()
        output_text.insert(tk.END, "newpost.py terminated.\n")
    else:
        messagebox.showerror("Error", "newpost.py is not running!")

def restart_newpost():
    stop_newpost()
    start_newpost()

# Initialize the main window
root = tk.Tk()
root.title("JPyPA")
root.geometry("600x400")

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Create a Tools menu
tools_menu = tk.Menu(menu)
menu.add_cascade(label="Tools", menu=tools_menu)
# Add items to the Tools menu here

# Create control buttons
start_button = tk.Button(root, text="Start", command=start_newpost)
start_button.pack(side=tk.LEFT, padx=5, pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_newpost)
stop_button.pack(side=tk.LEFT, padx=5, pady=5)

restart_button = tk.Button(root, text="Restart", command=restart_newpost)
restart_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create output text box
output_text = tk.Text(root, wrap=tk.WORD)
output_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# Initialize the process variable
process = None

root.mainloop()
