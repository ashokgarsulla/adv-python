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