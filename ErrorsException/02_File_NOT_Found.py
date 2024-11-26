#Creating the file
try:
    file = open("a_file.txt")
    a_dictionary = {"car": "toyota"}
    car_list = ["Toyota", "Lambo", "Bugatti", "Astin Martin"]
    fourth_item = car_list[3]
    print(a_dictionary["car"])
except FileNotFoundError:
    file = open("a_file.txt", mode = "w")
    file.write("Sayed\n")
    file.write("Ali")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
except IndexError:
    print(f"The list has 4 items. However, you can add your item to the list.")
    add_item = input("Type your item to include: ")
    car_list.append(add_item)
    # print(car_list)
else:
    content = file.read()
    print(content)
finally:
    file.close()