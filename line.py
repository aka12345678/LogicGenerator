from tkinter import *


canvas = Canvas(bg="white", width=600, height=400)
canvas.pack()

store = {'x':0,"y":0,"x2":0,"y2":0} #store values in a map  x,y:start   x2,y2:end  

def click(c):
    store['x'] = c.x
    store['y'] = c.y

def release(l):
    store['x2'] = l.x
    store['y2'] = l.y
    draw() # Release the mouse and draw

def draw():
    canvas.create_line(store['x'],store['y'],store['x2'],store['y2'])

canvas.bind('<ButtonPress-1>', click)
canvas.bind('<ButtonRelease-1>', release)

mainloop()