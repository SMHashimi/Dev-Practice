

with open("./file1.txt") as file1:
    numbers_in_file1 = file1.readlines()
    # print(numbers_in_file1)
with open("./file2.txt") as file2:
    numbers_in_file2 = file2.readlines()
    # print(numbers_in_file1)
file1_as_integer = [int(number) for number in numbers_in_file1]
file2_as_integer = [int(number) for number in numbers_in_file2]
# print(file1_as_integer)
# print(file2_as_integer)
comparing_two_lists_of_integers = [number for number in file2_as_integer if number in file1_as_integer]
print(f"The result of comparing the two integer lists is: {comparing_two_lists_of_integers}")



