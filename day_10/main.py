# Day 10 project
# This is the code to implement a simple calculator
from art import logo
from functions import operations
def calculator():
    should_accumulate = True
    print(logo)
    n1 = float(input("What's the first number?: "))
    while should_accumulate:
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, "
                                f"or type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            n1 = result
        else:
            should_accumulate = False
            print('\n' * 100)
            calculator()
calculator()

