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