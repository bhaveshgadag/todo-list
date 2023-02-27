# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
#
# 3. Prints out the amount in euros,

dollars = int(input("How many dollars have you got? "))
euros = dollars * 0.95
print("The amount in euros is:")
print(euros)