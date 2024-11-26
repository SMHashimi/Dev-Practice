# FileNOTFound
with open("./data.txt") as data:
    data.read()

# KeyError
a_dictionary = {
    "key": 9,
    "value": 10
}
print(a_dictionary["degree"])

# IndexError
car_list = ["Toyota", "Lambo", "Astin Martin"]
print(car_list[3])

# TypeError
text = ["a", "b"]
character = "a"
text + character

car_list = ["Lambo", "Benz", "Bugatti"]
try:
    car_list[3]
except:
    print("You are trying to get an item beyond the limit!")