'''Write a program that collects a task name, priority, and estimated minutes from the user. 
Store all three fields in a dictionary. Then:
Print each key-value pair using .items() in a loop
Add a "status" key set to "pending" after the dictionary is created
Print the status using .get() with a default value of "unknown"'''

task_name = input("What is the task name? ")
task_priority = input("What is the priority? ")
estimated_minutes = input("How long will the task take? ")

task = {}
task["name"] = task_name
task["priority"] = task_priority
task["minutes"] = estimated_minutes

for key, value in task.items():
    print(f"{key}: {value}")

task["status"] = "pending" 

print(f"status: {task.get("status", "unknown")}")