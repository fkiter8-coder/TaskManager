task_name = input("What is the task name? ")
est_min = int(input("What are the estimated minutes? "))
break_time = int(input("What is the break time? "))
urgent_input = input("is it urgent? (yes/no) ")
total_time = est_min + break_time
fits_in_hour = total_time <= 60 
is_urgent = urgent_input == "yes" 
high_priority = total_time > 20 and is_urgent
