'''
3. Find the maximum element in a list using reduce()
Sample data:
numbers = [23, 89, 12, 56, 4]
'''

from functools import reduce as r
numbers = [23, 89, 12, 56, 4]
print(r(lambda a,b: a if a > b else b, numbers))
