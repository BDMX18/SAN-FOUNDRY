# Python Program to Remove the nth Index Character from a Non-Empty String

def remove_char(string, n):
  new_string = ''
  if(len(string) <= 0):
    print('Enter A Valid String')
  else:
    for ip in range(len(string)):
      if(ip != n):
        new_string += string[ip]
      else:
        continue
  print(new_string)

string = input('Enter A String: ')
n = int(input('Enter The Index Position Of The Character You Want To Remove: '))
remove_char(string, n)