'''
Reverse Digits
Take an integer input from the user and use a while loop to reverse its digits. Example: 1234 → 4321.
'''

num = int(input('Enter A Number: '))
reverse = 0
while num != 0:
  rem = num % 10
  reverse = (reverse*10)+rem
  num//=10
print(reverse)