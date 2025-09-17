# Python Program to Remove a Key from a Dictionary

my_dict = {}

def removeKey(key):
  if key in my_dict:
    dict.pop(key)
  else:
    print('Key Not Available In Dictionary!')
  return my_dict

def createDict(key, value):
  my_dict.update([(key, value)])
  return my_dict

while True:
  choice = int(input('Enter 1 to Create, Enter 2 to Remove, Enter 3 to Exit: '))
  if(choice == 1):
    while True:
      key = input('Enter Key: ')
      if key == '0':
        break
      value = input('Enter Value: ')
      create = createDict(key, value)
    print(create)
  elif(choice == 2):
    while True:
      key = input('Enter Key To Delete: ')
      if(key == '0'):
        break
      remove = removeKey(key)
    print('Dictionary After Deletion: ', remove)
  elif(choice == 3):
    print('Thank You!')
    break
  else:
    print('Enter Valid Choice!')