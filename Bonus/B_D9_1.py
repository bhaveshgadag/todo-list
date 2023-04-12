# Create a program, where a user enters password and 
# the program suggests if it is a strong or weak password
# Check conditions for lenght is 8 or more, contains digit
# and contains an uppercase character

password = input("Enter a password: ")

result = {}
	
length = bool(len(password) >= 8)

result["lenght"] = length
	
digit = False
for char in password:
	if char.isdigit():
		digit = True
		break

result["digit"] = digit

uppercase = False
for char in password:
	if char.isupper():
		uppercase = True
		break

result["uppercase"] = uppercase

print(result)

if all(result.values()):
	print("Strong password")
else:
	print("Weak password")