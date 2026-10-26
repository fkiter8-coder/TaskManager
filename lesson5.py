task_name = input("What is the task name? ")
if task_name:
    priority = input("Enter a priority: (High, Medium, Low) ")
    if priority == "High":
        print("Do Immediately")
    elif priority == "Medium":
        print("Schedule for today")
    elif priority == "Low":
        print("Goes in backlog")
    else:
        print("Error")
else: 
    print("Error")
