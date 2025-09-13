import os

help_text = """
Features:
- Handles +, -, *, /, %, **/^ with correct precedence
- Supports floats and multi-digit numbers
- Parentheses supported: e.g., (2+3)*4
- 'ans' keyword reuses the last result
"""

# Basic Operations
def addition(x, y): return x + y
def subtraction(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y
def modulo(x, y): return x % y
def exponentiation(x, y): return x ** y

ops = {
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "^": exponentiation
}

opchars = "*+/-%^"
last_result = None
version = "v1.3"

# Flat Expression Evaluation
def evaluate_flat_expression(expr: str) -> float:
    numbers = []
    operators = []
    current_number = ""
    i = 0

    while i < len(expr):
        ch = expr[i]

        if ch.isdigit() or ch == ".":
            current_number += ch
        elif ch in opchars:
            # Unary minus
            if ch == "-" and (i == 0 or expr[i-1] in opchars):
                current_number += "-"
            else:
                numbers.append(float(current_number))
                operators.append(ch)
                current_number = ""
        else:
            raise ValueError(f"Invalid character: {ch}")
        i += 1

    numbers.append(float(current_number))

    # Operator precedence evaluation
    for group in ["^", "*/%", "+-"]:
        n = 0
        while n < len(operators):
            if operators[n] in group:
                if operators[n] in "/%" and numbers[n + 1] == 0:
                    raise ZeroDivisionError("Division or modulo by zero!")
                result = ops[operators[n]](numbers[n], numbers[n + 1])
                numbers[n] = result
                numbers.pop(n + 1)
                operators.pop(n)
            else:
                n += 1

    return numbers[0]

# Parentheses Evaluation
def evaluate_expression(expr: str) -> float:
    expr = expr.replace(" ", "")
    if "(" not in expr:
        return evaluate_flat_expression(expr)

    # Evaluate innermost parentheses first
    start = expr.rfind("(")
    end = expr.find(")", start)
    if end == -1:
        raise ValueError("Mismatched parentheses!")

    inner_result = evaluate_expression(expr[start+1:end])
    new_expr = expr[:start] + str(inner_result) + expr[end+1:]
    return evaluate_expression(new_expr)

# Main Input Handler
def inputhandler(string: str):
    global last_result
    try:
        if "h" in string:
            print(help_text)
            return
        elif "q" in string:
            print("\nBye bye!")
            quit()

        # Replace "ans" with last result
        if "ans" in string:
            if last_result is not None:
                string = string.replace("ans", str(last_result))
            else:
                print("No previous answer available.")
                return

        # Replace ** with ^ internally <- goofy method but works so why not lol
        string = string.replace("**", "^")

        # Evaluate the expression
        result = evaluate_expression(string)

        # Pretty display
        display_result = int(result) if result.is_integer() else result
        outputstr = string.replace("^", "**")
        print(f"\n{outputstr} = {display_result}\n")

        last_result = result

    except ValueError as ve:
        print(f"\nError: {ve}\n")
    except ZeroDivisionError as zde:
        print(f"\nError: {zde}\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")

# Main Loop
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\nnonsense {version} - A Simple Python Calculator\n\nh=help\nq=quit\n")
    while True:
        userinput = input(":: ")
        inputhandler(userinput)

main()
