import os
mypath = r'\Documents\Certificates' #change to correct folder path

files = []
for r, d, f in os.walk(mypath):
    for file in f:
        if '.pdf' in file: # you can change this to e.g .txt, to get any text file
            files.append(file.replace('_', ' ').replace('.pdf', '').title())

for f in range(len(files)):
    print(f+1, files[f], sep='. ')