'''
1. Match is used to find a pattern from starting position
'''
import re

name = 'sriram'
mo = re.match('sri', name)
print(mo.group())

# matching through \w pattern
name = 'sriram'
mo = re.match('\w\w\w', name)
print(mo.group())

# matching numbers through \d pattern
name = 'sriram123'
mo = re.match('\d\d\d', name)
print(mo.group())


'''
Error:1

  File "1_match.py", line 18, in <module>
    print(mo.group())
AttributeError: 'NoneType' object has no attribute 'group'

'''