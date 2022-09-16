# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Python Decorators
# -----------------------------------------------------------------------------------------------------------------------
#- A decorator takes in a function, adds some functionality and returns it. In this tutorial, 
# you will learn how you cancreate a decorator and why you should use it.
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Decorators in Python 
# -----------------------------------------------------------------------------------------------------------------------
# * Python has an interesting feature called decorators to add functionality to an existing code.
# * This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////       CODE      /////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


ordinary()  # OUTPUT: I am ordinary

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()

# -----------------------------------------------------------------------------------------------------------------------
# We can use the @ symbol along with the name of the decorator function and place it above
# the definition of the function to be decorated. For example,

@make_pretty
def ordinary():
    print("I am ordinary")

print("-" *30)
ordinary()

# is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
print("-" *30,'LINE 56',"-" *30)
ordinary()
# -----------------------------------------------------------------------------------------------------------------------
# Decorating Functions with Parameters
# -----------------------------------------------------------------------------------------------------------------------

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

print("-" *30,'LINE 69',"-" *30)
@smart_divide
def divide(a, b):
    print(a/b)
divide(3,2)

# -----------------------------------------------------------------------------------------------------------------------
# Chaining Decorators in Python
# -----------------------------------------------------------------------------------------------------------------------
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)
    
printer("Hello")
# -----------------------------------------------------------------------------------------------------------------------