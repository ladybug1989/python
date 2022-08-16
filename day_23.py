# canvas widget that is used to draw graphs, plots, images in a window

# from tkinter import *
#
# window = Tk()
#
# canvas = Canvas(window, height=500, width=500)
# pinkLine = canvas.create_line(0, 0, 500, 500, fill="pink", width=5)
# rectangle = canvas.create_rectangle(50, 50, 250, 250, fill="purple")
# triangle = canvas.create_polygon(250, 0, 500,500, 0,500, fill="orange")
# canvas.pack()
#
# window.mainloop()


# -------------------------------------------------------------------------
# drag & drop

# from tkinter import *
#
# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startX = event.y
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY+ event.y
#     widget.place(x=x, y=y)
#
# window = Tk()
#
# label = Label(window, bg="pink", width=10, height=5)
# label.place(x=0, y=0)
#
# label.bind("<Button-1>", drag_start)
# label.bind("<B1-Motion>", drag_motion)
# window.mainloop()

# -------------------------------------------------------------------------
# move images with keys

from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)

def move_left(event):
    label.place(x=label.winfo_x() -10, y=label.winfo_y() )

def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y() - 10)

window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<w>", move_right)

myimage = PhotoImage(file='flower.jpg')
label = Label(window, image=myimage)
label.place(x=0, y=0)

window.mainloop()
