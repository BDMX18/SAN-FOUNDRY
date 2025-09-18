'''
Question 1: Filter Prime Numbers from a List
Task: Given a list of integers, use filter() to return only the prime numbers.
Sample Data:
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''

def primeNumber(num):
  if num > 1:
    for div in range(2, num//2+1):
      if num % div == 0:
        return False
    else:
      return True
  else:
    return False
  
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(filter(primeNumber, nums)))