first_name = input("What is your first name? ")
age = int(input("What is your age? "))
program_language = input("What is your favorite programming language? ")
height = float(input("What is your height?"))
birth_year = 2026 - age
height_cm = height * 2.54
profile_complete = True

print(f"My first name is {first_name}.")
print(f" I am {age} years old, and I was born in {birth_year}.")
print(f" My height is {height_cm} centimeters.")
print(f"My favorite programming language is {program_language}.")
print(f"Profile Complete: {profile_complete}")

