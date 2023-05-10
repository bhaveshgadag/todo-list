# Create a program that generates a random whole number. 
# Here is how the program should behave:
# Enter the lower bound: 1
# Enter the upper bound: 10
# 7
# The program first asks the user to enter a whole number.
# Then, once the user enters a number, the program asks the user
# again to enter another number.
# Then, the program returns a random number that falls 
# between the two whole numbers.

from random import randint

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random = randint(lower_bound,upper_bound)

print(random)