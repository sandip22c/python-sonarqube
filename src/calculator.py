# calculator.py

def add(x, y):
    """Adds two numbers together."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers together."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y
