# Python Program to Find the Length of a String without Library Function

def stringLength(string):
  count = 0
  for char in string:
    count += 1
  return count

string = input('Enter A String: ')
print('String Length: ', stringLength(string))