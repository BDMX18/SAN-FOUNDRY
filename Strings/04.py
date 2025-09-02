# Python Program to Replace All Occurrences of ‘a’ with $ in a String

# Approach 01: Herein, I've defined a function which will iterate through each and every character of the string and will try to check whether it matches with the character that the user wants to replace. If it matches then it'll replace it with '$'. If it doesn't matches then it'll simply add it to new_string.

def replace(string, replace_char):
  new_string = ''
  for char in string:
    if(char == replace_char):
      new_string += '$'
    else:
      new_string += char
  return new_string

string = input('Enter A String: ')
replace_char = input('Enter The Character You Want To Replace with \'$\': ')
print(replace(string, replace_char))

# Approach 02: By using built-in method, replace().

string = input('Enter A String: ')
replace_char = input('Enter The Character You Want To Replace With \'$\': ')
new_string = string.replace(replace_char, '$')
print(new_string)