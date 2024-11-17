
#1
#Creating a list from the previous list is called list comprehension
numbers = [4, 7, 90]
#The task is to add each number in the list by 1
add_list = []
for num in numbers:
    added_num = num + 1
    add_list.append(added_num)     #as you can see, it takes more than 5 lines of codes to achieve it. We can minimize it by using list comprehension.
print(add_list)

numbers = [4, 7, 90]
add_list = [num + 1 for num in numbers]
print(add_list)                          #In just 3 lines of codes, it is done.

#2
names_to_four = []
name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
for n in name:
    if len(n) == 4:
        names_to_four.append(n)
print(names_to_four)

result = [n for n in name if len(n) == 4]
print(result)

#3
list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
numbers = [int(number) for number in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

