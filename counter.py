import os
import sys

file_name = input("Enter the path of the file to read words from: ")
if not os.path.exists(file_name):
    sys.exit("File does not exist")

counter = dict()

f = open(file_name, "r")
lines = f.readlines()
for line in lines:
    words = line.split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

print(counter)
f.close()