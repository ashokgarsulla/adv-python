# Python Iterators:Iterators are objects that can be iterated upon.
# In this tutorial, you will learn how iterator works and how you can
# build your own iterator using __iter__ and __next__ methods.

# //////////////////////////////////////////////////////////////////////////
# Iterating Through an Iterator
# //////////////////////////////////////////////////////////////////////////
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left //=>  StopIteration
# next(my_iter)

# ///////// StopIteration error will automatically solve by for loop
print("*"*20,"LINE 35","*"*20)
for i in my_list:
    print(i)

# //////////////////////////////////////////////////////////////////////////
# Working of for loop for Iterators
# //////////////////////////////////////////////////////////////////////////
print("*"*20,"LINE 42","*"*20)
test_list = [1,2,3,4,5]
for element in test_list:
    print(element)

#

print("*"*20,"LINE 49","*"*20)
# create an iterator object from that iterable
iter_obj = iter(test_list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
# -------------------------- NOTES START ----------------------------------------------------------
# So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

# Ironically, this for loop is actually an infinite while loop.

# Inside the loop, it calls next() to get the next element and executes the body of the for loop with
#  this value. After all the items exhaust, StopIteration is raised which is internally caught and the loop ends. 
#  Note that any other kind of exception will pass through.
        break
# -------------------------- NOTES END ----------------------------------------------------------

# //////////////////////////////////////////////////////////////////////////
# Building Custom Iterators
# //////////////////////////////////////////////////////////////////////////
# Building an iterator from scratch is easy in Python. We just have to implement the __iter__() and the __next__() methods.
# The __iter__() method returns the iterator object itself. If required, some initialization can be performed.
# The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        print(self.n)
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


print("*"*20,"LINE 102","*"*20)
# create an object
numbers = PowTwo(3)
for i in numbers:
    print(i)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

# We can also use a for loop to iterate over our iterator class
print("*"*20,"LINE 119","*"*20)
for i in PowTwo(5):
    print(i)


# //////////////////////////////////////////////////////////////////////////
# Python Infinite Iterators
# //////////////////////////////////////////////////////////////////////////
# The built-in function iter() can be called with two arguments where the first argument must be a callable object (function) 
# and second is the sentinel. The iterator calls this function until the returned value is equal to the sentinel.

print("*"*20,"LINE 130","*"*20)

print(int())
inf = iter(int,1)
# output will zero
print(next(inf)) 
# output will zero
print(next(inf))

# We can see that the int() function always returns 0. So passing it as iter(int,1) will return an iterator that calls 
# int() until the returned value equals 1. This never happens and we get an infinite iterator.