'''Write a program that starts with an empty list called tasks. 
Use a for loop with range(3) to collect three task names and append each to the list. 
Then: 
Print the total number of tasks using len()
Print the first and last task by index
Print all tasks in reverse order using slicing '''

tasks = []
for i in range(3): 
    task_name = input(f"What is the name of task {i+1}. ")
    tasks.append(task_name)
print(len(tasks))
print(tasks[0])
print(tasks[-1])
print(tasks[::-1])
