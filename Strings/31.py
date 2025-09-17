# Python Program to Find All Odd Palindrome Numbers in a Range without using Recursion

#  Using For-While Loop:
def oddPalindrome(lr, ur):
  odd_palindrome = []
  for num in range(lr, ur+1):
    reverse = 0
    dummy = num
    while dummy > 0:
      rem = dummy % 10
      reverse = reverse*10 + rem
      dummy //= 10
    if reverse == num:
      if(num%2 == 1):
        odd_palindrome.append(num)
  return odd_palindrome

# Using While-While Loop:
def oddPalindrome(lr, ur):
  odd_Palindrome = []
  num = lr
  while(num < ur+1):
    dummy = num
    reverse = 0
    while dummy > 0:
      rem = dummy % 10
      reverse = reverse*10 + rem
      dummy //= 10
    if(reverse == num):
      if(num%2 == 1):
        odd_Palindrome.append(num)
    num += 1
  return odd_Palindrome

lr = int(input('Enter The Lower Range: '))
ur = int(input('Enter The Upper Range: '))
print(oddPalindrome(lr, ur))

