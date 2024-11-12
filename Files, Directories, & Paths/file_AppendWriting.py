with open("my_file.txt", mode = "a") as file:
    contents = file.write("\nPhone:No: ")

#Change the mode from w to a
print(contents) ##11 number of characters you wrote in the file .txt