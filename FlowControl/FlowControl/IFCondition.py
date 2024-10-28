##

name = input("Please enter your name: ")

age =  int(input("{0}, How old are you? " .format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years" . format(18  - age))
