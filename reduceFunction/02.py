'''
. Find the product of all elements in a list using reduce()

Sample data:

numbers = [1, 4, 6, 2]
'''

from functools import reduce as r
numbers = [1, 4, 6, 2]
print(r(lambda a,b: a*b, numbers))