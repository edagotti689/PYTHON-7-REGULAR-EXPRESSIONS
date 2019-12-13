'''
1. Using compile we can create a  pattern object
2. We can avoid resuing pattern again and again
'''

import re
name = 'SRIram'

p = re.compile('[a-z]{6}',re.I)
v= p.search(name)
print('compile is :',  v.group())
