# Build a percentage calculator that gets from the user 
# the "total value" and the "value" and returns the
# percentage as shown below:
# Enter total value: 50
# Enter value: 20
# That is 40.0%
#
# The program should also print a message 
# if the user doesn't enter a number for the 
# "total value or for the "value":
# Enter total value: 20
# Enter value: hi
# You need to enter a number. Run the program again.
#
# Exercise 2 - extend the program you created in Exercise 1 by 
# displaying a message to the user when they enter 0 for the "total value".

try:
	total = float(input("Enter total value:"))
	value = float(input("Enter value:"))
	
	percent = (value / total) * 100
	
	print(f"That is {percent}%")

except ValueError:
	print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
	print("Your total value cannot be zero")