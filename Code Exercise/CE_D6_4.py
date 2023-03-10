# Create a program that generates multiple text files by iterating over the filenames list.
# The text Hello should be written inside each generated text file.

filenames = ['ce6_1.txt','ce6_2.txt','ce6_3.txt']

for filename in filenames:
	file = open(f"../files/{filename}", 'w')
	file.write('Hello')
	file.close()