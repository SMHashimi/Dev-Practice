#arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
addition = add(3, 5, 6, 12, 12, 334, 45, 54, 64, 675, 23, 23, 64)
# print(addition)

def calculate(n, **kwargs):
    add_value = kwargs["add"]
    add_value += n
    return add_value
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # n += kwargs["add"]
    # n *= kwargs["multiply"]
    # print(n)
    # print(kwargs)
print(calculate(4, add = 3))

# kw["name"] = "IS500"

class Car:
    def __init__(self, **kw):   #Advanced Keyword Arguments
        self.name = kw["name"]
        self.model = kw["model"]
        self.brand = kw["brand"]
my_car = Car(name = 'IS500', model = "2024", brand = "Lexus")
print(my_car.name)
print(my_car.model)
print(my_car.brand)

