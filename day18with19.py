#  day 18
# creating a scale

# # 1 tkinter import
# from tkinter import *
#
#
# # 7 define  submit
# def submit():
#     print("The temp is : " + scale.get() + "  degrees C ")
#
#
# # 2 window tk
# window = Tk()
#
# # 4 scale is measured 0 to 100
# scale = Scale(window, from_=0, to=100)
# # 5 scale pack
# scale.pack()
#
#
# # 6 adding a button and add text
#
# button = Button(window, text='submit', command=submit)
#
# #8 button pack
# button.pack()
# # 3 mainloop
# window.mainloop()

# ---------------------------------------------------------------------------
# listbox
# a listing of selectable text items within it's own container

# 9 submit function
def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ")
#18 list food
    for index in food:
        print(index)

#13 add function
def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

#14 delete function
def delete():
# delete multiple items
       for index in reversed(listbox.curselection()):
           listbox.delete(index)

       listbox.config(height=listbox.size())

# 1 from tkinter import
from tkinter import *



# 2 window
window = Tk()

# 4 listbox
listbox = Listbox(window,
                  bg="green",  # background color
                  font=("Constantia", 30),
                  width=10,
                  selectmode=MULTIPLE)
# 5
listbox.pack()

# 6 list of items
listbox.insert(1, "hamburger")
listbox.insert(2, "ice cream")
listbox.insert(3, "French Fries")
listbox.insert(4, "hot dog")

# 7 make listbox able to change size to fill the screen
listbox.config(height=listbox.size())

#10 someone can add something in the menu box
entryBox = Entry(window)
entryBox.pack()

# 8 create a submit button
submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

# 11 create  add button
addButton = Button(window, text="add", command=add)
addButton.pack()

# 14 create  Delete button
deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

# 3 window mainloop
window.mainloop()
