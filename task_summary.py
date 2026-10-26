first_name = input("What is your name? ")
task_name = input("What is that task name? ")

if task_name:
    task_priority = int(input("Enter a task priority: (1,2,3) "))
    est_time = int(input("How many minutes will the task take? "))
    est_hours = float(est_time/60)
    if task_priority == 1:
       print("'*** HIGH PRIORITY — Act immediately ***")
    if est_time > 120:
       print("Note: This is a long task — consider breaking it into smaller steps")

    print(f"My name is {first_name}. Today I am working on {task_name}. I think that the task priority is {task_priority}. I think it will take me {est_time} minutes, which is {est_hours} hours. ")

else:
  print("Warning: No task name provided. ")