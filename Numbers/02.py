def isPrime(num, div=None):
  if div is None:
    div = num-1
  while div >= 2:
    if num%div == 0:
      print('Number Is Not Prime')
      return False
    else:
      return isPrime(num, div-1)
  else:
    print('Number Is Prime')
    return True

num = int(input('Enter A Number: '))
isPrime(num)