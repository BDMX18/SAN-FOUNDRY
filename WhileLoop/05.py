'''
5.	Print Digits in Words
Take an integer and print each digit in words (e.g., 123 → "One Two Three"), using a while loop.
'''

num = int(input('Enter A Number: '))
digit_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'}
num_in_words = ''
while num != 0:
  rem = num % 10
  num_in_words = digit_dict[rem] +' '+ num_in_words
  num //= 10
print(num_in_words)