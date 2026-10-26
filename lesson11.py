'''Write a program that collects five task names from the user using a loop. Use a set to track
 names already entered and skip any duplicate — print a message if a duplicate is detected.
 After the loop, print only the unique task names. Then store the final unique list as a tuple and 
print it with a message confirming it is now locked.'''

seen_tasks = set()
unique_tasks = []

for i in range(5):
    task = input(f"What is task {i+1}. ")
    if task in seen_tasks:
        print("Duplicate is detected. ")
    else:
        seen_tasks.add(task) 
        unique_tasks.append(task)

print(unique_tasks)
locked_tasks = tuple(unique_tasks)

print(type(locked_tasks))