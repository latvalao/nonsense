import os

help_text = """
Syntax:
- Enter a calculation in one line.
- You can use these operators: +  -  *  /
- Examples:
    3+5*2      # multiplies 5*2 first, then adds 3
    12/4-1     # divides 12 by 4, then subtracts 1
- No spaces needed (spaces are okay too)
- To see this help again, type: h
"""


def addition(x, y):
	return x+y
	
def subtraction(x, y):
	return x-y

def multiply(x, y):
	return x*y
	
def divide(x, y):
	return x/y

def inputhandler(string:str):
	
	if "h" in string:
		print(help_text)
		return
		
	elif "q" in string:
		print("Bye bye!")
		quit()
		
		# Logic: Loop through items in the ops dictionary
	numbers = []
	operators = []
	current_number = ""
	for ch in string:
		if ch.isdigit() or ch == ".":
			current_number += ch
		elif ch in opchars:
			numbers.append(float(current_number))
			operators.append(ch)
			current_number=""
	numbers.append(float(current_number)) 
	
	
	n=0
	while n < len(operators):
		if operators[n] in "*/":   
			result = ops[operators[n]](numbers[n],numbers[n+1])
			numbers[n]=result
			numbers.pop(n+1)
			operators.pop(n)
		else:
			n += 1
	n=0
	while n < len(operators):
		if operators[n] in "+-":   
			result = ops[operators[n]](numbers[n],numbers[n+1])
			numbers[n]=result
			numbers.pop(n+1)
			operators.pop(n)
		else:
			n += 1
	result = numbers[0]
	print(f"{string} = {result}")
	
	
			
			
	

	
version = "v1.1"
ops = { # operators
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide
}
opchars = "*+/-"
def main(): 
	os.system('cls' if os.name == 'nt' else 'clear')

	print(f"\n\nnonsense {version} - A Simple Python Calculator\n\nh=help\nq=quit\n")
	while True:
		userinput = input(":: ")
		inputhandler(userinput)
	
main()
