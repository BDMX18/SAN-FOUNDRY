'''
Python Program to Find Prime Numbers in a Given Range
'''

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if(num%div == 0):
        return False
    else:
      return True
  else:
    return False

def primeNumber(lr, ur):
  for num in range(lr, ur+1):
    if(isPrime(num)):
      print(num, end=' ')

# Using while loop:

def primeNumber(lr, ur):
  num = lr
  while num <= ur:
    if(isPrime(num)):
      print(num, end=' ')
    num += 1
  
lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
primeNumber(lr, ur)



