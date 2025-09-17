# Python Program to Find the Sum of All the Items in a Dictionary

my_dict = {}

def createDict(key, value):
  my_dict.update([(key, value)])
  return my_dict

# Function to find sum of values:
def sumValues():
  sum = 0
  for value in my_dict.values():
    if(value.isdigit()):
      sum += int(value)
  return sum

# Function to find product of values:
def productValues():
  product = 1
  for value in my_dict.values():
    if(value.isdigit()):
      product *= int(value)
  return product

print('Enter Operation To Perform: ')
while True:
  choice = int(input('Enter Your Choice (1 to Create Dictionary || 2 to Add Values Of Dictionary || 3 to Product of Values of Dictionary || 4 to Exit): '))
  if(choice == 1):
    while True:
      key = input('Enter The Key (Enter 0 To Exit!): ')
      if key == '0':
        break
      value = input('Enter The Value: ')
      dictVar = createDict(key, value)
    print(dictVar)
  elif(choice == 2):
    sumVal = sumValues()
    print('Sum Of Values In Dictionary:', sumVal)
  elif(choice == 3):
    productVal = productValues()
    print('Product Of Values In Dictionary:', productVal)
  elif(choice == 4):
    print('Thank You!')
    break
  else:
    print('Enter Valid Choice!')

