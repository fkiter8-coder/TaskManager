# task_manager_v1.py
# Function-based refactor of task_input_v2.py.
# Each validated input field becomes its own function.
# The main program calls each function in sequence.
def get_valid_task_name():
    while True:
        task_name = input("Enter task name: ").strip()
        if task_name:
            return task_name
        else:
            print("ERROR: Please input a task name. ")



def get_valid_priority():
    """Collect and return a valid integer priority (1, 2, or 3)."""
    while True:
      priority_input = input("Enter priority (1, 2, or 3): ")
      if priority_input == "1":
          return int(priority_input)
      elif priority_input == "2":
          return int(priority_input)
      elif priority_input == "3":
          return int(priority_input)
      print("Error")

def get_valid_minutes():
    """Collect and return a valid positive integer of minutes."""
    while True:
        minutes_input = input("Enter estimated minutes: ")
        if minutes_input.isdigit() and int(minutes_input) > 0:
           return int(minutes_input)
        print("Error")

def get_priority_label(priority):
    """Take an integer priority, return the label string HIGH, MEDIUM, or LOW."""
    if priority == 1:
       return "HIGH"
    elif priority == 2:
       return "MEDIUM"
    else:
       return "LOW"

def display_task_summary(name, priority, minutes):
    """Print a formatted task summary using the three collected values."""
    label = get_priority_label(priority)
    hour = minutes/60
    print(f"Task is: {name}. ")
    print(f"The priority is {label}. ")
    print(f"This will take {minutes} mins, or {hour} hours. ")
 

# --- Main program ---
# Should be exactly four lines:
# one call to get_valid_task_name(), one to get_valid_priority(),
# one to get_valid_minutes(), one to display_task_summary().
if __name__ == "__main__":
    name = get_valid_task_name()
    priority = get_valid_priority()
    minutes = get_valid_minutes()
    display_task_summary(name, priority, minutes)
    