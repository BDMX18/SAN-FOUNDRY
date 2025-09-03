# Python Program to Create a New String Made up of First and Last 2 Characters

def newString(string):
  if len(string) == 0:
    print('Enter A String!')
  elif len(string) < 4:
    print('String Length Should Be Atleast 4!')
  elif len(string) == 4:
    print(string)
  else:
    print(string[:2]+string[-2:])

string = input('Enter A String: ')
newString(string)