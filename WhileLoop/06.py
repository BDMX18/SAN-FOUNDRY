'''
6.	Count Digit Frequency
Input a number and count the frequency of each digit using a while loop. Example: 112233 → 1:2, 2:2, 3:2.
'''

num = int(input('Enter A Number: '))
freq_dict = {}
while num != 0:
  count = 0
  rem = num % 10
  if rem not in freq_dict:
    count += 1
    freq_dict[rem] = count
  else:
    freq_dict[rem] +=1
  num //= 10
print(freq_dict)
