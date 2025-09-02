# The program takes a string and removes the characters of odd index values in the string.

def odd_index(string):
  new_string=''
  for ip in range(len(string)):
    if(ip%2==1):
      new_string += string[ip]
  return new_string


string = input('Enter A String: ')
odd_string = odd_index(string)
print(odd_string)