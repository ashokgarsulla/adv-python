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




