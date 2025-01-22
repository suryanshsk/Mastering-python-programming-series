import csv  #pip install python-csv

with open("data.csv", "r") as file: # At the Place Of data.csv You Have to write your path 
    reader = csv.reader(file)
    for row in reader:
        print(row)
