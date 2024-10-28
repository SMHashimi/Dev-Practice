class User:
    print("You are good to go!")
user_1 = User()
user_2 = User()
user_3 = User()
user_1.id = "2323"
user_1.name = "Sayed Mubaris"
print(user_1.name)
print(user_1.id)
user_2.id = "121"
user_2.name = "Sayed Mubaris Hashimi"
print(user_2.name)
print(user_2.id)
user_3.id = "323"
user_3.name = "Zaid Hashemi"
print(user_3.name)
print(user_3.id)

class User():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1
user_1 = User("Sayed Mubaris", 2323)
user_2 = User("Sayed Mubaris Hashimi", 121)
print(user_1.name)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
user_3 = User("Zaid Hashemi", 323)
print(f"The user_1 name is {user_1.name} with the ID of {user_1.id}")
print(f"The user_2 name is {user_2.name} with the ID of {user_2.id}")
print(f"The user_3 name is {user_3.name} with the ID of {user_3.id}")

class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breathe()
        print("They are doing this underwater")
    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.breath()
print(nemo.num_eyes)


import another_module
print(another_module.another_variable)

from another_module import another_variable
print(another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.circle(5)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over.")
my_dog = Dog("Alex", 12)

from another_module import another_variable
print(another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy.shape("turtle"))
timmy.color("coral")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Afghanistan", ["Kabul", "Kunduz", "Kandahar"])
table.add_column("Type", ["City", "District", "County"])
table.align = "l"
print(table)

class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1
#
user_1 = User("001", "Sayed Mubaris Hashimi")
user_2  = User("002", "Zaid Hashimi")

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

today, we are going to talk about object-oriented programming, known as procedural programming.
in this methods, we use classes. And from classes, we are going to create instances of those classes

# So, let's begin

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Peter", "10")
your_dog = Dog("Max", "8")          ##Multiple instances

print(f"My dog's name is {my_dog.name}")
my_dog.sit()
my_dog.roll_over()
print(f"Your dog's name is {your_dog.name} and is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

class CoffeMachine():
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
my_coffee = CoffeMachine("Americano", 50)
print(f"The coffe type is {my_coffee.type} and the amount is {my_coffee.amount}gr!")

class Restaurant():
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name= cuisine_name
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
restaurant = Restaurant("Bukhara", "Italian")
print(f"The restaurant is {restaurant.restaurant_name} and its cuisine is {restaurant.cuisine_name}!")
restaurant.open_restaurant()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
my_new_car = Car('Mercedez', "Maybach", "2024")
print(f"{my_new_car.model} {my_new_car.year} {my_new_car.make}")
my_new_car.read_odometer()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_desriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odomoter(self):
        print(f"This car has {self.odometer_reading} miles on it. ")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back on odometer")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car("Toyota", "Land Cruiser", "2024")
my_car.update_odometer(22)
print(f"I have {my_car.make} which is designed in {my_car.year} and tha model is {my_car.model}."
      f" Moreover, it has {my_car.odometer_reading} miles on it!")
my_car.read_odomoter()

class ElectrirCar(Car):     #child class
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_leaf = ElectrirCar("BENZ", "Maybach", "2023")
print(my_leaf. get_desriptive_name())
print(my_leaf.read_odomoter())

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting!")
    def roll_over(self):
        print(f"{self.name} rolled over!")
my_dog = Dog("Max", 8)
print(f"My dog's name is {my_dog.name}")
print(f"{my_dog.name} rolled over")

from pathlib import Path
path = Path("C:/Users/Sayed Mubaris H/OneDrive/Pictures/Desktop/python_file/pi_digits.txt")  #absolute file paths
reading = path.read_text()
reading = reading.rstrip()
print(reading)

from pathlib import Path
path = Path("pi_digits.txt")  #relative file path
reading = path.read_text()
print(reading)

from pathlib import Path
path = Path("pi_digits.txt")
reading = path.read_text()
separated_line = reading.splitlines()
for line in separated_line:
    print(line)

from pathlib import Path
path = Path("pi_digits.txt")
reading = path.read_text()
separated_line = reading.splitlines()
pi_string = ""
for line in separated_line:
    pi_string += line
print(pi_string.strip())
print(len(pi_string))

from pathlib import Path
path  = Path("pi_digits.txt")
reading = path.read_text()
print(reading)

from pathlib import Path
from sys import path_hooks
from tkinter.font import names

from unicodedata import lookup

path = Path('pi_digits.txt')
reading =  path.read_text()
separated_lines = reading.splitlines()
pi_string = ""
for line in separated_lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi! ")
else:
    print("Your birthday does not appear in the first million digits of pi.")


from pathlib import Path
path = Path("notepad_file.txt")
reading = path.read_text()
separated_lines = reading.splitlines()
for line in separated_lines:
    print(line.strip())



from pathlib import Path
path = Path("notepad_file.txt")
reading =  path.write_text("I am here to help!")
print(reading)

from pathlib import Path
path = Path("notepad_file.txt")
contents = "I love programming." + "\nYou should love it too." + "\nIt is not a bad thing to pursue."
reading = path.write_text(contents)
print(reading)

from pathlib import Path
path = Path("guest.txt")
users_name_string = ""
is_saving = True
while is_saving:
    putting_name = input("Do you want add your name, Type 'yes' or 'no': ")
    if putting_name.lower() == "yes":
        users_name = input("Please include your name: ").title()
        users_name_string += " " + users_name + "\n"
        writing_to_the_file = path.write_text(users_name_string)
    elif putting_name == "no".lower():
        print(writing_to_the_file)
        is_saving = False
        exit()
    else:
        print("You have typed wrong character. Please try again")
        is_saving = False
        exit()

zerodivisionerror
print(5 / 0)

print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst Number: ")
    if first_number == "q":
        break
    second_number = input("Second Number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(answer)

from pathlib import Path
path = Path("guest.txt")
try:
    reading = path.read_text()
except FileNotFoundError:
    print(f"Sorry the file {path} does not exist.")
else:
    words = reading.split() #This takes every word and put them in a list
    length_words = len(words)
    print(f"The file has {length_words} words!")

from pathlib import Path
import json
numbers  = [2, 4, 6, 7, 8]
path = Path('numbers.json')
reading = json.dumps(numbers)
path.write_text(reading)
#
from pathlib import Path
import json
path = Path('numbers.json')
reading = path.read_text()
numbers = json.loads(reading)
print(numbers)

from another_module import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'janis joplin'
print("You are good to go!")

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")













