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