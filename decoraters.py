import functools
import time
def valid(func):
    def inner(a,b):
        if not isinstance(a,str):
            a=str(a)
        if not isinstance(b,str):
            b=str(b)
            func(a,b)
    return inner
@valid
def fun(a:str,b:str)->str:
    """This is a docstring, This function is for concatenation"""
    return a+b
print(fun.__annotations__)
print(fun.__doc__)
print(print.__doc__)




def dec(func):
    print("Function called")
    def inner():
        print("Starting Function")
        print(f"Func:{func.__name__}")
        func()
        print("Ending Function")
    return inner
@dec
def greet():
    print("hello bro")
greet()
print(f"greet:{greet.__name__}")




def login(func):
    us={"rama":"rama12", "teju":"teju12", "kavya":"kavya12"}
    def inner():
        user=input("enter your username:")
        password=input("enter your password:")
        if user in us.keys():
            if password==us[user]:
                print("login successful")
                func()
            else:
                print("wrong password")
        else:
            print("user not found")
    return inner
@login
def file():
    print("secured file")
file()
