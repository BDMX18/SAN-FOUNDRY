# Python Program to Replace Every Blank Space with Hyphen in a String

# Approach 01:

# def replace_blank(string):
#   new_string = ''
#   for char in string:
#     if(char == ' '):
#       new_string += '-'
#     else:
#       new_string += char
#   return new_string

# string = input('Enter A String: ')
# print(replace_blank(string))

# Approach 02:

string = input('Enter A String: ')
new_string = string.replace(' ', '-')
print(new_string)