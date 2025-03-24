import calculations as calc
from tkinter import *
from tkinter import ttk

# create root window
root = Tk()

# root window title
root.title("Calculator")
# set screen size (widthxheight)
root.geometry('411x562')

# frame
mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# buttons
clearButton = ttk.Button(mainframe, text="C").grid(column=1, row=1)
squareButton = ttk.Button(mainframe, text="x^2").grid(column=2, row=1)
percentageButton = ttk.Button(mainframe, text="%").grid(column=3, row=1)
divideButton = ttk.Button(mainframe, text="/").grid(column=4, row=1)

oneButton = ttk.Button(mainframe, text="1").grid(column=1, row=2)
twoButton = ttk.Button(mainframe, text="2").grid(column=2, row=2)
threeButton = ttk.Button(mainframe, text="3").grid(column=3, row=2)
multiplyButton = ttk.Button(mainframe, text="x").grid(column=4, row=2)

fourButton = ttk.Button(mainframe, text="4").grid(column=1, row=3)
fiveButton = ttk.Button(mainframe, text="5").grid(column=2, row=3)
sixButton = ttk.Button(mainframe, text="6").grid(column=3, row=3)
subtractButton = ttk.Button(mainframe, text="-").grid(column=4, row=3)

sevenButton = ttk.Button(mainframe, text="7").grid(column=1, row=4)
eightButton = ttk.Button(mainframe, text="8").grid(column=2, row=4)
nineButton = ttk.Button(mainframe, text="9").grid(column=3, row=4)
addButton = ttk.Button(mainframe, text="+").grid(column=4, row=4)

changeSignButton = ttk.Button(mainframe, text="+/-").grid(column=1, row=5)
zeroButton = ttk.Button(mainframe, text="0").grid(column=2, row=5)
periodButton = ttk.Button(mainframe, text=".").grid(column=3, row=5)
enterButton = ttk.Button(mainframe, text="=").grid(column=4, row=5)

# key bindings
root.bind("<Return>", enterButton)
# TODO: add other key bindings



root.mainloop()


