import tkinter as tk


class UI:
    walker_num = 0
    top = tk.Tk()
    C = tk.Canvas(top, width=900, height=450)

    def __init__(self, num):
        self.top.title("Simulate")
        self.top.geometry("2000x1000")
        self.top.resizable(width=False, height=False)
        self.C.pack()
        self.walker_num = num

    def init(self, info):
        for index in info:
            self.C.create_oval(index[0] * 50 - 10, index[1] * 50 - 10, index[0] * 50 + 10, index[1] * 50 + 10,
                               fill="yellow")
        self.C.update()

    def run(self):
        self.top.mainloop()
