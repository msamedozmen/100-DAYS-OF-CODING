from flask import Flask


# class User():
#     def __init__(self,name):
#         self.name = name
#         self.is_login = False
        


# def is_authenticaed_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_login == True:
#             function(args[0])
            
#     return wrapper

# @is_authenticaed_decorator
# def create_blog(user):
#     print(f"This is {user.name}")
    
    
# user_name = User("Samet")

# user_name.is_login =True

# create_blog(user_name)

# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0],args[1],args[2])
        print(f"It returned {result}")
    return wrapper

# Use the decorator 👇

@logging_decorator
def a_function(*args):
    sum=1
    for sumx in args:
        sum =sumx*sum
    return sum
a_function(1,2,4)