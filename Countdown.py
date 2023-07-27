import time
import tkinter as tk

# Define the countdown function.
def countdown(t):
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    countdown_label.config(text=timer)  # Update the label in the GUI
    if t > 0:
        window.after(1000, countdown, t - 1)  # Schedule the countdown after 1000 ms (1 second)
    else:
        countdown_label.config(text='Fire in the hole!!')

# Function called when the "Start Countdown" button is pressed
def start_countdown():
    t = get_user_input()
    if t is not None:
        countdown(t)

# Function to get user input for time
def get_user_input():
    t = entry.get()
    try:
        t = int(t)
        if t < 0:
            raise ValueError
        return t
    except ValueError:
        countdown_label.config(text="Invalid input. Please enter a positive integer.")
        return None

# Create the GUI window
window = tk.Tk()
window.title("Countdown Timer")

# Create and place GUI widgets
label = tk.Label(window, text="Enter the time in seconds:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

start_button = tk.Button(window, text="Start Countdown", command=start_countdown)
start_button.pack(pady=10)

# Label to display the countdown
countdown_label = tk.Label(window, text="00:00")
countdown_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()