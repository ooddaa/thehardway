def print_two(*args):
	arg1, arg2 = args
	print("first {:>10} second {:<10}".format(arg1, arg2))
	#https://docs.python.org/3.0/tutorial/inputoutput.html)

def print_two_again(arg1, arg2):
	print("first {:^10} second {:<10}".format(arg1, arg2))

def print_one(arg1):	
	print(f"first {arg1}")

def print_none():
	print("I got nottin..")

print_two("Oda", "Nabunaga") 
print_two_again("Dim", "Vik")
print_one("one and only")
print_none()
