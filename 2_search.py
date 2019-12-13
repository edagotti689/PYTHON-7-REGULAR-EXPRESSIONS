'''
1. Search is used to find a pattern anywhere in the string 
'''
import re


name = 'sriram'
mo = re.search('ram', name)
print(mo.group())


# matching space through \s pattern
name = 'sri ram'
mo = re.search('\w\w\w\s\w\w\w', name)
print(mo.group())