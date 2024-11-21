from tkinter import *

intro = Tk()
intro.title("The Introduction App")
intro.minsize(width = 800, height = 800)
#text in the interface
my_app = Label(text = "Hey, I am Sayed!\nWelcome to the first app I created in Tkinter library of Python",
               font = ("Arial", 16, "bold", "italic", "underline"))
my_app.pack(pady = (40, 10))
my_app["text"] = "Hey, I am Mubaris"
my_app.config(text = "Hey, I am Mubaris.")



def button_clicked():
    print("I got clicked!")
    new_text = user_input.get()
    my_app.config(text = new_text)

button = Button(text = "Sign in Here", command = button_clicked)
button.pack(pady = 10)
user_input = Entry(width = 35)
user_input.pack()









intro.mainloop()



