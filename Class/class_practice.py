# class User:
#     print("You are good to go!")
# user_1 = User()
# user_2 = User()
# user_3 = User()
# user_1.id = "2323"
# user_1.name = "Sayed Mubaris"
# print(user_1.name)
# print(user_1.id)
# user_2.id = "121"
# user_2.name = "Sayed Mubaris Hashimi"
# print(user_2.name)
# print(user_2.id)
# user_3.id = "323"
# user_3.name = "Zaid Hashemi"
# print(user_3.name)
# print(user_3.id)
#
# class User():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.followers = 0
#         self.following = 0
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
# user_1 = User("Sayed Mubaris", 2323)
# user_2 = User("Sayed Mubaris Hashimi", 121)
# print(user_1.name)
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
# user_3 = User("Zaid Hashemi", 323)
# print(f"The user_1 name is {user_1.name} with the ID of {user_1.id}")
# print(f"The user_2 name is {user_2.name} with the ID of {user_2.id}")
# print(f"The user_3 name is {user_3.name} with the ID of {user_3.id}")
#
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, exhale.")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breath(self):
#         super().breathe()
#         print("They are doing this underwater")
#     def swim(self):
#         print("Moving in water")
#
# nemo = Fish()
# nemo.breath()
# print(nemo.num_eyes)
#
#
# import another_module
# print(another_module.another_variable)
#
# from another_module import another_variable
# print(another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.circle(5)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
# from prettytable import PrettyTable
# table = PrettyTable()
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#     def roll_over(self):
#         print(f"{self.name} rolled over.")
# my_dog = Dog("Alex", 12)
#
# from another_module import another_variable
# print(another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy.shape("turtle"))
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Afghanistan", ["Kabul", "Kunduz", "Kandahar"])
# table.add_column("Type", ["City", "District", "County"])
# table.align = "l"
# print(table)
#
# class User:
#
#     def __init__(self, id, username):
#         self.id = id
#         self.username = username
#         self.follower = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.follower += 1
#         self.following += 1
# #
# user_1 = User("001", "Sayed Mubaris Hashimi")
# user_2  = User("002", "Zaid Hashimi")
#
# user_1.follow(user_2)
#
# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)
#
# today, we are going to talk about object-oriented programming, known as procedural programming.
# in this methods, we use classes. And from classes, we are going to create instances of those classes
#
# # So, let's begin
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f"{self.name} is now sitting")
#
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
#
# my_dog = Dog("Peter", "10")
# your_dog = Dog("Max", "8")          ##Multiple instances
#
# print(f"My dog's name is {my_dog.name}")
# my_dog.sit()
# my_dog.roll_over()
# print(f"Your dog's name is {your_dog.name} and is {your_dog.age} years old")
# your_dog.sit()
# your_dog.roll_over()
#
# class CoffeMachine():
#     def __init__(self, type, amount):
#         self.type = type
#         self.amount = amount
# my_coffee = CoffeMachine("Americano", 50)
# print(f"The coffe type is {my_coffee.type} and the amount is {my_coffee.amount}gr!")
#
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_name):
#         self.restaurant_name = restaurant_name
#         self.cuisine_name= cuisine_name
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")
# restaurant = Restaurant("Bukhara", "Italian")
# print(f"The restaurant is {restaurant.restaurant_name} and its cuisine is {restaurant.cuisine_name}!")
# restaurant.open_restaurant()
#
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 23
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
# my_new_car = Car('Mercedez', "Maybach", "2024")
# print(f"{my_new_car.model} {my_new_car.year} {my_new_car.make}")
# my_new_car.read_odometer()
#
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_desriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name
#     def read_odomoter(self):
#         print(f"This car has {self.odometer_reading} miles on it. ")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back on odometer")
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
# my_car = Car("Toyota", "Land Cruiser", "2024")
# my_car.update_odometer(22)
# print(f"I have {my_car.make} which is designed in {my_car.year} and tha model is {my_car.model}."
#       f" Moreover, it has {my_car.odometer_reading} miles on it!")
# my_car.read_odomoter()
#
# class ElectrirCar(Car):     #child class
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
# my_leaf = ElectrirCar("BENZ", "Maybach", "2023")
# print(my_leaf. get_desriptive_name())
# print(my_leaf.read_odomoter())
#
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting!")
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
# my_dog = Dog("Max", 8)
# print(f"My dog's name is {my_dog.name}")
# print(f"{my_dog.name} rolled over")
#
# from pathlib import Path
# path = Path("C:/Users/Sayed Mubaris H/OneDrive/Pictures/Desktop/python_file/pi_digits.txt")  #absolute file paths
# reading = path.read_text()
# reading = reading.rstrip()
# print(reading)
#
# from pathlib import Path
# path = Path("pi_digits.txt")  #relative file path
# reading = path.read_text()
# print(reading)
#
# from pathlib import Path
# path = Path("pi_digits.txt")
# reading = path.read_text()
# separated_line = reading.splitlines()
# for line in separated_line:
#     print(line)
#
# from pathlib import Path
# path = Path("pi_digits.txt")
# reading = path.read_text()
# separated_line = reading.splitlines()
# pi_string = ""
# for line in separated_line:
#     pi_string += line
# print(pi_string.strip())
# print(len(pi_string))
#
# from pathlib import Path
# path  = Path("pi_digits.txt")
# reading = path.read_text()
# print(reading)
#
# from pathlib import Path
# from sys import path_hooks
# from tkinter.font import names
#
# from unicodedata import lookup
#
# path = Path('pi_digits.txt')
# reading =  path.read_text()
# separated_lines = reading.splitlines()
# pi_string = ""
# for line in separated_lines:
#     pi_string += line.strip()
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi! ")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
#
#
# from pathlib import Path
# path = Path("notepad_file.txt")
# reading = path.read_text()
# separated_lines = reading.splitlines()
# for line in separated_lines:
#     print(line.strip())
#
#
#
# from pathlib import Path
# path = Path("notepad_file.txt")
# reading =  path.write_text("I am here to help!")
# print(reading)
#
# from pathlib import Path
# path = Path("notepad_file.txt")
# contents = "I love programming." + "\nYou should love it too." + "\nIt is not a bad thing to pursue."
# reading = path.write_text(contents)
# print(reading)
#
# from pathlib import Path
# path = Path("guest.txt")
# users_name_string = ""
# is_saving = True
# while is_saving:
#     putting_name = input("Do you want add your name, Type 'yes' or 'no': ")
#     if putting_name.lower() == "yes":
#         users_name = input("Please include your name: ").title()
#         users_name_string += " " + users_name + "\n"
#         writing_to_the_file = path.write_text(users_name_string)
#     elif putting_name == "no".lower():
#         print(writing_to_the_file)
#         is_saving = False
#         exit()
#     else:
#         print("You have typed wrong character. Please try again")
#         is_saving = False
#         exit()
#
# zerodivisionerror
# print(5 / 0)
#
# print("Give me two numbers, and I'll divide them")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == "q":
#         break
#     second_number = input("Second Number: ")
#     if second_number == "q":
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You cannot divide by zero")
#     else:
#         print(answer)
#
# from pathlib import Path
# path = Path("guest.txt")
# try:
#     reading = path.read_text()
# except FileNotFoundError:
#     print(f"Sorry the file {path} does not exist.")
# else:
#     words = reading.split() #This takes every word and put them in a list
#     length_words = len(words)
#     print(f"The file has {length_words} words!")
#
# from pathlib import Path
# import json
# numbers  = [2, 4, 6, 7, 8]
# path = Path('numbers.json')
# reading = json.dumps(numbers)
# path.write_text(reading)
# #
# from pathlib import Path
# import json
# path = Path('numbers.json')
# reading = path.read_text()
# numbers = json.loads(reading)
# print(numbers)
#
# from another_module import get_formatted_name
#
# def test_first_last_name():
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'janis joplin'
# print("You are good to go!")
#
# print("Enter 'q' at any time to quit.")
#
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print(f"\tNeatly formatted name: {formatted_name}")
class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is not sitting!")
    def roll_over(self):
        print(f"{self.name} rolled over!")
