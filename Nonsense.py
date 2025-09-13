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
		
	for op_symbol, op_func in ops.items(): 
		if op_symbol in string:
			parts=string.split(op_symbol)
			result=op_func(int(parts[0]),int(parts[1]))
			print(result)
			
	

	

ops = { # operators
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide
}
def main():
	os.system("clear")
	print("\n\nnonsense - A Simple Python Calculator\n\nh=help\nq=quit\n")
	while True:
		userinput = input(":: ")
		inputhandler(userinput)
	
main()
