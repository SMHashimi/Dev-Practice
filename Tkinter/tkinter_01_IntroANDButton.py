from tkinter import *

intro = Tk()
intro.title("The Introduction App")
intro.minsize(width = 800, height = 800)
intro.config(padx = 40, pady = 40)
#text in the interface
my_app = Label(text = "Hey, I am Sayed!\nWelcome to the first app I created in Tkinter library of Python",
               font = ("Arial", 16, "bold", "italic", "underline"))

# my_app.pack(pady = (40, 10))
my_app["text"] = "Hey, I am Mubaris"
my_app.config(text = "Hey, I am Mubaris.")
# my_app.pack(pady = (40, 10))
my_app.grid(column = 0, row = 0)

def button_clicked():
    print("I got clicked!")
    new_text = user_input.get()
    my_app.config(text = new_text)

button = Button(text = "Sign in Here", command = button_clicked)
button.grid(column = 1, row = 1)

user_input = Entry(width = 35)
user_input.grid(column = 3, row = 2)
# user_input.pack()
#You cannot use the grid and pack in the same file.

new_button = Button(text = "New button")
new_button.grid(column = 2, row = 0)

intro.mainloop()