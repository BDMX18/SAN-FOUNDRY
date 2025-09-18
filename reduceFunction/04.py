'''
1. Group and count occurrences of elements in a list using reduce()

Count how many times each element appears in a list and return a dictionary.

Sample data:

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
'''

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

from functools import reduce

def countItem(item_dict, item):
  if item in item_dict:
    item_dict[item] += 1
  else:
    item_dict[item] = 1
  return item_dict

result = reduce(countItem, items, {})
print(result)