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


# even series infnite nenerator
def infnite_even_generator():
    n = 0
    while True:
        n += 2
        yield n

print("*"*20,"LINE 132","*"*20)
inf_even_obj = infnite_even_generator()
for i in range(10):
    print(inf_even_obj.__next__())

# /////////////////////////////////////////////////////////////////////////////////////////////////
# Python Generator Expression
# /////////////////////////////////////////////////////////////////////////////////////////////////
# The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.
# The major difference between a list comprehension and a generator expression is that a 
# => list comprehension produces the entire list 
# =>while the generator expression produces one item at a time.
# They have lazy execution ( producing items only when asked for ). For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print("*"*20,"LINE 157","*"*20)
print(list_)

print("*"*20,"LINE 160","*"*20)
# It will print genrator object
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# /////////////////////////////////////////////////////////////////////////////////////////////////
# Use of Python Generators
# /////////////////////////////////////////////////////////////////////////////////////////////////
# 1. Easy to Implement
# 2. Memory Efficient
# 3. Represent Infinite Stream
# 4. Pipelining Generators

#  difficulty in  using iterartor
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# Using above code in generator
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1