# user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out the sum of the numbers.
# The output of your code should be as below:
#	49.1

user_entries = ['10', '19.1', '20']

user_entries = [float(item) for item in user_entries]

print(sum(user_entries))