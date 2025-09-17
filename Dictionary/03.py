# Python Program to Add a Key-Value Pair to the Dictionary

dict = {}

def addPair(key, value):
  dict[key] = value
  return dict

while True:
  key = input('Enter The Key (0 to Exit): ')
  if(key == '0'):
    break
  value = input('Enter The Value: ')
  print(addPair(key, value))