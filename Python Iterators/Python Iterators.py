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

# This will raise error, no items left
next(my_iter)