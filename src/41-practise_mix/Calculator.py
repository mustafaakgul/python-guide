
print("hello")

def calc(x,y,operation):

	if operation not in "+-/*":
		return "Only +-/* ! "

	if operation == "+":
		return(str(x) + " " + operation " " + str(y) + " = " + str(x+y))
	elif operation == "-":
		return(str(x) + " " + operation " " + str(y) + " = " + str(x-y))
	elif operation == "/":
		return(str(x) + " " + operation " " + str(y) + " = " + str(x/y))
	elif operation == "*":
		return(str(x) + " " + operation " " + str(y) + " = " + str(x*y))


x = input("plse enter first number")
y = input("plse enter first number")
ops = input("ops")

print(calc(int(x),int(y), ops))