# Write a program that reads the essay.txt file 
# and returns the number of characters contained in the file.

file = open('../files/essay.txt')
content = file.read()

print(f"Number of characters in essay.txt: {len(content)}")