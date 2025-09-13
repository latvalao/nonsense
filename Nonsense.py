import os

help_text = """
Features:
- Handles +, -, *, /, % with correct precedence
- Supports floats and multi-digit numbers
- 'ans' keyword reuses the last result
"""


def addition(x, y):
	# Return the addition of x and y
	return x+y
	
def subtraction(x, y):
	# Return the subtraction of x and y
	return x-y

def multiply(x, y):
	# Return the multiplication of x and y
	return x*y
	
def divide(x, y):
	# Return the division of x and y
	return x/y
	
def modulo(x,y):
	# Return the modulo of x and y
	return x%y



def inputhandler(string: str):
    global last_result
    try:
        if "h" in string:
            print(help_text)
            return

        elif "q" in string:
            print("\nBye bye!")
            quit()

        # Replace "ans" with last result, if available
        if "ans" in string:
            if last_result is not None:
                string = string.replace("ans", str(last_result))
            else:
                print("No previous answer available.")
                return

        # Parse input into numbers and operators
        string = string.replace(" ", "")  # Remove spaces
        numbers = []
        operators = []
        current_number = ""
        for ch in string:
            if ch.isdigit() or ch == ".":
                current_number += ch
            elif ch in opchars:
                numbers.append(float(current_number))
                operators.append(ch)
                current_number = ""
        numbers.append(float(current_number))

        # Evaluate * / % first
        n = 0
        while n < len(operators):
            if operators[n] in "*/%":
                # Handle division/modulo by zero
                if operators[n] in "/%" and numbers[n + 1] == 0:
                    print("Error: Division or modulo by zero!")
                    return
                result = ops[operators[n]](numbers[n], numbers[n + 1])
                numbers[n] = result
                numbers.pop(n + 1)
                operators.pop(n)
            else:
                n += 1

        # Evaluate + -
        n = 0
        while n < len(operators):
            result = ops[operators[n]](numbers[n], numbers[n + 1])
            numbers[n] = result
            numbers.pop(n + 1)
            operators.pop(n)

        result = numbers[0]

        # Build a pretty version of the input string for display
        outputstr = ""
        for ch in string:
            if ch in opchars:
                outputstr += " " + ch + " "
            else:
                outputstr += ch

        # Clean up result display (int if whole number, else float)
        if result.is_integer():
            display_result = int(result)
        else:
            display_result = result
        print(f"\n{outputstr} = {display_result}\n")

        last_result = result

    except ValueError:
        print("\nError: Invalid number entered!")
    except IndexError:
        print("\nError: Invalid expression!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

	
	
	
			
			
	

	
version = "v1.2"

ops = { # operators
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide,
    "%": modulo
}
opchars = "*+/-%"

def main(): 
	os.system('cls' if os.name == 'nt' else 'clear')

	print(f"\n\nnonsense {version} - A Simple Python Calculator\n\nh=help\nq=quit\n")
	while True:
		userinput = input(":: ")
		inputhandler(userinput)
	
main()
