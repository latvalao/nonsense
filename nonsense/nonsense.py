# nonsense/nonsense.py
import os

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    USE_COLOR = True
except ImportError:
    USE_COLOR = False
    print("Installing the 'Colorama' module is highly recommended\n\n")


def color_text(text, color):
    if USE_COLOR:
        return f"{color}{text}{Style.RESET_ALL}"
    return text


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
version = "v1.4"


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


def inputhandler(string: str, last_result_holder: dict):
    try:
        if "h" in string:
            print(help_text)
            return
        elif "q" in string:
            print("\nBye bye!")
            quit()
        elif "c" in string:
            main()
            return

        # Replace "ans" with last result
        if "ans" in string:
            if last_result_holder["last_result"] is not None:
                string = string.replace("ans", str(last_result_holder["last_result"]))
            else:
                print("No previous answer available.")
                return

        # Replace ** with ^ internally
        string = string.replace("**", "^")

        # Evaluate the expression
        result = evaluate_expression(string)

        # Pretty display
        display_result = int(result) if result.is_integer() else result
        outputstr = string.replace("^", "**")
        outputstr = string.replace(" ", "")
        print(f"\n{color_text(outputstr, Fore.GREEN)} = {color_text(display_result, Fore.GREEN)}\n")

        last_result_holder["last_result"] = result

    except ValueError as ve:
        print(f"\nError: {ve}\n")
    except ZeroDivisionError as zde:
        print(f"\nError: {zde}\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\nnonsense\n\nh=help\nq=quit\nc=clear\n")
    last_result_holder = {"last_result": None}
    while True:
        userinput = input(color_text(":: ", Fore.YELLOW))
        inputhandler(userinput, last_result_holder)


if __name__ == "__main__":
    main()
