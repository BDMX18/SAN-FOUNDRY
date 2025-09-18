def isEvenOdd(num):
  if num < 2:
    return (num % 2 == 0)
  else:
    return isEvenOdd(num - 2)
num = int(input('Enter A Number: '))
if (isEvenOdd(num)):
  print('Even Number')
else:
  print('Odd Number')

