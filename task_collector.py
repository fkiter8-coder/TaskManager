# task_collector.py
# Collects multiple tasks from the user using a for loop.
# Validates each task name and priority before accepting it.
# Tracks valid and skipped tasks using accumulators.
num_tasks = int(input("How many tasks do you want to enter? "))
tasks_entered = 0 # accumulator: count of valid tasks accepted
tasks_skipped = 0 # accumulator: count of invalid tasks rejected
for i in range(num_tasks):
 print(f"\nTask {i + 1} of {num_tasks}")
 task_name = input(" Task name: ")
 # --- Validation ---
if task_name:
 priority = input(" Priority (1, 2, or 3): ")
 if priority == "1":
  print("High Priority")
 if priority == "2":
  print("Medium Priority")
 if priority == "3":
  print("Low Priority")
else:
 print("Error: Enter a Valid Priority")
 # Add your validation logic here.
 # If task_name is empty: print an error, increment tasks_skipped, continue
 # If priority is not "1", "2", or "3": print an error, increment tasks_skipped,continue
 # If both are valid: increment tasks_entered
# --- Summary ---
# After the loop, display:
# Total tasks requested, tasks successfully entered, tasks skipped.