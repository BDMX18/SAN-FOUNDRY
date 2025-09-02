# Python Program to Count the Number of Words and Characters in a String

def countString(string):
  word_count = 0
  char_count = 0
  str_list = string.split()
  for word in str_list:
    word_count += 1
  for char in string:
    char_count += 1
  print(f'Word Count: {word_count}, Character Count: {char_count}')

string = input('Enter A String: ')
countString(string)