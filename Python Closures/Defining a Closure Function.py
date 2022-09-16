def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()


# ////////////////////////////////////////////////////
# When do we have closures?
# ////////////////////////////////////////////////////
# 1.We must have a nested function (function inside a function).
# 2.The nested function must refer to a value defined in the enclosing function.
# 3.The enclosing function must return the nested function.

# ////////////////////////////////////////////////////
# When to use closures?
# ////////////////////////////////////////////////////
# So what are closures good for?

# Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

# When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.

# Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

#///////////////////////////////////////////////////////////////////
#On a concluding note, it is good to point out that the values that 
# get enclosed in the closure function can be found out.
# All function objects have a __closure__ attribute that returns a 
# tuple of cell objects if it is a closure function. Referring to the
#  example above, we know times3 and times5 are closure functions.

# It will print Nothing
print(make_multiplier_of.__closure__)


# It will print object address
print(times3.__closure__)

# It will print content
print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)

#///////////////////////////////////////////////////////////////////