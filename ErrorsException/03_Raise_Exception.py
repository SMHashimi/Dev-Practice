#Raising your own error - Calculating your BMI
height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError(f"The {height}m is not considered a valid "
                     f"entry for human beings height.")
BMI = weight / height ** 2
print(BMI)






