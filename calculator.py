"""
Simple Interactive Calculator in Python
Cloud & DevOps Lab Assignment - Q1
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b

def get_welcome_message() -> str:
    # This function is used to create intentional merge conflicts across branches
    return ">> Minimal Calculator CLI (v2.0 Fast) <<"

if __name__ == "__main__":
    print(get_welcome_message())
    print("Operations: 1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Enter choice (1-4): ")
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(n1, n2)}")
    elif choice == '2':
        print(f"Result: {subtract(n1, n2)}")
    elif choice == '3':
        print(f"Result: {multiply(n1, n2)}")
    elif choice == '4':
        try:
            print(f"Result: {divide(n1, n2)}")
        except ValueError as err:
            print(f"Error: {err}")
    else:
        print("Invalid choice")
