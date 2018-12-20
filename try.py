import tkinter as tk
import random

walker_num = 0
top = tk.Tk()
C = tk.Canvas(top, width=900, height=450)
top.title("Simulate")
top.geometry("2000x1000")
top.resizable(width=False, height=False)
C.pack()
C.create_oval(40, 40, 60, 60, fill="yellow")
C.update()
top.mainloop()