# task_input_v2.py
# Collects a validated task from the user using while True / break retry loops.
# Replaces the guard clause pattern from task_input.py (Lesson 5)
# with loops that retry on invalid input instead of stopping.

# --- Field 1: Task name ---
while True:
 task_name = input("Enter task name: ").strip()
 if task_name:
  break
 else:
  print("ERROR: Please input a task name. ")

# --- Field 2: Priority ---
while True:
 priority_input = input("Enter priority (1, 2, or 3): ")
 if priority_input == "1":
        break
 elif priority_input == "2":
        break
 elif priority_input == "3":
        break
 print("Error")
print(priority_input)

# --- Field 3: Estimated minutes ---
while True:
 minutes_input = input("Enter estimated minutes: ")
 break

print(f"I am doing the task {task_name}. It has a priority of {priority_input}. It will take {minutes_input} minutes. ")