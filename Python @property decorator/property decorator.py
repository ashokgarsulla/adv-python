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









