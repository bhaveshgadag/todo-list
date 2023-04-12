# Write a program that asks users to enter a password. 
# Then, it checks if the password length is greater than 7 
# and returns "Great password there!".
# If the password has 7 or fewer characters, the program 
# returns, "Your password is weak".

password = input('Enter a password: ')

if len(password) > 7:
	print('Great password there!')
else:
	print('Your password is weak')