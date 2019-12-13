'''
1. To find all matching pattrens in a string
2. It will return all matching values in list format
'''
import re

s = '888ijk89ijdh564ij675'

v = re.findall('\d{3}', s)
print(v)
