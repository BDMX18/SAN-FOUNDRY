from random import randint as ri
a = ri(1, 100)
while True:
  num = int(input('Enter A Number: '))
  if num != a:
    if num < a:
      print('Too Low')
    else:
      print('Too High')
  else:
    print('Your Guess Is Correct!')
    break