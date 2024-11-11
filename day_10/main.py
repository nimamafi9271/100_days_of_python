# Day 10 project
# This is the code to implement a simple calculator
from art import logo
from functions import operations
while True:
    print(logo)
    restart = False
    n1 = float(input("What's the first number?: "))
    while not restart:
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        should_continue = input(f"Type 'y' to continue calculating with {result}, "
                                f"or type 'n' to start a new calculation: ").lower()
        if should_continue == 'n':
            restart = True
            print('\n'*100)
        elif should_continue == 'y':
            n1 = result
