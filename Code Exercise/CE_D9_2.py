# Extend the program we built in Coding Exercise 1 by adding a new feature.
# The new feature should allow the program to return
#  "Password is OK, but not too strong" when the password 
# is exactly seven characters long.

password = input('Enter a password: ')

if len(password) > 7:
	print('Great password there!')
elif len(password) == 7:
	print('Password is OK, but not too strong')
else:
	print('Your password is weak')