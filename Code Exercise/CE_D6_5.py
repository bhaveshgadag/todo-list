# Please download the three text files a.txt, b.txt, and c.txt from the resources.
# Then, create a program that reads each text file
# and prints out the content of each in the command line.
# The expected output would be like the following:
#	I am a.
#	I am b.
#	I am c.

filenames = ['a.txt', 'b.txt' ,'c.txt']

for filename in filenames:
	file = open(f"../files/{filename}")
	content = file.read()
	file.close()
	print(content)