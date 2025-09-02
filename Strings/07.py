# Python Program to Reverse a String Without using Recursion

# Approach 01: 
def reverseString(string):
  new_string = ''
  for ip in range(-1, -(len(string)+1), -1):
    new_string += string[ip]
  return new_string

string = input('Enter A String: ')
print('Reverse String: ', reverseString(string))

# Approach 02:
string = input('Enter A String: ')
print('Reverse String: ', string[::-1])