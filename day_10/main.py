# Day 10 project
# This is the code to implement a simple calculator
from art import logo
from functions import operations
def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, otherwise type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n"*100)
            calculator()
calculator()

