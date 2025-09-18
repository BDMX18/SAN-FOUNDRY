'''
Count Zeros in a Number
Given a number, count how many zeros it contains using recursion.
Input: 102030 → Output: 3
'''

# By using Normal Approach:

# num = int(input('Enter A Number: '))
# count = 0
# while num != 0:
#   rem = num % 10
#   num //= 10
#   if rem == 0:
#     count += 1
# print(count)

# Using recursion:
def countZero(num):
  if(num == 0):
    return 0
  if(num % 10 == 0):
    return 1 + countZero(num//10)
  return countZero(num//10)

num = int(input('Enter a number: '))
print(countZero(num))

