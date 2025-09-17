'''
Sum Until Zero
Continuously accept numbers from the user and add them to a total. Stop when the user enters 0, then print the total sum.
'''

total = 0
while True:
  num = int(input('Enter A Number: '))
  if num != 0:
    total += num
  else:
    break
print('Total is:', total)