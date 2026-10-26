'''Write a function called get_valid_minutes() that asks the user to enter a number of minutes. It must handle two error cases:
The user enters something that is not a number — catch the ValueError and retry
The user enters zero or a negative number — print a message and retry
The function should keep looping until it gets a valid positive integer, then return it. Call it from main() and print the result.'''

def get_valid_minutes():
    while True:
        try:
            minutes_input = int(input("Enter number of minutes: "))
            if minutes_input <= 0:
                print("Enter a number of minutes greater than zero")
            else:
                return minutes_input    
        except ValueError:
            print("Enter an integer greater than zero")

def main():
    minutes = get_valid_minutes()
    print(f"The task will take {minutes} minutes. ")

main()
        
            

    

