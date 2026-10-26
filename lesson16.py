'''Write a program that creates one task dictionary with a name, priority, and minutes field. Then
 use the standard library to do all three of the following:
Assign the task a random ID between 1000 and 9999 using random
Stamp it with the current date and time as a formatted string using datetime — format: 
YYYY-MM-DD HH:MM
Calculate and print the estimated hours using math.ceil() to round up from minutes
Print the complete task summary at the end.'''

import random
from datetime import datetime
task = {"name": "Homework", "priority": "High", "minutes": 120}
task["ID"] = random.randint(1000, 9999)
task["Created"] = datetime.now()