his_dog = Dog("German Sheperd", 6)
your_dog = Dog("Hosky", "11")
# print(f"My dog's name is {your_dog.name} sitting now and is {your_dog.age} years old."
#       f" However, his dog's name is {his_dog.name} and {his_dog.age} years old!")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name: {self.restaurant_name} "
                  f"\nThe cuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open right now!")
restaurant = Restaurant("Shah Halal's Food", "Italian")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"The user's first name: {self.first_name}\n"
              f"The user's last name: {self.last_name}")
    def greet_user(self):
        print(f"Welcome, {self.first_name + self.last_name}")
users1 = User("Sayed Hashimi", " Mubaris")
# users1.describe_user()
# users1.greet_user()
user2 = User("Zaid", " Hashimi")
# user2.greet_user()
class Car:
    """
    A simple attempt to represent a car.
    Initialize attributes to describe a car.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        """
            Not all cars has o mile on them. 
            We are going to change it in three ways:
            First, we are going to change it directly.
        """
        self.odometer = 0
    def get_descriptive_name(self):
        """We are going to return a neatly formatted descriptive name"""
        neatly_descriptive_name = (f"My car is: {self.make} {self.model} {self.year}").title()
        return neatly_descriptive_name
    """Changing the attrbute Odometer through a method"""
    def update_odometer(self, mileage):
        self.odometer = mileage
        """
            Or, increment the odometer in a method
        """
    def increment_odometer(self, miles):
        self.odometer += miles
    def read_odometer(self):
        """We are going to print a statement showing the car's mileage"""
        print(f"The car has {self.odometer} miles on it!")
    def fill_gas_tank(self):
        print("Please fill the gask tank. It's been two weeks since you filled the gask tank of your car.")
