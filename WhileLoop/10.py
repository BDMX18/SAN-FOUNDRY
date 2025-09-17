num = int(input('Enter A Number: '))
count_dummy = num
dummy = num
sum = 0
count = 0
while count_dummy != 0:
  count_dummy //= 10
  count += 1
while dummy != 0:
  rem = dummy % 10
  dummy //= 10
  sum += rem**count
if sum == num:
  print('Armstrong Number!')
else:
  print('Not Armstrong Number!')