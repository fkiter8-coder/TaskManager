""" Take this flat script and refactor it into two functions:
name = input("Task name: ")
if not name:
    print("Name cannot be empty.")
else:
    minutes = int(input("Minutes: "))
    print(f"Task '{name}' will take {minutes} minutes.")
Write a function called get_task_name() that handles the name prompt and validation, and a function called display_task() 
that takes a name and minutes as parameters and prints the summary line. Call both from a main() function."""

def get_task_name():
    name = input("What is the task name? ")
    if name:
        return name
    else:
        print("Name cannot be empty. ")
        return None
def display_task(name, minutes):
    print(f"Task {name} will take {minutes} minutes. ")
def main():
    task_name = get_task_name()
    if task_name:
        minutes = int(input("How many minutes will this take? "))
        display_task(task_name, minutes)
main()