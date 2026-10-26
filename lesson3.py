task_name = input("Enter a task name. ")
est_min = int(input("Enter estimated minutes. "))
urgent_input = input("Urgent? Yes or no? ")
is_urgent = urgent_input.lower() == "yes"
print(f"You are working on {task_name}. This will probably take you {est_min} minutes. Is this urgent? {is_urgent} ")