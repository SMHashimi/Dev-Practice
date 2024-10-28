age = int(input("What is your age? "))
if age == 900 :
    print("Please come back in {0} years" .format(18 - age))
elif age < 900:
    print("Sorry,  Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

x = int(input("Type your number: "))
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")

