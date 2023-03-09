# Write string in contents list in files in filenames list 
# and store it in files directory

contents = ['This is content for the doc.txt file.', 
'This is content for write multiple files.', 
'This is content for writing files in diffrent directory.']

filenames = ['doc.txt', 'sample.txt', 'presentation.txt']

for content, filename in zip(contents,filenames):
	file = open(f'../files/{filename}', 'w')
	file.write(content)