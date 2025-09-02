# Python Program to Count the Number of Digits and Letters in a String

def countDigitLetter(string):
  count_digit = 0
  count_letter = 0
  for char in string:
    if(char.isdigit()):
      count_digit += 1
    if(char.isalpha()):
      count_letter += 1
  print(f'Digit Count: {count_digit}, Letter_Count: {count_letter}')

string = input('Enter A String: ')
countDigitLetter(string)