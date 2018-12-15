import tkinter as tk

top = tk.Tk()
top.title("Simulate")
top.geometry("720x480")
top.resizable(width=False, height=False)

C = tk.Canvas(top, width=720, height=480)
C.pack

pos_list = []

for i in range(1700):
    for index in p_l:
        a = C.create_oval(index[0] * 50 - 10, index[1] * 50 - 10, index[1] * 50 + 10, fill='blue')
    pos_list.append(p_l)

C.update()

p_l, v_l = generate_list(p_l, v_l, i_l)
C.delete("all")

top.mainloop()
