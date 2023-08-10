from art import logo


def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Return the difference between two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Return the quotient of two numbers."""
    if n2 == 0:  # To avoid ZeroDivisionError
        return "Undefined (division by zero)"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator(n1, n2, operation):
    """Perform a mathematical operation on two numbers."""
    return operations[operation](n1, n2)


def calc():
    """Run the main calculator functionality."""
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        result = calculator(num1, num2, operation_symbol)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if user_input == "y":
            num1 = result
        else:
            continue_calculation = False
            calc()


# The main execution of the calculator
calc()
