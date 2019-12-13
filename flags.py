'''
1. The flags modifies the meaning of the given regex pattern.

'''
import re

# re.M or re.MULTILINE to match ^ and $ every line
# name = 'sriram123\n999kumar'
# mo = re.search('^\d\d\d', name, re.M)
# print(mo.group())


# re.I or re.IGNORECASE to match Case sensitive values
# name = 'SRIram'
# mo = re.search('sriram', name, re.I)
# print(mo.group())


# re.S or re.DOTALL Makes a period (dot) match any character
name = 'SRI\nram'
mo = re.search('sri.ram', name, re.I + re.S)
print(mo.group())

