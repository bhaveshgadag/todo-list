# Define a function that has two parameters, year_of_birth and 
# current_year . The current_year parameter should be a 
# default parameter with the current year as a default value.
#
# The function should calculate and return the age of the user 
# given the year of birth and the current year.
#
# Then, below the function definition, get the year of birth from
# the user using an input function and then call and print the 
# defined function to get the user's age as output.
#
# Extend the program by printing a message to the user
# instead of their age if their age is greater than 120.

def calculate_age(year_of_birth,current_year=2023):
	age_local = current_year - year_of_birth
	return age_local


birth_year = int(input("Enter your year of birth : "))

age = calculate_age(birth_year)

if age > 120:
	print(f"Age > 120 : {age}. You are very old.")
else:
	print(f"Age : {age}")