my_car = Car("TOYOTA", "CAMRY XSE", 2024)
# print(my_car.get_descriptive_name())
"""
    Changing the value of odometer 
    (an attribute) 
    directly
"""
my_car.odometer = 23
"""
    Changing the value of odometer 
    (an attribute) 
    through a method.
    Or, incrementing the odometer value in a method
"""
# my_car.update_odometer(0)
# my_car.read_odometer()
# my_car.increment_odometer(100)
# my_car.read_odometer()
"""
        Inheritance in Python Class:
        We are going to still use __init__ method to use child class.
        For example, let's consider an ElectricCar
"""
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        We are going to initialize of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40
    def describe_battery(self):
        print(f"This car has a {self.battery_size}--kw battery.")
    def fill_gas_tank(self):
        print("This car does not have a gas tank!")
my_electricCar = ElectricCar(make = "Toyota", model = "Toyota Camry 2024", year =  2024)
# my_electricCar.fill_gas_tank()
# my_electricCar.fill_gas_tank()
"""
    Sometimes, when our project becomes larger and larger, we can separate a 
    portion of our first class's into another class   
"""
""" Exercise:
        An ice cream stand is a specific kind of restaurant. Write
        a class called IceCreamStand that inherits for the Restaurant class (line 400).
        Either version of the class will work; just pick the one you like better.
        Add an attribute called flavors that stores a list of ice cream flavors. Write a 
        method that displays these flavors. Create an instance of IceCreamStand, an call this method.
"""
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    def display_flavors(self):
        self.flavors = ["Vanilla", "Chocolate", "BlueBerry"]
        iccream_flavors = ""
        for flavor in self.flavors:
            iccream_flavors  = iccream_flavors + " \n\t" +  flavor
        print(f"The {self.restaurant_name} offers {self.cuisine_type} cuisine, and the following"
              f" IceCreamStand type is available currently:{iccream_flavors} ")
flavors = IceCreamStand("Shah Halal's Food", "German")
# flavors.display_flavors()
""" 
Let's consider the example of employees in a company.
"""
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "2018@gmail.com"
    def fullname(self):
        return "{} {}".format(self.first, self.last)
emp_1 = Employee(first = "Mubaris", last = "Hashimi", pay = 50000)
print(f"Employee Full Name: {emp_1.first} {emp_1.last}\nEmployee Salary: {emp_1.pay}$ annually\nEmployee E-mail: {emp_1.email}")



