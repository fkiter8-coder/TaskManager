'''Write a function called get_task() that collects a task name and estimated minutes from the 
user, validates both (name not empty, minutes greater than zero), and returns both values 
together in a single return statement. In main(), call get_task(), unpack the two return 
values into named variables, and print them.'''

def get_task():
    task_name = input("What is the task name? ")
    if not task_name:
        task_name = "unnamed_task"
    task_minutes = int(input("How many minutes will this take? "))
    if task_minutes <= 0:
        task_minutes = 1 
    return task_name, task_minutes

def main():
   name, minutes = get_task()
   print(f"This task is called {name}. It will take {minutes} minutes.")

main()

