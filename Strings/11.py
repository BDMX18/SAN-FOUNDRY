# Python Program to Count Number of Lowercase Characters in a String

# Approach 01: 
def lowercase_count(string):
  count = 0
  for char in string:
    if(char.islower()):
      count += 1
  return count

string = input('Enter A String: ')
print('Lowercase Characters Count: ',lowercase_count(string))

# Approach 02:
def lowercase_count(string):
  count = 0
  for char in string:
    if (ord(char) > 96 and ord(char) < 123):
      count += 1
  return count

string = input('Enter A String: ')
print('Lowercase Characters Count: ',lowercase_count(string))

