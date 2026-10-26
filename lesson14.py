'''Write a program that does the following:
Defines a list of two task dictionaries, each with keys "name", "priority", and "minutes"
Writes that list to a CSV file called tasks.csv using csv.DictWriter, with writeheader() called before the rows
Reads the file back using csv.DictReader and prints each row as a formatted string
Handles the case where the file does not exist on read with a FileNotFoundError message'''

import csv

tasks = [{"name": "Task_1", "priority": "High", "minutes": 60},{"name": "Task_2", "priority": "Low", "minutes": 120}]
FIELDNAMES = ["name", "priority", "minutes"]
with open("tasks.csv", "w", newline ="") as f:
    writer = csv.DictWriter(f, fieldnames= FIELDNAMES)
    writer.writeheader()
    writer.writerows(tasks)

with open("tasks.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} | {row['priority']} | {row['minutes']} min")
        