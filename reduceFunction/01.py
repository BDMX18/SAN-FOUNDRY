'''
1. Sum of all elements in a list using reduce(
Sample data:
numbers = [3, 7, 2, 9, 4]
'''

numbers = [3, 7, 2, 9, 4]
from functools import reduce as r
print(r(lambda a,b: a+b, numbers))