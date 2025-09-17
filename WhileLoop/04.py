'''
4.	Check for Palindrome Number
Use a while loop to check whether a number is a palindrome (e.g., 121, 1331).
'''

num = int(input('Enter A Number: '))
reverse = 0
dummy = num
while dummy != 0:
  rem = dummy % 10
  reverse = (reverse*10) + rem
  dummy //= 10
if reverse == num:
  print('Palindrome Number')
else:
  print('Not Palindrome Number')