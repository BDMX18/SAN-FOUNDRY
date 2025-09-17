'''
9.	Simulate Login System
Give the user 3 attempts to enter the correct password. Use a while loop to manage the attempts and lock them out after 3 failures.
'''

userProfile = {'name': 'Bibhu Dutta Mahapatra', 'password': 'a1b2c3d4'}
count = 1
while count <= 3:
  name = input('Enter Your Username: ')
  password = input('Enter Your Password: ') 
  if name == userProfile['name'] and password == userProfile['password']:
    print('Account Found!')
    break
  else:
    print('\t\tTry Again!')
    count += 1
if count > 3:
  print('Attempts Exhausted! Try Again Later')