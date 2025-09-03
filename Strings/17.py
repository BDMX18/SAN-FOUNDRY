# Python Program to Check if the Substring is Present in the Given String

def subStringCheck(string, sub_string):
  length = len(sub_string)
  count = 0
  if length == 0:
    print(f'The {sub_string} is available in {string} for 0 times!')
  else:
    for ip in range(len(string)):
      if(string[ip:ip+length]  == sub_string):
        count += 1
  print(f'The {sub_string} is available in {string} for {count} times!')

string = input('Enter A String: ')
sub_string = input('Enter The Sub-String To Check: ')
subStringCheck(string, sub_string)

