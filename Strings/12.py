# Python Program to Count the Number of Vowels in a String

def vowelCount(string):
  count = 0
  for char in string:
    if char in 'aeiou': 
      count += 1
  return count

string = input('Enter A String: ')
print('Vowel Count: ', vowelCount(string))