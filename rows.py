import os
import csv
import sys

file_name = input("Enter the path of the CSV file: ")
if not os.path.exists(file_name):
    sys.exit("File does not exist")

with open(file_name , 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)