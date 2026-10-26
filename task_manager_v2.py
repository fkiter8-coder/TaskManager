# task_manager_v2.py
# Composite function upgrade of task_manager_v1.py.
# get_valid_task() calls the three collection functions
# and returns all values as a tuple for the caller to unpack.
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

# Copy your working version from task_manager_v1.py
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
"""Call the three collection functions and return all values as a tuple."""
# Call get_valid_task_name(), get_valid_priority(), get_valid_minutes()
# Return all three values as a tuple: return name, priority, minutes
# --- Main program ---
# Should be exactly two lines:
# one unpacking call to get_valid_task(), one call to display_task_summary().
if __name__ == "__main__":
    name, priority, minutes = get_valid_task()
    display_task_summary(name, priority, minutes)
