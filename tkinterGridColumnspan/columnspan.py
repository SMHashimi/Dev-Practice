
from tkinter import *
examples = Tk()

red = Label(bg = "red", width = 20, height = 5)
red.grid(column = 0, row = 0)

green = Label(bg = "green", width = 20, height = 5)
green.grid(column = 1, row = 1)

blue = Label(bg = "blue", width = 40, height = 5)
blue.grid(column = 0, row = 2, columnspan = 2)



examples.mainloop()