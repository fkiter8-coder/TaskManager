def get_valid_task_name():
    while True:
        task_name = input("Enter a Valid Task Name: ").strip()
        if task_name:
            return task_name
        else:
            print("ERROR: Enter a Valid Task Name") 
   
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
    
def display_task_summary(name, priority, minutes):
    label = get_priority_label(priority)
    hours = minutes/60
    print(f"The task name is {name}. ")
    print(f"The task priority is {label}. ")
    print(f"The task will take {minutes} minutes, which is {hours} hours. ")

def get_valid_task():
    name = get_valid_task_name()
    priority = get_valid_priority()
    minutes = get_valid_minutes()
    return name, priority, minutes

def add_task(tasks):
    name, priority, minutes = get_valid_task()
    tasks.append((name, priority, minutes))

def display_all_tasks(tasks):
    for i, task in enumerate(tasks,start= 1):
        print(f"Task: {i} ")
        display_task_summary(task[0], task[1], task[2])

def display_tasks_by_priority(tasks):
    print("High Priority Tasks. ")
    for task in tasks:
        if task[1] == 1:
            display_task_summary(task[0], task[1], task[2])
    print("Medium Priority Tasks. ")
    for task in tasks:
        if task[1] == 2:
            display_task_summary(task[0], task[1], task[2])
    print("Low Priority Tasks. ")
    for task in tasks:
        if task[1] == 3:
            display_task_summary(task[0], task[1], task[2])

def show_menu(tasks):
    while True: 
        print("1. Add Task. ")
        print("2. View Tasks. ")
        print("3. Remove Last Task. ")
        print("4. Task count. ")
        print("5. View Tasks by Priority. ")
        print("6. Quit. ")
        choice = input(" Enter Your Choice: 1 - 6. ")
        if choice == "1":
            add_task(tasks)
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
                total_minutes = total_minutes + task[2]
            print(f"Total number of tasks is {total_tasks}")
            print(f"Total number of minutes is {total_minutes}")
        elif choice == "5":
            display_tasks_by_priority(tasks)
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid Choice: Try Again")

def main():
    tasks = []
    show_menu(tasks)


main()

        
         