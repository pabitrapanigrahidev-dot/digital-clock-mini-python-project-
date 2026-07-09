import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")
root.geometry("500x200")

def clock():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, clock)

label = tk.Label(
    root,
    font=("Calibri", 50, "bold"),
    background="yellow",
    foreground="black"
)

label.pack(expand=True)

clock()

root.mainloop()