# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Python property decorator
# -----------------------------------------------------------------------------------------------------------------------
# Python programming provides us with a built-in @property decorator which makes usage 
# of getter and setters much easier in Object-Oriented Programming.
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Class Without Getters and Setters
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Basic method of setting and getting attributes in Python
from tempfile import TemporaryDirectory


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())

print(human.__dict__)





# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Using Getters and Setters
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

print("*"*20,"LINE 61","*"*20)

# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation 
# updated temprature 
human.set_temperature(55)
print(human.get_temperature())

# Get the to_fahreheit method
print(human.to_fahrenheit())



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# The property Class
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)



print("*"*20,"LINE 112","*"*20)
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

# It will give value error
# human.temperature = -300

human.temperature = 75
print(human.temperature)
print(human.to_fahrenheit())

# ------------------------------------------- NOTE --------------------------------------------------------------------
# self.temperature = temperature. This expression automatically calls set_temperature().
# self.temperature. This expression automatically calls set_temperature().
# c = Celcius(30)
# c.temperature automatically calls get_temperature()
# Note: The actual temperature value is stored in the private _temperature variable. 
# The temperature attribute is a property object which provides an interface to this private variable.

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# The @property Decorator
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
# property(fget=None, fset=None, fdel=None, doc=None)'

# where,

# fget is function to get value of the attribute
# fset is function to set value of the attribute
# fdel is function to delete the attribute
# doc is a string (like a comment)

# Using @property decorator

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


print("*"*20,"LINE 172","*"*20)
# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

# It will give Value error
# coldest_thing = Celsius(-300)