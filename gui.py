from tkinter import *
from PIL import Image, ImageTk


resistors, coils = [], []

class ElComponents:

    counter = 0
    
    
   
    def __init__(self, startX, startY, compType = "resistor"):
        self.x = startX
        self.y = startY
        self.type = compType
        # self.left_node = left_node
        # self.right_node = right_node
        self.nodeX = 10
        self.nodeY = 20
        ElComponents.counter += 1


    def draw_node(self):
        pass


    def drag_start(self, event):
        widget = event.widget                               # makes this function compatible for all movable components. unless program would not distinct different components from each other, when moving
        widget.startX = event.x        
        widget.startY = event.y 


    def drag_motion(self, event):
        widget = event.widget                               # makes this function compatible for all movable components. unless program would not distinct different components from each other, when moving
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        self.width2 = widget.winfo_width()
        if(x > element_canvas.winfo_width() or y > element_canvas.winfo_height() + 15):            
            event.x = 0
            event.y = 0
        else: 
            widget.place(x=x,y=y)

            


    def draw_component(self):

        # canvas = Canvas(
        #                 ws,
        #                 height=500,
        #                 width=1000,
        #                 bg="#fff"
        #                 )

        # canvas.pack()

        # img = PhotoImage(file="resistor.png")
        # canvas.create_image(370, 200, image=img)

        # label.bind("<Button-1>",self.drag_start)
        # label.bind("<B1-Motion>",self.drag_motion)


       
      

        filename = str(self.type)               
        photo = PhotoImage(file = filename+".png")
        

        label = Label(window)        
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.config(height=35, width=100)
        #print(label.winfo_height())
        label.place(x = self.x, y = self.y)
        
      
        label.bind("<Button-1>",self.drag_start)
        label.bind("<B1-Motion>",self.drag_motion)


# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x        
#     widget.startY = event.y   


# def drag_motion(event):
#     widget = event.widget

#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y

#     print(widget.startX)

#     if(x < 550):
#         widget.place(x=x,y=y)
#     else: widget.place(x=widget.startX,y=widget.startY)

for i in range(5):
    coils.append(ElComponents(100, 0, "coil"))

for i in range(5):
    resistors.append(ElComponents(0, 0, "resistor"))


window = Tk()
window.geometry("700x500")

element_canvas = Canvas(window, bg = "white", height = 300, width = 550)
element_canvas.pack(pady = 50)


for resistor in resistors:
    resistor.draw_component()

for coil in coils:
    coil.draw_component()


button1=Button(window, text="generate CSV")
button1.pack()

#print(ElComponents.width2)
window.mainloop()






