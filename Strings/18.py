# Python Program to Find Common Characters in Two Strings

'''
At first I implemented Approach 1, but with this approach there's an issue:
  Duplicate characters: If a character appears more than once in the first string and also exists in the second string, it will be counted multiple times.
'''

# Approach 01:
def commonCharacter(f_string, s_string):
  common = ''
  for f_char in f_string:
      if(f_char in s_string):
        common += f_char+', '
  print(f'These are the common characters {common}')

# Approach 02:
def commonCharacter(f_string, s_string):
  f_set = set()
  common = ''
  for char in f_string:
     f_set.add(char)
  for char in f_set:
     if(char in s_string):
        common += char + ', '
  print(f'These are the common characters {common}')

# Approach 03:
def commonCharacter(f_string, s_string):
   f_set = set(f_string)
   s_set = set(s_string)
   intersection = f_set.intersection(s_set)
   print('Common Characters: ', intersection)

f_string = input('Enter First String: ')
s_string = input('Enter Second String: ')
commonCharacter(f_string, s_string)


