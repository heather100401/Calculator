from tkinter import *
from tkinter import ttk

# create root window
root = Tk()

# root window title
root.title("Calculator")

# set screen size (widthxheight)
root.geometry('411x562')
root.resizable(0,0)     # prevent from being resized

input_text = ""

# button clicked functions

# places numbers pressed in frame
def onButtonClicked(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# clears expression
def onClearButtonClicked():
    global expression
    expression = ""
    input_text.set("")

# evaluates expression
def onEqualButtonClicked():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
    input_text = StringVar()

# input frame
# TODO: change background colors
input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

# frame

buttons_frame = Frame(root, width = 312, height = 272.5, bg = "grey")
buttons_frame.pack()


# buttons


# key bindings
# TODO: add other key bindings



root.mainloop()


