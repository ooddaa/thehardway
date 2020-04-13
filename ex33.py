from sys import argv

script, var, incr = argv

def while_loop(var, incr = 1):
	i = 0
	col = []
	while i < var:
		print(f"Top i is {i}")
		i += incr
		print(f"Bottom i is {i}")
		col.append(i)
		print(f"col is: {col}")

while_loop(int(var), int(incr))

