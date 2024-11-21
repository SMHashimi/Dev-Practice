from tkinter import *

#Importing Tk class (from tkinter module) - and setting up the window size
widget_window = Tk()
widget_window.title("Widgets Illustrations")
widget_window.minsize(height = 700, width  = 700)

##creating a text in the widget_window and re-edit it by .config
widget_label = Label(text = "Welcome to the widgets created by Sayed!",
                     font = ("Arial", 15, "bold", "italic"))
widget_label.pack(pady = (50, 25))
widget_label.config(text = "Hi, this is Sayed. Welcome to the first Tkinter library app in Python.")

#changing the widget_label to another text when 'Press me' is pressed.
def action():
    widget_label.config(text = "Hi, this is Hashimi. How can I help you?",)
button = Button(text = "Press me", command = action)
button.pack()

#user input in the Entry dedicated. END means the text starts at the end of the previous text (Your Email:)
user_entry = Entry(width = 70)
user_entry.insert(END, string = "Your Email: ")
user_entry.pack(pady = (25))

#Creating a somewhat big screen to put text
a_void_for_text = Text(height = 5, width = 53)
a_void_for_text.focus()
a_void_for_text.insert(END, "Please Share your experiences here: ")
print(a_void_for_text.get("1.0", END))
a_void_for_text.pack(pady = (20))

#Creating spinbox
def spin_box():
    print(spinbox_roller.get())
spinbox_roller  = Spinbox(from_ = -4, to = 20, command = spin_box, width  = 5)
spinbox_roller.pack(pady = (10))

#Creating a scale - What is the reason for the value here? - The value here is the current position of slider on the scale.
def scale_value(value):
    print((value))
scale = Scale(from_ = 1, to = 300, command = scale_value)
scale.pack()

#Creating Checkbutton - you can choose more than one options
def state_checked():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text = "Is On?)", variable = checked_state, command = state_checked)
checkbutton.pack(pady = (5))

#Creating a Radiobutton - you only choose one option among the two.
def radio_result():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value = 1, variable = radio_state, command = radio_result)
radiobutton2 = Radiobutton(text="Option 2", value = 2, variable = radio_state, command = radio_result)
radiobutton1.pack(pady = (5, 0))
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack(pady = (10))

widget_window.mainloop()