class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
def is_authenticated_decorator(function):
    def wrapper(*user, **kwargs):
        if user[0].is_logged_in == True:
            function(user[0])
    return wrapper
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}' blog post")
# new_user = User("Hashimi")
# new_user.is_logged_in = True
# create_blog_post(new_user)
"""
   *args - non-keyword arguments
   **kwargs - keyword arguments 
"""
# create_blog_post(new_user)
def order_pizza(size, *toppings):
    print(f"Ordered a {size} pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {toppings}")
# order_pizza("large", "pepporoni", "olives")
def fun(*args):
    return sum(args)
addition = fun(1, 2, 3, 4, 5, 6)
# print(addition)
def fun(**kwargs):
    for key, value in kwargs.items():
        return key, value
function = fun(a = 1, b = 2, c = 4)
# print(function)
def myFun(*argv):
    for arg in argv:
        return arg
my_fun = myFun("hello", "sayeed", "Hashimi")
def fun(arg1, *args):
    print("First argument: ", arg1)
    for arg in args:
        print("Argument *args :", arg)
# fun("Hello", "Welcome", "to", "GeeksforGeeks")
"""
    Python decorator (a function that takes 
                                    another function as an argument): 
                                        changes to a function without 
                                            changing the function itself directly
"""
"""
    Functions in Python are first-class citizens; meaning that
                                    1) functions can be assigned to a variable  
"""
def plus_one(number):
    return number + 1
addition_to_one = plus_one
# print(addition_to_one(15))
"""
                                    2) functions can be returned from a function
"""
def add_one(number):
    def one_add(number):
        return number + 1
    return one_add(number)
# print(add_one(3))
"""
                                    3) functions can be passed as an arguments to other functions
"""
def plus_two(number):
    return number + 1
def function_call(function):
    return function(5)
# print(function_call(plus_two))
"""
                                    4) functions can return other functions
"""
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
# print(hello())
"""
Understanding Closures: a nested function is allowed to access the outer scope 
                                                    of the enclosing function.
"""
def outer_function(message):
    def inner_function():
        print(f"Message from closure: {message}")
    return inner_function
closure_function = outer_function("Hello, closures!")
# closure_function()

"""
    We need a wrapper inside our decorator because the function get_ice_cream should be called whenever we want it,
                                                                            not when the decorator (add_sprinkles) is called!  
"""
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles💕")
        func(*args, **kwargs)
    return wrapper
def add_fudge(func):
    def wrapper():
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍧")
# get_ice_cream("Chocolate")
"""
    Exercise: Create a logging_decorator which is going to print 
                                    the name of the function that was called,
                                                    the arguments it was given and finally the returned output
"""
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(result)
    return wrapper
@logging_decorator
def a_function(*args):
    return sum(args)
a_function(1, 2, 3)




