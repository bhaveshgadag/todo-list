# Replace dot after Sr no. with a dash

filenames = ['1.Raw file.txt','2.Reports.txt','3.Presentations.txt']

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)