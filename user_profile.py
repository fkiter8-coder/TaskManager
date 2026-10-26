first_name = input("what is your first name? ")
age = int(input("What is your age? "))
height = float(input("What is your height?" ))
language = input("What is your favorite programming language? ")

birth_year = 2026 - age
height_cm = height * 2.54

profile_complete = True

print(f"Hello, my name is {first_name}. I am {age}. My favorite programming language is {language}. I am {height} inches tall, and {height_cm} centimetes tall. I was born in {birth_year}. Profile complete: {profile_complete}. ")


