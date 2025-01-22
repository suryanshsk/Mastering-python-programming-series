import csv

with open("day52.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Fav Coder", "Fav Language"])
    writer.writerow(["Suryanshsk", "Python"])
