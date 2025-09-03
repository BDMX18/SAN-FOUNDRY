# Python Program that Displays Letters that are not Common in Two Strings

def letter(str1, str2):
  new_str = ''
  for ch1 in str1:
    if ch1 not in str2 and ch1 not in new_str:
      new_str += ch1
  for ch2 in str2:
    if ch2 not in str1 and ch2 not in new_str:
      new_str += ch2
  return new_str

str1 = input('Enter First String: ')
str2 = input('Enter Second String: ')
print(letter(str1, str2))