# Python Program to Swap the First and the Last Character of a String

# Approach 01:
def swapString(string):
  new_str = ''
  new_str += string[-1]
  for ip in range(len(string)):
    if ip == 0 or ip == len(string)-1:
      continue
    else:
      new_str += string[ip]
  new_str += string[0]
  return new_str

# Approach 02:
def swapString(string):
  first =  string[-1]
  middle = string[1:-1]
  last = string[0]
  return first+middle+last

string = input('Enter A String: ')
print('Updated String: ', swapString(string))