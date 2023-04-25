# Create a script that asks the user to enter a password. 
# Then create a function that checks the strength of the 
# user password. The function should return Strong Password 
# if all of the following conditions are true:
#
# Eight or more characters
# 
# At least one uppercase letter.
#
# At least one digit.

def check_password_strength(password_local):
	result = {}
	
	length = bool(len(password_local) >= 8)
	
	result["lenght"] = length
		
	digit = False
	for char in password_local:
		if char.isdigit():
			digit = True
			break
	
	result["digit"] = digit
	
	uppercase = False
	for char in password_local:
		if char.isupper():
			uppercase = True
			break
	
	result["uppercase"] = uppercase
	
	if all(result.values()):
		return "Strong password"
	
	return "Weak password"
	

password = input("Enter a password : ")

pw_strength = check_password_strength(password)

print(pw_strength)