import os
import csv
import sys
import pandas as pd

file_name = input("Enter the path of the CSV file: ")
if not os.path.exists(file_name):
    sys.exit("File does not exist")

column = input("Enter the column name: ")
df = pd.read_csv(file_name)

try:
    print(df[column])
except KeyError:
    print("Column not found!")