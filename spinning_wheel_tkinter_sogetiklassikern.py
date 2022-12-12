import time
import random
import tkinter as tk

window = tk.Tk()

frame1 = tk.Canvas(master=window, width=600, height=500, borderwidth=1)
frame1.grid(row=0, column=0, padx=5, pady=5)

frame2 = tk.Canvas(master=window, width=200, height=500, borderwidth=1)
frame2.grid(row=0, column=1, padx=5, pady=5)

names = ['Jinci', 'Andreas']
points = [1, 3]
new_lst = [sum(points[:i]) for i in range(len(points))]
colors = ['red', 'blue']
assert len(names) == len(points), "the points doesn't match the number of people"
assert len(names) == len(colors), "the number of colors doesn't match the number of people"
arc_length = 360 / sum(points)

def create_legend(x, y, r, color, name, point):
    frame2.create_oval(x-r, y-r, x+r, y+r, fill=color)
    name_label = tk.Label(frame2, text=f'{name} ({point})', fg='black')
    frame2.create_window(x+2*r, y, window=name_label, anchor=tk.W)
for i, (color, name, point) in enumerate(zip(colors, names, points)):
    create_legend(20, 30+i*30, 10, color, name, point)
frame2.update()

for j in range(10,1,-1):
    for mvmt in range(360//j+1):
        frame1.delete('all')
        for i, c in enumerate(colors):
            start = new_lst[i] * arc_length
            extent = (points[i]) * arc_length
            arc = frame1.create_arc(10, 10, 490, 490, style=tk.PIESLICE, outline='black', fill=c, start=start+mvmt*j, extent=extent)
        arrow = frame1.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
        frame1.update()
        time.sleep(0.001)

for mvmt in range(random.randint(1,361)):
    frame1.delete('all')
    for i, c in enumerate(colors):
        start = new_lst[i] * arc_length
        extent = (points[i]) * arc_length
        arc = frame1.create_arc(10, 10, 490, 490, style=tk.PIESLICE, outline='black', fill=c, start=start+mvmt, extent=extent)
    arrow = frame1.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
    frame1.update()
    time.sleep(0.001)

frame1.delete(arrow)
for _ in range(5):
    arrow = frame1.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
    frame1.update()
    time.sleep(0.5)
    frame1.delete(arrow)
    frame1.update()
    time.sleep(0.5)
arrow = frame1.create_line(490, 250, 550, 250, arrow=tk.FIRST, width=5)
frame1.update()

window.mainloop()