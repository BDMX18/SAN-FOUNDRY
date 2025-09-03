# Python Program to Find the Larger String without using Built-in Functions

def largerString(str1, str2):
  str1_count = 0
  str2_count = 0
  for ch1 in str1:
    str1_count += 1
  for ch2 in str2:
    str2_count += 1
  if(str2_count > str1_count):
    print(f'{str2} is the larger string')
  elif(str1_count > str2_count):
    print(f'{str1} is the larger string')
  else:
    print('Both Strings Are Of Same Size!')

str1 = input('Enter First String: ')
str2 = input('Enter Second String: ')
largerString(str1, str2)