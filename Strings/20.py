# Python Program that Displays which Letters are in First String but not in Second

def checkLetter(first_str, second_str):
  new_str = ''
  for char in first_str:
    if char not in second_str and char not in new_str:
      new_str += char
  return new_str

first_str = input('Enter First String: ')
second_str = input('Enter Second String: ')
print(checkLetter(first_str, second_str))