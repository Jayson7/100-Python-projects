first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# choose an operation
print(
    '''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    '''
)

# multiplication
def multiply(first_number, second_number):
    return first_number * second_number

# addition

def add(first_number, second_number):
    return first_number + second_number

# subtraction

def subtract(first_number, second_number):
    return first_number - second_number

# division

def divide(first_number, second_number):
    return first_number / second_number
 
# exit program
def exit():
    print("Goodbye!")
    

operation = int(input("Enter operation: "))

if operation == 1:
    print(add(first_number, second_number))
elif operation == 2:
    print(subtract(first_number, second_number))
elif operation == 3:
    print(multiply(first_number, second_number))
elif operation == 4:
    print(divide(first_number, second_number))
elif operation == 5:
    exit()
else:
    print("Invalid operation")
    exit()