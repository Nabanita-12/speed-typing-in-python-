import tkinter as tk
import time

# define the text to type
text = "The quick brown fox jumps over the lazy dog."

# define the time limit (in seconds)
time_limit = 30

# create the main window
root = tk.Tk()
root.title("Speed Typing Test")

# create a label for the text to type
text_label = tk.Label(root, text=text, font=("Arial", 16))
text_label.pack(pady=10)

# create a label for the timer
timer_label = tk.Label(root, text="", font=("Arial", 20))
timer_label.pack(pady=10)

# create a label for the user input
input_label = tk.Label(root, text="Type here:", font=("Arial", 16))
input_label.pack(pady=10)

# create an entry widget for the user input
input_entry = tk.Entry(root, width=30, font=("Arial", 16))
input_entry.pack(pady=10)

# create a label for the results
results_label = tk.Label(root, text="", font=("Arial", 16))
results_label.pack(pady=10)

# create a function to update the timer
def update_timer():
    remaining_time = time_limit - (time.time() - start_time)
    if remaining_time <= 0:
        remaining_time = 0
        input_entry.config(state="disabled")
        results_label.config(text="Time's up!")
    timer_label.config(text="Time: {:.1f}s".format(remaining_time))
    root.after(100, update_timer)

# create a function to handle the user input
def handle_input(event):
    if input_entry.get() == text:
        input_entry.config(state="disabled")
        elapsed_time = time.time() - start_time
        typing_speed = len(text.split()) / (elapsed_time / 60)
        results_label.config(text="You typed the text correctly in {:.1f}s.\nYour typing speed was {:.1f} words per minute.".format(elapsed_time, typing_speed))

# create a function to start the test
def start_test():
    global start_time
    start_time = time.time()
    input_entry.config(state="normal")
    input_entry.delete(0, tk.END)
    input_entry.focus()
    results_label.config(text="")
    root.after(100, update_timer)

# create a button to start the test
start_button = tk.Button(root, text="Start", font=("Arial", 16), command=start_test)
start_button.pack(pady=10)

# bind the handle_input function to the Return key
input_entry.bind("<Return>", handle_input)

# run the main event loop
root.mainloop()
