import csv

dictionary = input("Enter dictionary in the format 'key value key value': ").split()
if len(dictionary) % 2 !=0:
	dictionary = dictionary[:-1]

dictionary = {dictionary[x]:dictionary[x+1] for x in range (0, len(dictionary), 2)}

with open('dictionary.csv', 'w') as f:  
    writer = csv.writer(f)
    for key, value in dictionary.items():
       writer.writerow([key, value])

with open('dictionary.csv' , 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        print(",".join(row))