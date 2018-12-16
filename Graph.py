import tkinter as tk


class UI:
    walker_num = 0
    top = tk.Tk()
    C = tk.Canvas(top, width=800, height=700)

    def __init__(self, num):
        self.top.title("Simulate")
        self.top.geometry("800x700")
        self.top.resizable(width=False, height=False)
        self.C.pack()
        self.walker_num = num
        self.C.create_rectangle(3.41 * 50, (10.28 - 0.53) * 50, 12.46 * 50, 10.28 * 50, fill="gray")
        self.C.create_rectangle(9.33 * 50, 6.32 * 50, 9.91 * 50, 7.50 * 50, fill="gray")
        self.C.create_rectangle(3.41 * 50, 3.21 * 50, 3.94 * 50, 10.28 * 50, fill="gray")
        self.C.create_rectangle(3.41 * 50, 3.21 * 50, 12.46 * 50, 3.74 * 50, fill="gray")
        self.C.create_rectangle((12.46 - (3.94 - 3.41)) * 50, 7.39 * 50, 12.46 * 50, 10.28 * 50, fill="gray")
        self.C.create_rectangle((12.46 - (3.94 - 3.41)) * 50, 3.21 * 50, 12.46 * 50, 6.39 * 50, fill="gray")

    def init(self, info):
        for index in info:
            self.C.create_oval(index[0] * 50 - 10, index[1] * 50 - 10, index[0] * 50 + 10, index[1] * 50 + 10,
                               fill="yellow")
        self.C.update()

    def run(self):
        self.top.mainloop()
