# Python Generators : A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# /////////////////////////////////////////////////////////////////////////////////////////////////
# Create Generators in Python
# /////////////////////////////////////////////////////////////////////////////////////////////////
# It is as easy as defining a normal function, but with a "yield" statement instead of a "return" statement

# Generating Even number using custome iterator
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