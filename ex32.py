fruits = ['apple', 'orange', 'peach']
prices = [12, 10, 23]
change = [1, 'cat', 2, 'parrot', 3, 'giraffe']

for fruit in fruits:
	print(f'Fruit is {fruit}')

for i in prices:
	print(f"Price is {i}")

print(f"Let's count to ten!")
for i in range(1,11):
	print(f"{i}")

elements = []

for i in change:
	if i in range(0,4):
		elements.append(i)
		print(f"{i} is added")
	else:
		print(f"{i} is not a number")

print(elements)
elements.extend(prices)
print(f"elements are {elements}")
elements.insert(1, 666)
elements.append(666)
print(f"inserted 666 as second and last items.\n{elements}")
print(f"let's count 666s - there are {elements.count(666)} of them. (should be 2)")
elements.clear()
