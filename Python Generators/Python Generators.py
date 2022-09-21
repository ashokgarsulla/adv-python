# Python Generators : A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# /////////////////////////////////////////////////////////////////////////////////////////////////
# Create Generators in Python
# /////////////////////////////////////////////////////////////////////////////////////////////////
# It is as easy as defining a normal function, but with a "yield" statement instead of a "return" statement

# Generating Even number using custome iterator
from tkinter import N


class Even:
    def __init__(self,max):
        self.n = 2
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max :
            result = self.n
            self.n  = self.n + 2
            return result
        else:
            raise StopIteration

print("*"*20,"LINE 23","*"*20)
numbers = Even(10)
for i in numbers:
    print(i)

print("*"*20,"LINE 28","*"*20)
even_objext_for_iter = Even(20)
my_iter = iter(even_objext_for_iter)
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())


# /////////////////////////////////////////////////////////////////////////////////////////////////
# Create Generators in Python
# /////////////////////////////////////////////////////////////////////////////////////////////////
# ------------ IMPORTANT POINTS  ---------------
# * It is as easy as defining a normal function, but with a yield statement instead of a return statement

# * If a function contains at least one yield statement (it may contain other yield or return statements), 
# it becomes a generator function. Both yield and return will return some value from a function.
# * The difference is that while a return statement terminates a function entirely, yield statement 
# pauses the function saving all its states and later continues from there on successive calls.

def even_generator():
    n = 0

    n += 2
    yield n

    n += 2
    yield n

    
    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

print("*"*20,"LINE 80","*"*20)
# It returns an object but does not start execution immediately.
gen_obj = even_generator()

for i in gen_obj:
    print(i)

print("*"*20,"LINE 86","*"*20)
my_gen_obj = even_generator()

# We can iterate through the items using next().
print(my_gen_obj.__next__())
print(my_gen_obj.__next__())
print(my_gen_obj.__next__())
# we can also write
print(next(my_gen_obj))
print(next(my_gen_obj))
print(next(my_gen_obj))
# print(next(my_gen_obj)) 
# // It will give StopIteration 
#  bcz:Finally, when the function terminates, StopIteration is raised automatically on further calls

# /////////////////////////////////////////////////////////////////////////////////////////////////
# Python Generators with a Loop
# /////////////////////////////////////////////////////////////////////////////////////////////////


def even_generator(max):
    for i in range(2,max,2):
        yield i

print("*"*20,"LINE 110","*"*20)
even_loo_obj = even_generator(20)
for i in even_loo_obj:
    print(i)
print("*"*20,"LINE 114","*"*20)
my_even_loo_obj = even_generator(20)
print(next(my_even_loo_obj))
print(next(my_even_loo_obj))
print(next(my_even_loo_obj))

print(my_even_loo_obj.__next__())
print(my_even_loo_obj.__next__())
print(my_even_loo_obj.__next__())