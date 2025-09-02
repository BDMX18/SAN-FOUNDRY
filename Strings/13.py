# Python Program to Count Number of Uppercase and Lowercase Letters in a String

def upperLowerCount(string):
  upper_count = 0
  lower_count = 0
  for char in string:
    if(char.islower()):
      lower_count += 1
    if(char.isupper()):
      upper_count += 1
  print(f'Uppercase Count: {upper_count}, Lowercase Count: {lower_count}')

string = input('Enter A String: ')
upperLowerCount(string)