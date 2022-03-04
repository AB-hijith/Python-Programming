import os
import sys

read_file = input("Enter the file to copy lines from: ")
if not os.path.exists(read_file):
    sys.exit("File does not exist")

out_file = input("Enter the name of file to copy odd lines to: ")
out_file = open(out_file, 'a')

with open(read_file, 'r') as f:
    lines = f.readlines()
    c = 1
    for line in lines:
        if c % 2 !=0:
            out_file.write(line)
        c += 1

out_file.close()