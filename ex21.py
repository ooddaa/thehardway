def add(a,b):
	print(f"adding {a} + {b}")
	return a + b
def substract(a,b):
	print(f"substracting {a} - {b}")
	return a - b
def multiply(a,b):
	print(f"multiplying {a} * {b}")
	return a * b
def divide(a,b):
	print(f"dividing {a} / {b}")
	return a / b

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq: {iq}")

print("PUZZLE")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes: {what}") 
