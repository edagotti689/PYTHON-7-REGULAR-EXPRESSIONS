'''
1. used to replace substrings based on pattren and return replaced string
'''

import re

# To replace a number with $
name = '5A9BC 123'
v = re.sub('\d', '$', name)
print(' After replace :', v)

# To remove all numbers
name = '6AB9C 123'
v = re.sub('\d', '', name)
print(' After removing numbers  :', v)


# To replace only first occurrences
name = '6AB9C 123'
v = re.sub('\d', '@', name, 1)
print(' After removing numbers  :', v)