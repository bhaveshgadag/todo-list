# Write a program that gets a list of names from the user and 
# returns the number of names given. 
# Here is how the program would work:
# Enter names separated by commas (no spaces): john,jay,marry
# 3

def names_str_to_list(names_str):
	names_list_local = names_str.split(',')
	return names_list_local

names = input("Enter names separated by commas (no spaces): ")

names_list = names_str_to_list(names)

print(len(names_list))