tasks = []
for i in range(3):
    each_task = input(f"Enter task {i+1}")
    tasks.append(each_task)
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
    