import time
import random
import tkinter as tk

window = tk.Tk()
window.geometry('700x500')

canvas = tk.Canvas(window)
canvas.pack(expand=True, fill='both')

in_list = [1,1,2,5,1, 10]
new_lst = [sum(in_list[:i]) for i in range(len(in_list))]
color = ['red', 'blue', 'yellow', 'green', 'magenta', 'cyan']
assert len(in_list) == len(color), 'the number of colors are wrong...'
arc_length = 360 / sum(in_list)

for j in range(10,1,-1):
    for mvmt in range(360//j+1):
        canvas.delete('all')
        for i, c in enumerate(color):
            start = new_lst[i] * arc_length
            extent = (in_list[i]) * arc_length
            arc = canvas.create_arc(10, 10, 490, 490, style=tk.PIESLICE, outline='black', fill=c, start=start+mvmt*j, extent=extent)
        arrow = canvas.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
        window.update()
        time.sleep(0.001)

for mvmt in range(random.randint(1,361)):
    canvas.delete('all')
    for i, c in enumerate(color):
        start = new_lst[i] * arc_length
        extent = (in_list[i]) * arc_length
        arc = canvas.create_arc(10, 10, 490, 490, style=tk.PIESLICE, outline='black', fill=c, start=start+mvmt, extent=extent)
    arrow = canvas.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
    window.update()
    time.sleep(0.001)

canvas.delete(arrow)
for _ in range(5):
    arrow = canvas.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
    window.update()
    time.sleep(0.5)
    canvas.delete(arrow)
    window.update()
    time.sleep(0.5)
arrow = canvas.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
window.update()

window.mainloop()