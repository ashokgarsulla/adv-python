# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# ^a...s$ => The pattern is: any five letter string starting with a and ending with s.

import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	

# Here, we used re.match() function to search pattern within the test_string. The method returns
# a match object if the search is successful. If not, it returns None.

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Specify Pattern Using RegEx
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# To specify regular expressions, metacharacters are used. In the above example, ^ and $ are metacharacters.

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# MetaCharacters
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:
# [] . ^ $ * + ? {} () \ |

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Python RegEx
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Python has a module named re to work with regular expressions. To use it, we need to import the module.
# import re

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# re.findall()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("*"*20,"LINE 40","*"*20) 
import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# re.split()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("*"*20,"LINE 53","*"*20) 

import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']


# split only at first occurence
print("*"*20,"LINE 68","*"*20) 
import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# re.sub()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("*"*20,"LINE 84","*"*20)
# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# re.subn(): The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing
#  the new string and the number of substitutions made.
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Program to remove all whitespaces
import re
print("*"*20,"LINE 111","*"*20)
# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string) 
print(new_string)

# Output: ('abc12de23f456', 4)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# re.search() : If the search is successful, re.search() returns a match object; if not, it returns None.
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("*"*20,"LINE 132","*"*20)

import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Match object
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# match.group() : The group() method returns the part of the string where there is a match.

print("*"*20,"LINE 153","*"*20)

import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# Output: 801 35
