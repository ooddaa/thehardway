from sys import argv

script, val = argv
val = int(val)

if val > 0:
	print(f"{val} is > 0")
elif val < 0:
	print(f"{val} is < 0")
#if val == -2:
#	print(f"yo! some extra magic here!")
elif val == -2:
	print(f"yo! some extra magic here!")
else:
	print(f"{val} must be zero")

