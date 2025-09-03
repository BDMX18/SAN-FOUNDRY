# Python Program to Print All Letters Present in Both Strings

def combineString(str1, str2):
  new_str = ''
  for char in str1:
    if char in str2 and char not in new_str:
      new_str += char
  print(new_str)

str1 = input('Enter First String: ')
str2 = input('Enter Second String: ')
combineString(str1, str2)