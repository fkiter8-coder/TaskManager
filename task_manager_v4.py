import csv
import os
import math
import random
from datetime import datetime, timedelta

TASKS_FILE = os.path.join("data","tasks.csv")
FIELDNAMES = ["id", "name", "priority", "minutes", "status","created"]
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def load_tasks():
    try:    
        with open(TASKS_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            tasks = []
            for row in reader:
                try:
                    row["priority"] = int(row["priority"])
                    row["minutes"] = int(row["minutes"])
                    created_str = row["created"].split('.')[0]
                    row["created"] = datetime.strptime(created_str, DATETIME_FORMAT)
                except ValueError:
                    continue 
                tasks.append(row)
            return tasks
    except FileNotFoundError:
        return []
    except PermissionError:
        print("Warning: Could not read task file - permission denied.")
        return[]
    except csv.Error:
        print("Warning: Tasks file is malformed - starting with empty list.")
        return[]

def task_display_age(task):
    delta = datetime.now() - task["created"]
    if delta.days == 0:
        return "Created Today"
    elif delta.days == 1:
        return "Created yesterday"
    else:
        return f"Created {delta.days} days ago"

def task_stats(tasks):
    total_minutes = sum(t["minutes"] for t in tasks)
    print(f" {'Total tasks':<17} : {len(tasks):>4}")
    print(f" {'Total minutes':<17} : {total_minutes:>4}")
    print( f" {'Total hours':<17} : {math.ceil(total_minutes/60):>4}")

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w", newline="") as f:
            temp_tasks = []
            for task in tasks:
                row = dict(task)
                row["created"] = task["created"].strftime(DATETIME_FORMAT)
                temp_tasks.append(row)
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(temp_tasks)
    except PermissionError:
        print("Warning: Could not save tasks - permission denied.")
    except OSError:
        print("Warning: Could not save tasks - disk error.")

def get_valid_index(prompt, max_index):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_index:
                return value
            print(f"Please enter a number between 1 and {max_index}. ")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_task_name(seen_names):
    while True:
        task_name = input("Enter a Valid Task Name: ").strip().capitalize()
        if not task_name:
            print("Task can't be empty. ")
            continue
        if task_name.lower() in seen_names:
            print("Duplicate Task Name")
            continue
        return task_name


def get_valid_priority():
    while True:
        priority_input = input("Enter a Priority (1,2, or 3): ")
        if priority_input == "1":
            return int(priority_input)
        elif priority_input == "2":
            return int(priority_input)
        elif priority_input == "3":
            return int(priority_input)
        print("ERROR: Enter a Valid Priority")

def get_valid_minutes():
    while True:
        minutes_input = input("Enter Number of Minutes: ")
        if minutes_input.isdigit and int(minutes_input) > 0:
            return int(minutes_input)
        print("ERROR: Enter a Valid Number of Minutes")

def get_priority_label(priority):
    if priority == 1:
        return "HIGH"
    elif priority == 2:
        return "MEDIUM"
    else:
        return "LOW"

def get_valid_task(seen_names):
    name = get_valid_task_name(seen_names)
    priority = get_valid_priority()
    minutes = get_valid_minutes()
    return name, priority, minutes

def add_task(tasks, seen_names):
    name, priority, minutes = get_valid_task(seen_names)
    task = {"name": name,
            "priority": priority,
            "minutes": minutes,
            "status": "pending" 
            }
    task["id"] = random.randint(1000,9999)
    task["created"] = datetime.now()
    tasks.append(task)
    seen_names.add(name.lower())
    return True

def display_all_tasks(tasks):
    for i, task in enumerate(tasks,start= 1):
        print(f"Task: {i} ")
        display_task(task)

def display_tasks_by_priority(tasks):
    print("High Priority Tasks. ")
    for task in tasks:
        if task["priority"] == 1:
            display_task(task)
    print("Medium Priority Tasks. ")
    for task in tasks:
        if task["priority"] == 2:
            display_task(task)
    print("Low Priority Tasks. ")
    for task in tasks:
        if task["priority"] == 3:
            display_task(task)

def show_menu(tasks, seen_names):
    while True: 
        print("1. Add Task. ")
        print("2. View Tasks. ")
        print("3. Remove Last Task. ")
        print("4. Task count. ")
        print("5. View Tasks by Priority. ")
        print("6. Search Tasks. ")
        print("7. Select Random Task. ")
        print("8. Task Statistics. ")
        print("9. Quit. ")
        choice = input(" Enter Your Choice: 1 - 9. ")
        if choice == "1":
            add_task(tasks, seen_names)
        elif choice == "2":
            display_all_tasks(tasks)
        elif choice == "3":
            if tasks:
                tasks.pop()
            else:
                print("Nothing to Remove. ")
        elif choice == "4":
            total_tasks = len(tasks)
            total_minutes = 0
            for task in tasks:
                total_minutes = total_minutes + task["minutes"]
            print(f"Total number of tasks is {total_tasks}")
            print(f"Total number of minutes is {total_minutes}")
        elif choice == "5":
            display_tasks_by_priority(tasks)
        elif choice == "6":
            search_tasks(tasks, input("Enter a search query. "))
        elif choice == "7":
            if tasks:
                display_task(random.choice(tasks))
            else:
                print("No Task Found. ")
        elif choice == "8":
            task_stats(tasks)
        elif choice == "9":
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid Choice: Try Again")

def display_task(task):
    print(f" {'ID':<12} {task['id']}")
    print(f" {'Name':<12} {task['name']}")
    print(f" {'Priority':<12} {task['priority']}")
    print(f" {'Minutes':<12} {task['minutes']}")
    print(f" {'Status':<12} {task['status'].upper()}")
    print(f" {'Age':<12} {task_display_age(task)}")

def search_tasks(tasks, query):
    normalized = query.strip().lower()
    results = [t for t in tasks if normalized in t["name"].lower()]
    if not results:
        print("No matching tasks found. ")
    for task in results:
        display_task(task)

def main():
    os.makedirs("data",exist_ok=True)
    tasks = load_tasks()
    seen_names = {task["name"].lower() for task in tasks}
    show_menu(tasks, seen_names)


main()

